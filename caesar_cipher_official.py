# Creative Commons Zero v1.0 Universal
# Caesar Cipher encoder/decoder
# will add english dictionary soon
# Made by: AtlasWiki

# global variables
alphabet = "abcdefghijklmnopqrstuvwxyz"
shifted_list = []
rep_chars = []
forbidden_chars = []
space = " "


def caesar_cipher():
    # start menu - prompts user on letter shifting options
    print("\nCURRENT ALPHABET: " +alphabet)
    shift_options = input("\n[1] Shift only capitalized letters \n[2] Shift only lower case letters \n[3] Both " + 
    "\n[4] Customize alphabet \n\n>>> ")
    # takes user back to start menu if not selecting any of the options
    if not (shift_options == "1" or shift_options == "2" or shift_options == "3" or shift_options == "4"):
        caesar_cipher()    
   
    def task():
        global shifted_list 
        global rep_chars
        global forbidden_chars
        shifted_list = []
        rep_chars = []
        forbidden_chars = []
        #opt 1: shift capitalized letters only 
        def opt_one():
            global shifted_list
            if shift_options == "1":
                user_text = input("\ntext: ")
                shift = 0
                shifted_word = ""
        
                # shifting algorithm - shifts uppercase letters individually 
                # uppercase letters are shifted 26 times
                for list in range(0, 27): # loop does the shift algorithm 26 times
                    shift = list
                    shifted_list = []
                    # shift algorithm - loop lasts until algorithm goes through all characters
                    # of user's input
                    for letter in user_text:
                        if letter in alphabet.upper():
                            # letter gets converted to array index and takes the sum of varaible shift
                            shifted_num = (alphabet.index(letter.lower()) + shift) % len(alphabet)
                           
                            # converts new sum to alphabet
                            shifted_letter = alphabet[shifted_num]
                           
                            # converts user's input back to uppercase
                            uppercase = shifted_letter.upper()
                           
                            # adds all shifted letters to a list
                            shifted_list.append(uppercase)
                            
                            # combines everything at the end
                            shifted_word = "".join(shifted_list)
                               
                        # does not shift characters other than uppercase
                        else:
                            # adds letter to the shift list
                            shifted_list.append(letter)

                            # combines all letters in the shift list
                            shifted_word = "".join(shifted_list)

                    # displays all 26 shifts and outcomes
                    print(str([list]) + ": " + shifted_word)
                                      
        opt_one()
        #opt 2: shift lowercase letters only 
        def opt_two():
            # user is taken to option 2 based on user's choice
            # prompt user to input text for encrypting/decrypting 
            # prompt user to input the shift amount for each letter
            if shift_options == "2":
                user_text = input("\ntext: ")
                shift = 0
                # shift uppercase letters individually 
                for list in range(0, 27): # loop does the shift algorithm 26 times
                    shift = list
                    shifted_list = []
                    for letter in user_text:
                        if letter in alphabet.lower():
                            shifted_num = (alphabet.index(letter) + shift) % len(alphabet)
                            shifted_letter = alphabet[shifted_num]
                            shifted_list.append(shifted_letter)
                            shifted_word = "".join(shifted_list)
                        # does not shift characters other than uppercase
                        else:
                            shifted_list.append(letter)
                            # combines all letters into a string
                            shifted_word = "".join(shifted_list)
                    print(str([list]) + ": " + shifted_word)
        opt_two()
        #opt 3: shift all letters  
        def opt_three():        
            if shift_options == "3": 
                user_text = input("\ntext: ")
                # resets shift 
                shift = 0
                for list in range(0, 27): # shift algorithm for 26 times
                    shift = list 
                    shifted_list = []
                    # checks for characters in user_input and shifts them
                    for letter in user_text:
                        # checks for lowercase letters and shifts letter
                        if letter in alphabet.lower():
                            shifted_num = (alphabet.index(letter) + shift) % len(alphabet)
                            shifted_letter = alphabet[shifted_num]
                            shifted_list.append(shifted_letter)
                            shifted_word = "".join(shifted_list)
                        # checks for uppercase letters and shifts letter
                        elif letter in alphabet.upper(): 
                            shifted_num = (alphabet.index(letter.lower()) + shift) % len(alphabet)
                            shifted_letter = alphabet[shifted_num]
                            uppercase = shifted_letter.upper()
                            shifted_list.append(uppercase)
                            shifted_word = "".join(shifted_list)
                        # Add any other characters to the list
                        else:
                            shifted_list.append(letter)
                            shifted_word = "".join(shifted_list)
                    # print all 26 shifts
                    print(str([list]) + ": " + shifted_word)
        opt_three()

        # opt 4: Customize alphabet
        def opt_four():
            global alphabet
            global rep_chars 
            # creates repeated/forbidden characters list
            rep_chars = []
            rep = ""
            forbid = ""
            # sets previous alphabet to current
            old_alphabet = alphabet
            # displays options
            if shift_options == "4":
                print("\ncurrent alphabet: " + alphabet + "\n")
                char_choice = input("[a] Add Character \n[b] Change whole alphabet \n[c] Reset alphabet"
                + "\n[d] Reverse alphabet\n\n[e] Go back \n\n>>> ")
                # adding character to alphabet option
                if char_choice == "a":
                    char_choice = input("\nadd character(s) to before or after a certain letter in the alphabet? [b/a] ")
                    # takes user input for adding characters before/after a letter in alphabet
                    if char_choice.lower() == "before" or char_choice.lower() == "b":
                        print("\ncurrent alphabet: " + alphabet + "\n")
                        letter_place = input("behind/before [any letter]: ")
                        if not len(letter_place) == 1:
                            print("\n***you could only specify 1 letter***")
                            print("\n   going back to menu  ")
                            opt_four() 
                        add_char = input("[+] ")
                        # FOR LOOP - Checks for spaces. Adds characters to alphabet if there are no spaces 
                        for letter in add_char:
                            # repeated characters are added in the repeated chars list
                            if letter in alphabet: 
                                rep_chars.append(letter)
                            # detect spaces
                            elif letter == " ":
                                print("\nSpaces are not allowed!\n")
                                forbidden_chars.append("space")    
                            # insert user's characters to the front of the alphabet
                            else:
                                edit_alphabet = list(alphabet)
                                edit_alphabet.insert(alphabet.index(letter_place.lower()), letter)
                                alphabet = "".join(edit_alphabet)
    
                        # LOOP - Checks for forbidden characters. Adds characters to alphabet if there are no spaces 
                        if not rep_chars == []:
                            print("\nyou cannot have repeated letters")
                            rep = list(dict.fromkeys(rep_chars))
                            print("\n repeated_characters: " + str(rep))
                            rep = str(rep)
                            print(" removed: " + rep)
                        # checks if forbidden characters list is empty or else forbidden chars are displayed
                        if not forbidden_chars == []:
                            forbid = str(list(dict.fromkeys(forbidden_chars)))
                            print(" removed: " + forbid)
                        # print statements for previous and current alphabet
                        print("\nold alphabet: " + old_alphabet)
                        print("added: " + add_char.strip(rep))
                        print("\nnew alphabet: " + alphabet)
                    
                    # AFTER OPTION - allows user to input characters in the back of alphabet
                    elif char_choice.lower() == "after" or char_choice.lower() == "a":
                        print("\ncurrent alphabet: " + alphabet + "\n")
                        letter_place = input("after/in-front [any letter]: ")
                        add_char = input("[+] ")
                        # Algorithm for checking characters and adding it to their proper lists
                        for letter in add_char[::-1]: # reverses the order user's letters/input
                            if letter in alphabet: 
                                rep_chars.append(letter)
                            elif letter == " ":
                                print("\nSpaces are not allowed!\n")
                                forbidden_chars.append("space") 
                            else:
                                edit_alphabet = list(alphabet)
                                # takes array index of letter and inserts user's characters after it
                                edit_alphabet.insert(alphabet.index(letter_place.lower()) + 1, letter)
                                alphabet = "".join(edit_alphabet)
                        # checks for repeated characters
                        if not rep_chars == []:
                            print("\nyou cannot have repeated letters")
                            rep = list(dict.fromkeys(rep_chars))
                            print("\n repeated_characters: " + str(rep))
                            rep = str(rep)
                            print(" removed: " + rep)
                        # checks for forbidden characters
                        if not forbidden_chars == []:
                            forbid = str(list(dict.fromkeys(forbidden_chars)))
                            print(" removed: " + forbid)
                    # print statement for old and current alphabet   
                        print("\nold alphabet: " + old_alphabet)
                        print("added: " + add_char.strip(rep)) 
                        print("\nnew alphabet: " + alphabet)
                    # sends user back to prompt question
                    else:
                        caesar_cipher()
                    # prompt user if user wants to use the new alphabet
                    use_alpha = input("\nwould you like to use this alphabet [y/n] ? ")
                    if use_alpha.lower() == "y":
                        caesar_cipher()
                    # gets sent back to option 4 and returns previous alphabet
                    else:
                        alphabet = old_alphabet
                        opt_four()
                # Allows user to type up the alphabet instead
                elif char_choice.lower() == "b":
                    print("\ncurrent: " +alphabet)
                    replace_alpha = input("replace: ")
                    # sets to new alphabet and removes repeated letters
                    new_alphabet = list(dict.fromkeys(replace_alpha))
                    # informs user that repeated letters are removed if length does not match
                    if (len(replace_alpha) != new_alphabet):
                        print("\n*Removed Repeated Letters*")
                    # set new alphabet
                    new_alphabet = "".join(new_alphabet)
                    print("\nnew: " + new_alphabet)
                    # prompts user if user wants to use new alphabet
                    use_alpha = input("\nwould you like to use this alphabet [y/n] ? ")
                    # if yes, user gains new alphabet or else retains the previous one
                    if use_alpha.lower() == "y":
                        alphabet = new_alphabet
                        caesar_cipher()
                    else:
                        opt_four()
                # Reset Alphabet
                if char_choice.lower() == "c":
                    use_alpha = input("\nwould you like to confirm changes [y/n] ? ")
                    if use_alpha.lower() == "y":
                        alphabet = "abcdefghijklmnopqrstuvwxyz"
                        caesar_cipher()
                    elif char_choice.lower() == "n":
                        caesar_cipher()
                    else:
                        opt_four()
                # Reverse order of alphabet
                if char_choice.lower() == "d":
                    use_alpha = input("\nwould you like to confirm changes [y/n] ? ")
                    if use_alpha.lower() == "y":
                        alphabet = list(alphabet)
                        alphabet.reverse() 
                        alphabet = "".join(alphabet)
                        alphabet = alphabet 
                        caesar_cipher()
                # go back
                if char_choice.lower() == "e":
                    caesar_cipher()  
        opt_four()

        # gives user the decision to continue using the program or the desire to exit
        def continue_quest():
            enc_ = input("\nwant to continue ? [y/n] ")
            if enc_.lower() == "y":
                caesar_cipher()
            elif enc_.lower() == "n":
                print("\nthank you for using this")
                quit()
            else:
                continue_quest()
        continue_quest()
    task()

caesar_cipher()
        