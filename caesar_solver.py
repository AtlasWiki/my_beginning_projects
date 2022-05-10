# Creative Commons Zero v1.0 Universal
# Caesar Cipher encoder/decoder
# Made by: AtlasWiki

#note: be sure to download the caesar_wordlist.txt file 

import time
from colorama import Fore, Style, init
import os
init(autoreset=True)

def caesar():
    text = input(Fore.GREEN + Style.DIM + '\nciphertext: ' )
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    word_counter = 0
    corr_word_count = 0
    break_loop = False

# shift function
    def shifts(min,max):
        shifted_letters = []
        for character in text:
            for shift in range(min, max):
                if character in alphabet:
                    shifted_nums = (alphabet.index(character) + shift) % len(alphabet)
                    shifted_letters += alphabet[shifted_nums]
                elif character in alphabet.upper():
                    shifted_nums = (alphabet.upper().index(character) + shift) % len(alphabet)
                    shifted_letters += alphabet.upper()[shifted_nums]
                else:
                    shifted_letters += character
            
                if len(shifted_letters) % 1 == 0:
                    shifted = ''.join(shifted_letters)
                    break
        return shifted

# check function: verifies words in shift
    with open('caesar_wordlist.txt', 'r') as dict:
            dict = dict.read().split('\n')
            for all_shifts in range(1, 26):
                if break_loop == True:
                    break    
                corr_word_count = 0
                word_counter = 0
                a_shift = shifts(all_shifts, 26)
                a_shift_copy = a_shift
                for character in a_shift:
                    if character.lower() not in alphabet and character != ' ':        
                        a_shift_copy = a_shift_copy.replace(character, ' ')

                shift_words = a_shift_copy.split()
                print(Fore.RED + Style.DIM + 'trying shift # ' + str(all_shifts) + '...' )

                for word in shift_words:
                    word_counter = word_counter + 1
                    for english_word in dict:
                        if word.lower() == english_word:
                            corr_word_count = corr_word_count + 1
                        percentage = (corr_word_count/len(shift_words)) * 100
                        if percentage >= 66 and word_counter == len(shift_words):
                            print( Fore.YELLOW + '\n '  + str(all_shifts) + ' place(s) shifted' +  '\n')
                            print( ' ' * 10 + '[plaintext]: ' + a_shift + "\n")
                            print( Fore.GREEN + Style.DIM + ' ' * 10 + '+' + str(percentage) + "% matched\n")
                            print( Fore.GREEN + Style.DIM + ' ' * 10 + 'time taken: ' + str(time.process_time()) + ' seconds')
                            if len(shift_words) > 3:
                                break_loop = True
                            percentage = 0
                            break
                            
            
            if input("\nWould you like to try again? (y/n) ").lower()=='y':
                os.system('cls')
                caesar()
                
            else:
                quit()
            
caesar()
        
