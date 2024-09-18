def count_word_occurrences(sentence):
    if not isinstance(sentence, str):
        return "Invalid input: Please enter a valid string."
    if not sentence.strip():
        return "Empty input provided."

    cleaned_sentence = ''
    for char in sentence.lower():
        if char.isalnum() or char.isspace():
            cleaned_sentence += char
        else:
            cleaned_sentence += ' '

    words = cleaned_sentence.split()

    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    return word_counts


user_input = input("Enter a sentence: ")
result = count_word_occurrences(user_input)
print("\n")
print(f"Count of word occurrences is: {result}")
