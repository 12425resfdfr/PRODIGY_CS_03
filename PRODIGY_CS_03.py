import re

def check_password_strength(password):
    # Initialize strength score
    strength_score = 0
    feedback = []

    # Criteria for password strength
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    digit_criteria = bool(re.search(r'[0-9]', password))
    special_char_criteria = bool(re.search(r'[^A-Za-z0-9]', password))

    # Evaluate strength based on criteria
    if length_criteria:
        strength_score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if uppercase_criteria:
        strength_score += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")

    if lowercase_criteria:
        strength_score += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")

    if digit_criteria:
        strength_score += 1
    else:
        feedback.append("Password should contain at least one number.")

    if special_char_criteria:
        strength_score += 1
    else:
        feedback.append("Password should contain at least one special character.")

    # Determine strength level
    if strength_score == 5:
        strength_level = "Very Strong"
    elif strength_score == 4:
        strength_level = "Strong"
    elif strength_score == 3:
        strength_level = "Moderate"
    elif strength_score == 2:
        strength_level = "Weak"
    else:
        strength_level = "Very Weak"

    # Provide feedback
    print(f"Password Strength: {strength_level}")
    if feedback:
        print("Feedback to improve your password:")
        for suggestion in feedback:
            print(f"- {suggestion}")
    else:
        print("Your password meets all the recommended criteria.")

def main():
    # Ask the user for a password
    password = input("Enter a password to check its strength: ")

    # Check password strength
    check_password_strength(password)

if __name__ == "__main__":
    main()