# Creative Commons Zero v1.0 Universal
# Base64 Encoder/Decoder
########### By: AtlasWiki ###########
# Comment: this is my first python project, hope you enjoy

print("Hi, this script was made to encode/decode base64 codes")  
print("Made by: AtlasWiki \n")


# Entire Base64 Program
def b64_program():
    import base64
    user_decision = input(" \n encode or decode >> ")

# Decoding Process
# If user picks "decode", user will be prompted to input encoded message
    def decode():
        if (user_decision.lower() == "decode"):
            b64_decode = input ("\ndecode_input: ") # prompts user to input base64
            decoded_text = (base64.b64decode(b64_decode)) # base64 code gets decoded
            print('decode_output: ' + str(decoded_text).lstrip('b').strip('\'')) # prints decoded output
            input(" \n hit enter to continue        ")
    decode()

# Encoding Process
# If user picks "encode", user will be prompted to input decoded message
    def encode():
          if (user_decision.lower() == "encode"):
            text_input = input("\nencode_input: ")
            b_encoded = bytes(text_input, encoding = "utf-8") #encodes user-input to byte string
            b64_encoded = (base64.b64encode(b_encoded)) # text gets encoded
            print('encode_output: ' + str(b64_encoded).lstrip('b').strip('\'')) # prints encoded string
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


    
