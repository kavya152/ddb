def register_user():
    print("=== User Registration ===")
    fullname = input("Full Name: ")
    email = input("Email: ")
    password = input("Password: ")
    confirm_password = input("Confirm Password: ")

    if password != confirm_password:
        print("Error: Passwords do not match.")
        return

    # Save the user data in a file
    with open("users.txt", "a") as file:
        file.write(f"{fullname},{email},{password}\n")

    print("Registration successful!")

if __name__ == "__main__":
    register_user()

