# Decoder for DA Assessment

# Read in a .txt file with format 'number word' for each line
# each number will be used to organise a pyramid of numbers, with 1 being the top of the pyramid

#   1
#  2 3
# 4 5 6
# 7 8 9 10

# The final word from each like i.e 1, 3, 6 in this case, will be the message decoded.


def decode_message():

    # first read in the text file
    encoded_message = "./coding_qual_input.txt"  # I've kept the file in the same folder, would need to update file path otherwise
    broken_down_message = {}  # initialise dictionary
    line_count = 0
    with open(encoded_message, "r") as file:  # read in text file
        for line in file:
            # print(line) -> this was a test that file reads in okay
            number, word = (
                line.strip().split()
            )  # strip whitespace and split the line by space
            broken_down_message[int(number)] = (
                word  # performing own quality of life check on number being an int
            )
            line_count += 1

    decoded_message = []  # initialise decoded message as list for easier manipulation

    # take the first word as standard, then the third, then the 6th, then 10th etc
    # general solution is the last key + the current row number
    # ie, for the fourth word, we would be looking for the current index (6) + 4 = 10 - general solution for this should be n * (n + 1) // 2

    # calculate the index for each word based on above solution
    i = 0
    word_index = 0
    word_index_list = []

    while word_index < line_count:
        word_index = i * (i + 1) // 2
        word_index_list.append(word_index)
        i += 1

    # now we have a list with the key for each word in the sentence, in order
    # this does include 0 which needs to be removed first.

    for _ in word_index_list:
        if _ < 1:
            word_index_list.remove(_)

    # now join each word in the list to form one sentence

    for _ in word_index_list:
        decoded_message.append(broken_down_message[_])

    secret_message = " ".join(decoded_message)

    return secret_message
