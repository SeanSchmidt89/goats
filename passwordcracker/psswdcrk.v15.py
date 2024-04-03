import hashlib
import random
import string

# Function to generate a random password of length n
def generate_password(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

# Function to hash a password using SHA-256 algorithm
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

if __name__ == "__main__":
    # Prompt the user to input the target hash value
    target_hash = input("Enter the target SHA-256 hash: ")

    # Crack passwords up to length 8
    for length in range(1, 9):
        print(f"Attempting to crack passwords of length {length}...")

        # Iterate over all possible passwords of length 'length'
        for _ in range(10**6):
            password = generate_password(length)
            hashed_password = hash_password(password)
            
            # Check if the hashed password matches the target hash
            if hashed_password == target_hash:
                print(f"Password cracked: {password}")
                exit()

    print("Password not found.")
