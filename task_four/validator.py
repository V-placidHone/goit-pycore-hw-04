import re

NAME_RE = re.compile(r"^[A-Za-zА-Яа-яІіЇїЄєҐґ]+(?:-[A-Za-zА-Яа-яІіЇїЄєҐґ]+)*$")
PHONE_RE = re.compile(r"^\+?\d+$")  # дозволяє або тільки цифри, або + і цифри

def validate_name(name: str) -> None:
    if not NAME_RE.fullmatch(name):
        raise ValueError("Invalid name. Use letters, hyphens only (e.g., Jean-Pierre).")

def validate_phone(phone: str) -> None:
    if not PHONE_RE.fullmatch(phone):
        raise ValueError("Invalid phone. Use digits only or +digits (e.g., 1234567890 or +1234567890).")