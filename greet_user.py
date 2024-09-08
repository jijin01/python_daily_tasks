def greet_user():
    name = input("Please enter your name: ").strip()

    if name == "":
        print("Name cannot be empty. Please provide a valid name.")
        return

    if not name.isalpha():
        print("Name should contain only letters. Please provide a valid name.")
        return

    print(f"Hello, {name}!")


greet_user()
