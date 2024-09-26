def valid_input(num):
    while True:
        try:

            user_input = float(input(num))
            if isinstance(user_input, (float, int)):
                return user_input
        except ValueError:
            print("Invalid input")


def bmi_calculator(height, weight):
    BMI = weight / (height ** 2)
    if BMI < 18.5:
        print(f"Your BMI is {round(BMI, 2)}, you are underweight.")
    elif BMI >= 35:
        print(f"Your BMI is {round(BMI, 2)}, you are clinically obese.")
    elif 18.5 <= BMI < 25:
        print(f"Your BMI is {round(BMI, 2)}, you have a normal weight.")
    elif BMI < 30:
        print(f"Your BMI is {round(BMI, 2)}, you are slightly overweight.")
    elif BMI < 35:
        print(f"Your BMI is {round(BMI, 2)}, you are obese.")
    else:
        print(f"Your BMI is {round(BMI, 2)}, you are clinically obese.")
    return BMI


weight = valid_input("Enter your weight in kg : ")
height = valid_input("Enter your height in mtr: ")
result = bmi_calculator(height, weight)

