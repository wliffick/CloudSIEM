import requests
import os

def check_ip_reputation(ip):
    """
    Queries AbuseIPDB to check the reputation of a given IP address.

    Parameters:
        ip (str): The IP address to check.

    Returns:
        dict: A dictionary containing reputation information such as:
              - abuseConfidenceScore
              - country
              - ISP
              - domain
              - lastReportedAt
              - usageType
              Returns None if the request fails.
    """

    # Load the API key from environment variable
    api_key = os.getenv("ABUSEIPDB_API_KEY")

    if not api_key:
        print("Error: AbuseIPDB API key is not set in environment variables.")
        return None

    # Prepare the API request to AbuseIPDB
    url = "https://api.abuseipdb.com/api/v2/check"
    querystring = {
        "ipAddress": ip,
        "maxAgeInDays": "90"  # Look back up to 90 days
    }
    headers = {
        "Accept": "application/json",
        "Key": api_key
    }


    try:
        # Make the GET request to the AbuseIPDB API
        response = requests.get(url, headers=headers, params=querystring)
        response.raise_for_status()  # Raise an error if the request failed

        # Extract useful fields from the response JSON
        data = response.json().get("data", {})
        return {
            "ip": ip,
            "abuseConfidenceScore": data.get("abuseConfidenceScore"),
            "country": data.get("countryCode"),
            "isp": data.get("isp"),
            "domain": data.get("domain"),
            "usageType": data.get("usageType"),
            "lastReportedAt": data.get("lastReportedAt")
        }

    except requests.exceptions.RequestException as e:
        # Print any request/connection errors
        print(f"Error querying AbuseIPDB for IP {ip}: {e}")
        return None
