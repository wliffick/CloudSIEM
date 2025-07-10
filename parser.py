from collections import defaultdict

def parse_failed_logins(log_file_path="/var/log/auth.log"):
    """
    Parses the authentication log to find failed SSH login attempts
    from invalid users and counts them by IP address.

    Parameters:
        log_file_path (str): Path to the authentication log file.

    Returns:
        dict: A dictionary with IP addresses as keys and failed attempt counts as values.
    """
    failed_logins = defaultdict(int)

    with open(log_file_path, "r") as log_file:
        for line in log_file:
            # We're looking for lines with both 'Invalid user' and 'from <IP>'
            if "Invalid user" in line and "from" in line:
                parts = line.split()
                if "from" in parts:
                    index = parts.index("from")
                    if index + 1 < len(parts):
                        ip = parts[index + 1]
                        failed_logins[ip] += 1

    return failed_logins
