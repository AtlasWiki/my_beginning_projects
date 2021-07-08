# Creative Commons Zero v1.0 Universal
# Base64 Encoder/Decoder
########### By: AtlasWiki ###########
# Comment: this is my first python project, hope you enjoy

print("Hi, this script was made to encode/decode base64 codes")  
print("Made by: AtlasWiki \n")


def b64_program():
    import base64
    user_decision = input(" \n encode or decode >> ")
    # decoding process
    def decode():
        if (user_decision.lower() == "decode"):
            decode_count = int(input("\n number of messages to decode (type in #'s): "))
            # creates # of lines for inputting code and outputting text
            for number in range(1, decode_count + 1):
                line_num = input("\n" + str([number]) + ": ") # line number 
                decoded_text = (base64.b64decode(line_num)) # base64 code gets decoded
                print('[o]: ' + str(decoded_text).lstrip('b').strip('\'')) # prints decoded output
            input(" \n\n hit enter to continue        ")
    decode()

    # encoding process
    def encode():
        if (user_decision.lower() == "encode"):
            encode_count = int(input("\n number of messages to encode (type in #'s): "))
            for number in range(1, encode_count + 1):
                line_num = input("\n" + str([number]) + ": ") # line number 
                b_encoded = bytes(line_num, encoding = "utf-8") #encodes user-input to byte string
                b64_encoded = (base64.b64encode(b_encoded)) # text gets encoded
                print('[o]: ' + str(b64_encoded).lstrip('b').strip('\'')) # prints encoded string
            input(" \n hit enter to continue        ")
    encode()
# Question/prompt loops until user selects "encode" or "decode"
    while not (user_decision.lower() == "encode" or user_decision.lower() == "decode"):
        user_decision = input(" \n encode or decode >> ")
        # User gets sent back to the encoding/decoding process based on their new input
        if (user_decision.lower() == "encode" or user_decision.lower() == "decode"):
            if (user_decision.lower() == "encode"):
                encode()
            else: 
                decode()
            break # while loop will break when user either chooses encode or decode
            
# prompts the user to make a decision to use the program again before closing the program
 # user must make a decision based on the options or else will go in a permanent loop
 # user is taken back to the entire program when wanting to encode/decode again
# Asks user if the user wants to encode/decode more codes
# takes user back to the beginning of the program when wanting to encode/decode again
    reset_input = input("\n Do you want to decode/encode more stuff? (y/n) ")
    if (reset_input.lower() == "y"):
        b64_program()
# program ends when user does not want to encode/decode again
    elif (reset_input.lower() == "n"):
            print("bye, thanks for using this")
            input("press enter to exit")
# keeps repeating question when user specifies an unknown option
    else:
        while not (reset_input.lower() == "n"):
            print("\nError >> that is not even an option \n\n *****please try again*****\n")
            reset_input = input("Do you want to decode/encode more stuff? (y/n) ")
        # takes user to the beginning of the program when user wants to encode/decode again
            if (reset_input.lower() == "y"):
                b64_program()
                break
         # program ends when user does not want to encode/decode
            if (reset_input.lower() == "n"):
                print("bye, thanks for using this")
                input("press enter to exit")
                break
b64_program()


    
