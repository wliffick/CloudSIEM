from parser import parse_failed_logins
from alert import send_email_alert
from config import load_config
from geoip import lookup_ip

def main():
    """
    Main entry point for the SIEM-lite tool.
    Parses failed login attempts and sends alerts if thresholds are exceeded.
    """
    # Load environment variables (email credentials)
    config = load_config()

    # Parse auth.log for failed SSH logins
    failed_logins = parse_failed_logins()

    # Alert threshold (e.g., send alert if an IP has >= 3 failures)
    threshold = 3

    print("Failed login attempts by IP:")
    for ip, count in sorted(failed_logins.items(), key=lambda x: x[1], reverse=True):
        print(f"{ip} - {count} time(s)")

        #GeoIP lookup
        geo = lookup_ip(ip)
        if geo:
            print(f"    Location: {geo['city']}, {geo['region']}, {geo['country']}")
            print(f"    Org: {geo['org']} | ASN: {geo['as']}")

        if count >= threshold:
            send_email_alert(ip, count, geo)

if __name__ == "__main__":
    main()
