import json
import os

# File to store the record of alerted IPs
ALERT_TRACKER_FILE = "alerted_ips.json"

def load_alerted_ips():
    """
    Load the alerted IPs from the JSON file.

    Returns:
        dict: A dictionary mapping IP addresses to True if already alerted.
    """
    if not os.path.exists(ALERT_TRACKER_FILE):
        return {}
    
    with open(ALERT_TRACKER_FILE, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return {}

def save_alerted_ips(alerted_ips):
    """
    Save the alerted IPs dictionary to the JSON file.

    Parameters:
        alerted_ips (dict): Dictionary mapping IPs to True.
    """
    with open(ALERT_TRACKER_FILE, "w") as file:
        json.dump(alerted_ips, file, indent=4)

def has_been_alerted(ip):
    """
    Check if the IP has already been alerted.

    Parameters:
        ip (str): IP address to check.

    Returns:
        bool: True if already alerted, False otherwise.
    """
    alerted_ips = load_alerted_ips()
    return ip in alerted_ips

def mark_alerted(ip):
    """
    Mark the given IP as alerted.

    Parameters:
        ip (str): IP address to mark.
    """
    alerted_ips = load_alerted_ips()
    alerted_ips[ip] = True
    save_alerted_ips(alerted_ips)

