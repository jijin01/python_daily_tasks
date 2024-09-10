def remove_duplicates(input_list):
    if not isinstance(input_list, list):
        return "Input must be a list."

    # Remove duplicates by converting the list to a set and back to a list
    unique_elements = list(set(input_list))

    return unique_elements


print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))
print(remove_duplicates([]))
print(remove_duplicates([1, "hello", 2, "hello"]))
print(remove_duplicates("not a list"))
