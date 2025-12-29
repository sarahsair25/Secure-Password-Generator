import secrets
import string

def generate_password(length: int, digits: bool, special: bool) -> str:
    if length < 8:
        raise ValueError("Password length must be at least 8")

    letters = string.ascii_letters
    digits_set = string.digits
    special_set = string.punctuation

    pool = letters
    password = [secrets.choice(letters)]

    if digits:
        pool += digits_set
        password.append(secrets.choice(digits_set))

    if special:
        pool += special_set
        password.append(secrets.choice(special_set))

    remaining = length - len(password)
    password.extend(secrets.choice(pool) for _ in range(remaining))
    secrets.SystemRandom().shuffle(password)

    return "".join(password)
