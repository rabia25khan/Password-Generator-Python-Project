import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    print("🔒 Simple Password Generator 🔒")
    length = int(input("Enter password length: "))
    password = generate_password(length)
    print("\nGenerated Password:", password)
