def find_factor(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors


try:
    num = int(input("Enter the number: "))
    print(*find_factor(num))
except ValueError:
    print("Invalid Input")
