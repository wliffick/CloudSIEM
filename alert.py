import smtplib
from email.message import EmailMessage
import os

def send_email_alert(ip, count, geo=None, reputation=None):
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

    if reputation:
        body += "\n\nIP Reputation Info:\n"
        body += f"  Abuse Confidence Score: {reputation.get('abuseConfidenceScore')} / 100\n"
        body += f"  ISP: {reputation.get('isp')}\n"
        body += f"  Domain: {reputation.get('domain')}\n"
        body += f"  Country: {reputation.get('countryCode')}\n"
        body += f"  Total Reports: {reputation.get('totalReports')}\n"
        body += f"  Last Reported: {reputation.get('lastReportedAt')}\n"

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
