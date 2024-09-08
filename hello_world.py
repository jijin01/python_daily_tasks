def print_hello_world(message="Hello, World!"):
    if not isinstance(message, str):
        raise ValueError("Input must be a string.")

    if message.strip() == "":
        print("Message is empty")
        message = "Hello, World!"

    print(message)


# Test cases
print_hello_world()
print_hello_world("Hi there!")
print_hello_world("   ")
