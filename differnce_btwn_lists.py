def list_difference(list1, list2):
    difference = []

    for item in list1:
        if item not in list2:
            difference.append(item)

    for item in list2:
        if item not in list1:
            difference.append(item)

    return difference


input_list1 = [1, 2, 3, 4, 5]
input_list2 = [4, 5, 6, 7, 8]

result = list_difference(input_list1, input_list2)
print("Difference between the two lists:", result)
