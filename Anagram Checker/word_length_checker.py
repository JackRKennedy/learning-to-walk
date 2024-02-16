# sort the fule, then find the longest word in the file
with open("all_words.txt", "r") as infile:
    lines = infile.readlines()
    sorted_lines = sorted(lines, key=lambda x: len(x))
    with open("all_words_sorted.txt", "w") as outfile:
        for line in sorted_lines:
            outfile.write(line.lower())

# Now, we can use the sorted file to find the longest word in the file.

with open("all_words_sorted.txt", "r") as infile:
    lines = infile.readlines()
    longest_word_length = 0
    for line in lines:
        if len(line) > longest_word_length:
            longest_word_length = len(line)
            print(longest_word_length)
