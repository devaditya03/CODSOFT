import random
import string
import secrets

def generate_unique_password():
    """
    A unique password generator that allows users to specify
    password length and complexity options.
    """
    print("=" * 50)
    print("🔐 UNIQUE PASSWORD GENERATOR 🔐")
    print("=" * 50)
    
    # Get password length from user
    while True:
        try:
            length = int(input("\nEnter desired password length (minimum 8): "))
            if length >= 8:
                break
            else:
                print("⚠️  Password length must be at least 8 characters.")
        except ValueError:
            print("⚠️  Please enter a valid number.")
    
    # Get complexity options
    print("\nComplexity Options:")
    print("1. Lowercase letters only (a-z)")
    print("2. Lowercase + Uppercase letters (a-z, A-Z)")
    print("3. Letters + Numbers (a-z, A-Z, 0-9)")
    print("4. Letters + Numbers + Special characters (a-z, A-Z, 0-9, !@#$%^&*)")
    
    while True:
        try:
            complexity = int(input("\nChoose complexity level (1-4): "))
            if 1 <= complexity <= 4:
                break
            else:
                print("⚠️  Please choose a number between 1 and 4.")
        except ValueError:
            print("⚠️  Please enter a valid number.")
    
    # Define character sets based on complexity
    if complexity == 1:
        char_set = string.ascii_lowercase
        required_chars = []
    elif complexity == 2:
        char_set = string.ascii_letters
        required_chars = [random.choice(string.ascii_lowercase), 
                         random.choice(string.ascii_uppercase)]
    elif complexity == 3:
        char_set = string.ascii_letters + string.digits
        required_chars = [random.choice(string.ascii_lowercase), 
                         random.choice(string.ascii_uppercase),
                         random.choice(string.digits)]
    else:  # complexity == 4
        char_set = string.ascii_letters + string.digits + "!@#$%^&*"
        required_chars = [random.choice(string.ascii_lowercase), 
                         random.choice(string.ascii_uppercase),
                         random.choice(string.digits),
                         random.choice("!@#$%^&*")]
    
    # Generate password using secrets for better security
    if complexity > 1:
        # Ensure required characters are included
        password_chars = required_chars[:]
        remaining_length = length - len(required_chars)
        password_chars += [secrets.choice(char_set) for _ in range(remaining_length)]
        # Shuffle to randomize position of required characters
        secrets.SystemRandom().shuffle(password_chars)
        password = ''.join(password_chars)
    else:
        password = ''.join(secrets.choice(char_set) for _ in range(length))
    
    # Display the generated password
    print("\n" + "=" * 50)
    print("✅ PASSWORD GENERATED SUCCESSFULLY!")
    print("=" * 50)
    print(f"🔑 Your Password: {password}")
    print(f"📏 Length: {len(password)} characters")
    print(f"🎯 Complexity Level: {complexity}")
    print("=" * 50)
    
    return password

# Run the password generator
if __name__ == "__main__":
    generate_unique_password()
