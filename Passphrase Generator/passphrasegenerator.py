import random

# Function to generate a passphrase from a txt file containign all words
def passphrasegenerator(input_file, complexity):
    # Open the file and read all the lines
    with open(input_file, "r") as in_file:
        lines = in_file.readlines()
    
    if complexity == "1":
        number_of_words = min(4, len(lines))
    elif complexity == "2":
        number_of_words = min(6, len(lines))
    elif complexity == "3":
        number_of_words = min(8, len(lines))

    # Select (complexity) random words from the list
    passphrase = random.sample(lines, number_of_words)

    # Join the words together and remove the \n
    passphrase = "".join(passphrase).replace("\n", "-")

    if passphrase[-1] == "-": 
        passphrase = passphrase[:-1]
    # Return the passphras=
    print('Your new passsword is: {}'.format(passphrase))


# We wnat to understand how complex they want the passqword to be
# consider simple as 4 words, moderate and 6 and complex as 8 words joined by hyphens

# Ask the user for the complexity of the password
complexity = 0
while complexity not in ["1", "2", "3"]:
    complexity = input("How complex would you like the passphrase to be? \n 1. Simple \n 2. Moderate \n 3. Complex \n")

passphrasegenerator('every_20_words.txt', complexity)
