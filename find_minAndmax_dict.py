def find_min_max(dic):
    if not isinstance(dic, dict):
        return "The input should be a dictionary"
    if not dic:  # dic == {} ie check for empty dic
        return "The dictionary should not empty"

    min_value = min(dic.values())
    max_value = max(dic.values())
    return min_value, max_value


sample_input = {'a': 10, 'b': 35, 'c': 50, 'd': 15}
min_val, max_val = find_min_max(sample_input)
print(f"Minimum value is {min_val} and maximum value is {max_val}.")
