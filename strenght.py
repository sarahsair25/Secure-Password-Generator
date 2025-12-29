import string

def password_strength(password: str) -> str:
    score = 0

    if len(password) >= 12:
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1
    if any(c.isupper() for c in password) and any(c.islower() for c in password):
        score += 1

    return ["Weak", "Fair", "Good", "Strong", "Very Strong"][score]
