def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt).strip())
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def convert_celsius_to_fahrenheit():
    print("Welcome to the Celsius to Fahrenheit Converter!")

    celsius = get_float_input("Please enter the temperature in Celsius: ")

    fahrenheit = (celsius * 9 / 5) + 32
    print(f"{celsius}°C is equal to {fahrenheit}°F.")


convert_celsius_to_fahrenheit()
