def valid_input(user_input):
    while True:
        try:
            radius = float(input(user_input))
            if isinstance(radius, (float, int)):
                return radius
        except ValueError:
            print("Enter a valid input")


def area_of_circle():
    pie = 3.14159
    radius = valid_input("Enter the radius of the Circle: ")
    area = pie * radius ** 2
    area = round(area, 2)

    print(f"Area of the circle is {area}")


area_of_circle()
