import re

def check_password_strength(password):
    # Define the criteria for a strong password
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[ @!#$%^&*()_+{}:;'\"<>,.?/\\|`~-]", password) is None

    # Create a dictionary with results of all checks
    password_strength = {
        "length_error": length_error,
        "digit_error": digit_error,
        "uppercase_error": uppercase_error,
        "lowercase_error": lowercase_error,
        "symbol_error": symbol_error
    }

    # Calculate score
    strength_score = 5 - sum(password_strength.values())

    # Evaluate strength
    if strength_score == 5:
        return "Strong"
    elif 3 <= strength_score < 5:
        return "Moderate"
    else:
        return "Weak"

# User input
password = input("Enter your password to check its strength: ")

# Check the password
strength = check_password_strength(password)
print(f"Password strength: {strength}")
