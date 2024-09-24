def find_intersection(set1, set2):
    if not isinstance(set1, set) or not isinstance(set2, set):
        return "Both inputs must be sets."

    intersection = set1 & set2

    if len(intersection) == 0:
        return "No common elements."

    return intersection


print(find_intersection({1, 2, 3}, {3, 4, 5}))
print(find_intersection({1, 2, 3}, {4, 5, 6}))
print(find_intersection({}, {}))
print(find_intersection({1, 2}, "not a set"))
