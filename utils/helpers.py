import json
import random
import secrets
import time
import string
import os
from faker import Faker

fake = Faker()



def save_local_storage(driver, path):
    """Save localStorage content to a JSON file."""
    local_storage = driver.execute_script("return {...localStorage};")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(local_storage, f)


def load_local_storage(driver, path):
    """Load localStorage content from a JSON file."""
    with open(path, "r", encoding="utf-8") as f:
        local_storage = json.load(f)
    for key, value in local_storage.items():
        driver.execute_script(f"localStorage.setItem('{key}', '{value}');")


def save_cookies(driver, path):
    """Save cookies to file"""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(driver.get_cookies(), f)


def load_cookies(driver, path):
    """Load cookies from file"""
    with open(path, "r", encoding="utf-8") as f:
        cookies = json.load(f)
    for cookie in cookies:
        cookie.pop("sameSite", None)
        driver.add_cookie(cookie)


def generate_email(prefix):
    """Generate name"""
    ts = int(time.time())
    return f"{prefix}+{ts}@test.com"


def generate_password(length=5):
    """Generate password"""
    lowers = string.ascii_lowercase
    uppers = string.ascii_uppercase
    digits = string.digits
    specials = "!@#$%^&*()-_+=[]{}|:;,.?/"

    pwd = [
        secrets.choice(lowers),
        secrets.choice(uppers),
        secrets.choice(digits),
        secrets.choice(specials),
    ]

    all_chars = lowers + uppers + digits + specials
    pwd += [secrets.choice(all_chars) for _ in range(length - len(pwd))]

    secrets.SystemRandom().shuffle(pwd)
    return "".join(pwd)


def gen_creds(prefix="at"):
    """Generate test credentials"""
    print({
        "email": generate_email(prefix),
        "password": generate_password()
    })
    return {
        "email": generate_email(prefix),
        "password": generate_password()
    }

def generate_pet_data(owner_email):
    """Generate test pet data in the same format as NEW_PET_DATA."""
    pet_types = ["cat", "dog", "parrot", "hamster", "rabbit"]
    genders = ["Male", "Female"]

    return {
        "name": fake.first_name(),
        "type": random.choice(pet_types),
        "age": random.randint(1, 15),
        "gender": random.choice(genders),
        "pic": f"https://picsum.photos/seed/{fake.uuid4()}/300/300",
        "owner_name": owner_email or fake.email(),
        "likes_count": 0,
        "liked_by_user": None,
    }