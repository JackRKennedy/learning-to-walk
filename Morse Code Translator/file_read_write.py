# file to remove definition from the dictionary text file

with open("Oxford English Dictionary words and definitions.txt", "r") as f:
    lines = f.readlines()
    with open("Oxford English Dictionary words and definitions.txt", "r") as f:
        lines = f.readlines()

    # Remove text after the first space in each line, then remove any space after word
    lines = [line.split(" ", 1)[0] for line in lines]
    lines = [line.strip() for line in lines]
    
    #remove any blank lines from file for efficiency
    lines = [line for line in lines if line != ""]
    
    #now handle edge cases - such as a word starting with a number or a symbol
    #remove any words whose first letter is not a letter
    lines = [line for line in lines if line[0] in "abcdefghijklmnopqrstuvwxyz" or line[0] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
    
    #for ease of programming, make all words lower case
    lines = [line.lower() for line in lines]

    # write lines back to a new file called 'just english words'
    with open("just english words.txt", "w") as f:
        for line in lines:
            f.write(line + "\n")
