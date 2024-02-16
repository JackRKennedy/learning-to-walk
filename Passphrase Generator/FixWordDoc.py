#The purpose of this program is to read in the word doc
#and write out to a new txt file

from docx import Document

def update_lines(input_file, output_file, interval):
    with open(input_file, 'r') as infile:
        lines = infile.readlines()

    updated_lines = lines[::interval]

    with open(output_file, 'w') as outfile:
        outfile.writelines(updated_lines)

# Call the function with your file names and interval
update_lines('all_words.txt', 'every_20_words.txt', 20)


