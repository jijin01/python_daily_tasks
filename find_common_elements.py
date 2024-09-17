def find_common_elements(list1, list2):
    if not list1 or not list2:
        return []

    # Find common elements
    commonList = []
    for x in list1:
        if x in list2:
            commonList.append(x)

    return commonList


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = [1, 10, 11, 2, 7, 20, 3, 21]
common_elements = find_common_elements(list1, list2)
print(common_elements)
