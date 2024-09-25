def find_prime_num(num):
    list_of_prime_num = []
    for i in range(2, num + 1):
        is_prime = True
        for n in range(2, i):
            if i % n == 0:
                is_prime = False
                break
        if is_prime:
            list_of_prime_num.append(i)

    return list_of_prime_num


user_input = input("Enter a number: ")
if not user_input.isdigit():
    print("Invalid input")
else:
    user_input = int(user_input)
    result = find_prime_num(user_input)
    print(f" The prime numbers with in the provided range is: {result}")
