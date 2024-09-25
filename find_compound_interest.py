def get_valid_input(num):
    value = input(num)
    try:
        user_input = float(value)
        if isinstance(user_input, float):
            return user_input

    except ValueError:
        print("Input should be a valid number")
        return 0


principal_amount = get_valid_input("Enter the principal amount: ")
rate_of_interest = get_valid_input("Enter the annual interest rate (as a decimal): ")
time_of_period = get_valid_input("Enter the time (in years): ")
num_of_time = get_valid_input("Enter the number of times interest is compounded per year: ")

final_amount = principal_amount * (1 + rate_of_interest / num_of_time) ** (num_of_time * time_of_period)

compound_interest = final_amount - principal_amount
print(f"The compound interest is rs.{compound_interest}.")
