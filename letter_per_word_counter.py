# Creative Commons Zero v1.0 Universal
# By: AtlasWiki
usr_input = input("\n\ntext: ")
print("\n")
letter_str = ""
word_list = ""
alphabet = "abcdefghijklmnopqrstuvwxyz"

# add spaces and letters to the same list
def add_char_list():
    global letter_str
    for char in usr_input:
        if char == " ":
            letter_str = letter_str + char 
        elif char in alphabet or alphabet.upper(): 
            letter_str = letter_str + char         
add_char_list()

# separate letters and spaces to form words
def make_word_list():
    global letter_str
    global word_list
    # split ups all letters and spaces into objects/words
    letter_str = letter_str.split(" ")
    # converts to a list
    word_list = list(letter_str)
make_word_list()

# removes spaces
def space_remover():
    global word_list
    # constantly checks and remove the '' character
    for chars in usr_input:
        if '' in word_list:
            word_list.remove('')
space_remover()

# counts letters
def letter_counter():
    # takes index of the words in the word list and counts char length
    for words in word_list:
        print(f"{words} - "  + str(len(word_list[word_list.index(words)])))
    quest_input = input("\n Add all character lengths? [y/n] ")
    # joins all words together and counts all chars
    if quest_input.lower() == "y":
        len_sum = len("".join(word_list))
        print("\n TOTAL: " + str(len_sum)) 
letter_counter()

input("\npress enter to exit")
