from alert import send_email_alert
from geoip import lookup_ip

def main():
    # Simulated test IP and failure count
    test_ip = "8.8.8.8"
    test_count = 99  # A high value to simulate threshold breach

    # Optional: Lookup geo info for test IP
    geo_info = lookup_ip(test_ip)

    # Send test alert
    send_email_alert(test_ip, test_count, geo_info)

if __name__ == "__main__":
    main()

