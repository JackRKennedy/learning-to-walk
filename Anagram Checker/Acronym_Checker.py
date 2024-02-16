#import the function that creates a dictionary of lists
from word_sorter import create_word_length_lists_from_file

#set that dictionary as the function using the file all_words_sorted.txt
word_length_lists = create_word_length_lists_from_file('all_words_sorted.txt')

#now we want to take in a user input word, firstlu check to see if it exists in the dictionary

#if it foes exist int he dictionary, we want to print either th elist of anagrams, oe a message saying that there are no anagrams

word_to_check = input('Enter a word to check: ').lower()
#check for type error (string)
if not isinstance(word_to_check, str):
    print('Please enter a word, not a number or other character.')
    exit()

length = len(word_to_check)
possible_anagrams = []
if length in word_length_lists:
    #check to see if the word is in the list
    if word_to_check in word_length_lists[length]:
        for word in word_length_lists[length]:
            # we want to check if every letter thats in the word to check is in the word in the list 
            # if it is, we want to add it to the list of possible anagrams
            if all(letter in word for letter in word_to_check) and all(letter in word_to_check for letter in word):
                #we must check that no other letters are in the word that are not in the word to check
                #if there are, we want to remove the word from the list of possible anagrams
                possible_anagrams.append(word)     
            else: 
                 continue   
    else: 
        print('I don\'t recognise {} as a word, hence I don\'t believe there are any anagrams for it'.format(word_to_check))
        exit()   
else:
    print('I don\'t recognise {} as a word, hence I don\'t believe there are any anagrams for it'.format(word_to_check))
    exit()        
#now we want to check if the word to check is the only word in the list of possible anagrams
#if it is, we want to print a message saying that there are no anagrams
if len(possible_anagrams) == 1:
        print('There are no anagrams for {}'.format(word_to_check))
        exit()

print('The anagrams for {} are: {}'.format(word_to_check, possible_anagrams))