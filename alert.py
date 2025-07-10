import smtplib
from email.message import EmailMessage
import os

def send_email_alert(ip, count, geo=None):
    """
    Sends an email alert when a specific IP exceeds the failed login threshold.

    Parameters:
        ip (str): The IP address to alert on.
        count (int): The number of failed login attempts from that IP.
        geo (dict, optional): GeoIP info (country, city, org, ASN)
    """
    # Load credentials and email info from environment variables
    sender_email = os.getenv("EMAIL_SENDER")
    receiver_email = os.getenv("EMAIL_RECEIVER")
    app_password = os.getenv("EMAIL_PASSWORD")

    subject = f"[ALERT] Failed Login Attempts from {ip}"
    body = f"Detected {count} failed login attempts from IP: {ip}"

    if geo:
        body += "\n\nGeoIP Information:\n"
        body += f"  Location: {geo.get('city')}, {geo.get('region')}, {geo.get('country')}\n"
        body += f"  Org: {geo.get('org')} | ASN: {geo.get('as')}\n"

    # Construct the email message
    msg = EmailMessage()
    msg.set_content(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email

    # Connect to Gmail SMTP server and send the email
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(sender_email, app_password)
            smtp.send_message(msg)
            print(f"Email alert sent for IP {ip}")
    except Exception as e:
        print(f"Failed to send email: {e}")
