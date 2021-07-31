# Creative Commons Zero v1.0 Universal
# By: AtlasWiki
print("\nHi this is a character/word counter\n")


usr_input = input("\ntext: ")
alphabet = "abcdefghijklmnopqrstuvwxyz"
# Individual lists
space_list = []
space = " "
space_count = ""
letter_list = ""
char_list = ""
letter_count = ""
numbers = "0123456789"
num_list = []
num_count = ""
spec_chars_list = []
spec_chars_count = ""
spec_chars_used_list = []
spec_chars_used = ""
word_list = ""

# Algorithm to detect characters and adds them to different lists
for character in usr_input:
    # adds spaces to a space list and letter list
    if character == " ":
        space_list.append(character)
        space_count = "".join(space_list)
        letter_list = letter_list + character
    # adds lowercase letters to letter and character list 
    elif character in alphabet:
        letter_list = letter_list + character
        char_list = char_list + character
    # adds uppercase letters to letter and character list  
    elif character in alphabet.upper():
        letter_list = letter_list + character
        char_list = char_list + character
    # number list
    elif character in numbers:
        num_list.append(character)
    # anything other than numbers, letters, and spaces are put in special characters list
    else: 
        spec_chars_list.append(character)
        spec_chars_count = "".join(spec_chars_list)
        spec_chars_used_list.append(character)
        spec_chars_used = "".join(spec_chars_used_list)

# combines all lists into strings
num_count = "".join(num_list)
letter_count = "".join(letter_list)
char_count = "".join(char_list)
# spaces are removed or used as delimiters for letters
# words are formed and separated in the list
word_list = list(letter_list.split(" "))

# remove '' character in user's input
for list_of_words in usr_input:
    if '' in word_list:
        word_list.remove('')
       
# print special characters but converts to a dictionary and back to string to remove repeated characters
print("\n special characters used: " + str(list(dict.fromkeys(spec_chars_used))))
print("\n letters used: " + str(list(dict.fromkeys(letter_list.replace(" ", "")))))

# print statement for length count of all different type of characters
print("\n\n" + "  Total characters: " + str(len(spec_chars_count) + len(letter_count) + len(num_count)) 
        + "," + "  Special characters: "
        + str(len(spec_chars_count)) + "," 
        + "  Numbers: "+ str(len(num_count)) + ","
        + "  Spaces: " + str(len(space_count)) + ","
        + "  Letters: " + str(len(char_count)) + ","
        + "  Words: " + str(len(word_list)))
# prompts user to exit python script before window immediately closes
input("\npress enter to exit")
