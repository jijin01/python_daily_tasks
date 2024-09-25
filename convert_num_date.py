def calculate_year(total_days):
    days_in_year = 365
    year = total_days // days_in_year
    remaining_days = total_days % days_in_year
    return year, remaining_days


def calculate_months(days):
    days_in_month = 30
    month = days // days_in_month
    remaining_days = days % days_in_month
    print(remaining_days)
    print(days)
    return month, remaining_days


def convert_days_to_ymd(user_input):
    year, remaining_days = calculate_year(user_input)
    month, remaining_days = calculate_months(remaining_days)  # remaining days from year  in convert function
    return year, month, remaining_days


def is_valid_input(value):
    return value.isdigit()


num_days = input("Enter the number of days:")
if not is_valid_input(num_days):
    print("Invalid input")
else:
    num_days = int(num_days)

    years, months, days = convert_days_to_ymd(num_days)
    print(f"{num_days} days is approximately {years} years, {months} months, and {days} days.")
