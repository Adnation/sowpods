
# Method to find all the legitimate words
def get_legimate_words(letters, sowpods):
    legitimate_words = []
    # Iterate on each word of the dictionary
    for word in sowpods:
        # Set the flag as True
        is_word_legitimate = True
        # Iterate on each character of word
        for character in word:
            # If character not in letters break the loop
            if character not in letters:
                is_word_legitimate = False
                break
        # Append the word to output list
        if is_word_legitimate:
            legitimate_words.append(word)
    # Return
    return legitimate_words


sowpods = [
    'FAST',
    'FEST',
    'PEST',
    'PAST',
    'PAT',
    'FAD',
    'FEAST',
    'DIRT'
]

letters = ['A', 'P', 'F', 'D', 'S', 'T', 'E']

print(get_legimate_words(letters, sowpods))
