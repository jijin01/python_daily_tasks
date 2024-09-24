def valid_input(string):
    user_input = input(string).strip()
    if user_input:
        return user_input
    else:
        print("Please enter a valid sentence.")
        return valid_input(string)


sentence = valid_input("Enter a sentence to find the largest word:")
sentence = sentence.replace(",", "").replace(".", "")
words = sentence.split()
largest_word = ""
for word in words:
    if len(word) > len(largest_word):
        largest_word = word
print(f"The largest word in the sentence is : {largest_word}")
