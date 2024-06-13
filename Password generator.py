import random
def generate_password(length):
    lower_case_letters = 'abcdefghijklmnopqrstuvwxyz'
    upper_case_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'
    punctuation = '!@#$%^&*()-_=+[]{}|;:,.<>?/~`'
    characters = lower_case_letters + upper_case_letters + digits + punctuation
    password = [
        random.choice(lower_case_letters),
        random.choice(upper_case_letters),
        random.choice(digits),
        random.choice(punctuation)
    ]
    password += [random.choice(characters) for _ in range(length - 4)]
    random.shuffle(password)
    return ''.join(password)

def main():
    length = int(input("Enter the desired length of the password (minimum 4): "))
    if length < 4:
        print("Password length should be at least 4 characters.")
        return
    password = generate_password(length)
    print(f"Generated password: {password}")
if __name__ == "__main__":
    main()
