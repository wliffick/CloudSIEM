# CloudSIEM: Lightweight SSH Threat Detector

## Overview
This project is a lightweight, Python-based security monitoring tool that simulates a basic SIEM (Security Information and Event Management) system. It monitors failed SSH login attempts on a Linux system, performs GeoIP and IP reputation lookups, and sends alert emails when suspicious activity is detected.

GitHub Repository: [https://github.com/wliffick/CloudSIEM](https://github.com/wliffick/CloudSIEM)

## Features
- Parses `/var/log/auth.log` for failed login attempts
- Counts failures by source IP address
- Performs GeoIP lookups using `ip-api.com`
- Checks IP reputation via AbuseIPDB OSINT API
- Sends email alerts when a threshold is exceeded
- Suppresses duplicate alerts using a local tracker
- Loads sensitive credentials from a `.env` file
- Modular and extensible Python code structure

## Directory Structure
```
main.py           - Entry point script
parser.py         - Extracts failed login attempts from log
geoip.py          - Resolves IP address to GeoIP information
ip_reputation.py  - Checks IPs using AbuseIPDB reputation API
alert.py          - Sends email alerts using SMTP
config.py         - Loads email credentials from .env
alert_tracker.py  - Prevents duplicate alerts for same IP
requirements.txt  - Python dependencies
README.md         - Project documentation
.gitignore        - Excludes secrets and cache files
.env              - Stores environment variables (excluded from git)
alerted_ips.json  - JSON file tracking previously alerted IPs
siem.log          - Local log file of tool activity
```

## Setup Instructions
1. **Clone this repository**:
   ```bash
   git clone https://github.com/wliffick/CloudSIEM.git
   cd CloudSIEM
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` file** in the root directory with the following variables:
   ```
   EMAIL_SENDER=your_email@gmail.com
   EMAIL_RECEIVER=your_email@gmail.com
   EMAIL_PASSWORD=your_gmail_app_password
   ABUSEIPDB_API_KEY=your_abuseipdb_api_key
   ```

5. **Run the tool** manually:
   ```bash
   python3 main.py
   ```

6. *(Optional)* **Schedule with cron** for periodic automated monitoring:
   ```
   crontab -e
   */10 * * * * /path/to/venv/bin/python3 /path/to/CloudSIEM/main.py >> /home/ubuntu/siem.log 2>&1
   ```

## Example Output
```
Failed login attempts by IP:
65.60.219.115 - 25 time(s)
    Location: Columbus, Ohio, United States
    Org: Wideopenwest Ohio | ASN: AS11776 Breezeline
    Reputation: 0% confidence
    Last Reported: None
    Total Reports: N/A
Email alert sent for IP 65.60.219.115
```

## Use Cases
- Demonstrates log parsing and basic SSH brute force detection
- Integrates external OSINT (GeoIP & IP reputation)
- Showcases modular Python, `.env` security, and SMTP alerts
- Strong showcase project for cybersecurity portfolios and interviews

## Future Enhancements
- HTML email formatting with alert summaries
- Centralized alert logging (e.g., database or CSV)
- Docker container for easier deployment
- Slack or Teams webhook integrations
- Web-based dashboard for real-time monitoring

## License
This project is licensed under the MIT License.

