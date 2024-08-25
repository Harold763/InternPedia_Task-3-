import secrets
import string

def generate_password(length=12, use_symbols=True):
    # Define the characters to use
    alphabet = string.ascii_letters + string.digits
    if use_symbols:
        alphabet += string.punctuation

    # Generate a secure random password
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password

def password_generator():
    print("Secure Password Generator")
    
    while True:
        try:
            length = int(input("Enter the length of the password (default is 12): ") or 12)
            if length < 8:
                print("Password length should be at least 8 characters.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        use_symbols = input("Include symbols (y/n)? ").lower() in ['y', 'yes']
        
        password = generate_password(length, use_symbols)
        print(f"Generated password: {password}")
        
        another = input("Generate another password (y/n)? ").lower()
        if another not in ['y', 'yes']:
            break

if __name__ == "__main__":
    password_generator()
