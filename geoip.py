import requests

def lookup_ip(ip):
    """
    Uses ip-api.com to fetch GeoIP info for a given IP address.

    Parameters:
        ip (str): The IP address to look up.

    Returns:
        dict: A dictionary with location data, or None if lookup failed.
    """
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}", timeout=5)
        data = response.json()

        if data["status"] == "success":
            return {
                "ip": ip,
                "country": data["country"],
                "region": data["regionName"],
                "city": data["city"],
                "org": data["org"],
                "as": data["as"]
            }
        else:
            return None
    except Exception as e:
        print(f"GeoIP lookup failed for {ip}: {e}")
        return None
