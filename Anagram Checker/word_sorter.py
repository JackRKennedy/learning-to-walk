from docx import Document


# take in the file, and return a dictionary of lists
def create_word_length_lists_from_file(input_file):
    word_length_lists = {}
    with open(input_file, "r") as file:
        for line in file:
            word = line.strip()  # Remove newline characters
            length = len(word)
            if length not in word_length_lists:
                word_length_lists[length] = []
            word_length_lists[length].append(word)
    # each key is a length, and each value is a list of words with that length
    return word_length_lists
