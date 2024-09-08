def get_positive_number(rectangle):
    while True:
        try:
            value = float(input(rectangle).strip())

            if value <= 0:
                print("Value must be positive. Please enter a valid number.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def calculate_rectangle_area():
    print("Welcome to the Rectangle Area Calculator!")

    length = get_positive_number("Please enter the length of the rectangle: ")

    width = get_positive_number("Please enter the width of the rectangle: ")

    area = length * width
    print(f"The area of the rectangle is: {area} square units")


calculate_rectangle_area()
