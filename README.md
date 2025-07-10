CloudSIEM: Lightweight SSH Threat Detector
===================================

Overview
--------
This project is a lightweight, Python-based security monitoring tool that simulates a basic SIEM (Security Information and Event Management) system. It monitors failed SSH login attempts on a Linux system, performs GeoIP lookups, and sends alert emails when suspicious activity is detected.

Features
--------
- Parses /var/log/auth.log for failed login attempts
- Counts failures by source IP address
- Performs GeoIP lookups using ip-api.com
- Sends email alerts when a threshold is exceeded
- Loads sensitive credentials from a .env file
- Modular and extensible Python code structure

Directory Structure
-------------------
main.py         - Entry point script
parser.py       - Extracts failed login attempts from log
geoip.py        - Resolves IP address to GeoIP information
alert.py        - Sends email alerts using SMTP
config.py       - Loads email credentials from .env
.env            - Stores environment variables (excluded from git)
README.md       - Project documentation
.gitignore      - Excludes .env and venv from version control

Setup Instructions
------------------
1. Clone this repository:
   git clone https://github.com/YOUR_USERNAME/siem-lite-ssh-monitor.git
   cd siem-lite-ssh-monitor

2. Create and activate a virtual environment:
   python3 -m venv venv
   source venv/bin/activate

3. Install dependencies:
   pip install -r requirements.txt

4. Create a `.env` file in the root directory with the following content:
   EMAIL_SENDER=your_email@gmail.com
   EMAIL_RECEIVER=your_email@gmail.com
   EMAIL_PASSWORD=your_app_password

5. Run the main script:
   python3 main.py

Example Output
--------------
Failed login attempts by IP:
174.216.7.151 - 4 time(s)
    Location: Chicago, Illinois, United States
    Org: Comcast Cable | ASN: AS7922

[Email Alert Sent]

Use Cases
---------
- Demonstrates log parsing and basic threat detection
- Integrates external OSINT (GeoIP API) for enrichment
- Shows use of Python environment variables and modular code
- A strong project for GitHub or technical interviews

Future Enhancements
-------------------
- HTML email formatting
- Centralized alert logging (e.g., to a database or CSV)
- Real-time monitoring with cron or systemd
- Docker containerization for deployment
- Web dashboard or Slack alert integration

License
-------
This project is licensed under the MIT License.
