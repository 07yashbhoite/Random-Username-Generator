import random
import string

# Pre-defined lists of adjectives and nouns
adjectives = ["Cool", "Happy", "Funky", "Epic", "Brave", "Sneaky", "Jolly", "Swift", "Sassy", "Clever"]
nouns = ["Tiger", "Dragon", "Panda", "Wizard", "Phoenix", "Knight", "Ninja", "Ranger", "Fox", "Wolf"]

# Function to generate random usernames
def generate_username(include_numbers=True, include_special_chars=True, length=None):
    adj = random.choice(adjectives)
    noun = random.choice(nouns)

    username = adj + noun

    # Add numbers if required
    if include_numbers:
        username += str(random.randint(10, 99))
    
    # Add special characters if required
    if include_special_chars:
        username += random.choice("!@#$%^&*")
    
    # Adjust length if specified
    if length and len(username) < length:
        username += ''.join(random.choices(string.ascii_letters + string.digits, k=length - len(username)))
    
    return username

# Function to save usernames to a file
def save_usernames_to_file(usernames, filename="usernames.txt"):
    try:
        with open(filename, "a") as file:
            file.write("\n".join(usernames) + "\n")
        print(f"Usernames saved to {filename}.")
    except Exception as e:
        print(f"Error saving usernames to file: {e}")

# Main function for user interaction
def main():
    print("Welcome to the Username Generator!")
    while True:
        try:
            num_usernames = int(input("How many usernames would you like to generate? "))
            include_numbers = input("Include numbers? (yes/no): ").strip().lower() == "yes"
            include_special_chars = input("Include special characters? (yes/no): ").strip().lower() == "yes"
            length = input("Specify username length (leave blank for default): ").strip()
            length = int(length) if length else None

            usernames = [
                generate_username(include_numbers, include_special_chars, length)
                for _ in range(num_usernames)
            ]

            print("\nGenerated Usernames:")
            print("\n".join(usernames))

            save_option = input("Would you like to save these usernames to a file? (yes/no): ").strip().lower()
            if save_option == "yes":
                save_usernames_to_file(usernames)

            continue_option = input("Generate more usernames? (yes/no): ").strip().lower()
            if continue_option != "yes":
                print("Thank you for using the Username Generator. Goodbye!")
                break
        except ValueError:
            print("Invalid input. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
