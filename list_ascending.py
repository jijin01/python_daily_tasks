def sort_list(myList):
    if all(isinstance(num, (int, float)) for num in myList):
        myList.sort()
        return myList

    else:
        return "Error: List must contain only integers or floats."


this_list = [10, 20, 45, 8, 9, 3, -9, -2, 96, 17, 56, 81, 0, -56]
result = sort_list(this_list)
print(result)

