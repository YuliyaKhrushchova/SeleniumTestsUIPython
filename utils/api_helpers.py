import requests
from utils.config import API_REGISTER_URL


def register_user_api(creds, timeout=10):
    payload = {
        "email": creds["email"],
        "password": creds["password"],
        "confirm_password": creds["password"],
    }
    try:
        r = requests.post(API_REGISTER_URL, json=payload, timeout=timeout)
        return {"status": r.status_code, "text": r.text}
    except Exception as e:
        return {"status": None, "error": str(e)}
