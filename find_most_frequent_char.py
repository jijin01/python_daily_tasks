def most_frequent_char(string):
    max_count = 0
    most_frequent = ""
    for char in string:
        if char != ' ':
            count = string.count(char)
            if count > max_count:
                max_count = count
                most_frequent = char

    return most_frequent


user_input = input("Enter a string: ")
result = most_frequent_char(user_input)
print("The most frequent charactor in the provided string is", result)
