from dotenv import load_dotenv
import os

def load_config():
    """
    Loads environment variables from a .env file using python-dotenv.

    Returns:
        dict: A dictionary of loaded environment variables.
    """
    load_dotenv()
    return {
        "EMAIL_SENDER": os.getenv("EMAIL_SENDER"),
        "EMAIL_RECEIVER": os.getenv("EMAIL_RECEIVER"),
        "EMAIL_PASSWORD": os.getenv("EMAIL_PASSWORD")
    }
