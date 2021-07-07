# Base64 Encoder/Decoder
########### By: AtlasWiki ###########
# Comment: this is my first python project, hope you enjoy

print("Hi, this script was made to encode/decode base64 codes")  
print("Made by: AtlasWiki")

# Entire Base64 Program
def b64_program():
    import base64
    user_decision = input("Would you like to decode or encode: ")

# Decoding Process
# If user picks "decode", user will be prompted to input encoded message
    def decode():
        if (user_decision.lower() == "decode"):
            b64_decode = input ("decode: ") # prompts user to input base64
            print(base64.b64decode(b64_decode)) # base64 code gets decoded
            input("hit enter to continue")
    decode()

# Encoding Process
# If user picks "encode", user will be prompted to input decoded message
    def encode():
        if (user_decision.lower() == "encode"):
            b64_input = input("encode: ")
            b64_encoded = bytes(b64_input, encoding = "utf-8") #encodes user-input to byte string
            print(base64.b64encode(b64_encoded)) # encodes to base64
            input("hit enter to continue")
    encode()

# Question/prompt loops until user selects "encode" or "decode"
    while not (user_decision.lower() == "encode" or user_decision.lower() == "decode"):
        user_decision = input("Would you like to decode or encode: ")
        # User gets sent back to the encoding/decoding process based on their new input
        if (user_decision.lower() == "encode" or user_decision.lower() == "decode"):
            if (user_decision.lower() == "encode"):
                encode()
            else: 
                decode()
            break # while loop will break when user either chooses encode or decode
    # prompts the user to make a decision to use the program again before closing the program
    # user must make a decision based on the options or else will go in a permanent loop
    reset_input = input("Do you want to decode/encode more stuff? ")
    if (reset_input.lower() == "yes" or reset_input.lower() == "sure"):
        b64_program()
    elif (reset_input.lower() == "no" or reset_input.lower() == "nope"):
            print("bye, thanks for using this")
            input("press enter to exit")
    else:
        while not (reset_input.lower() == "no" or reset_input.lower() =="nope"):
            print("that is not even an option")
            reset_input = input("Do you want to decode/encode more stuff? ")
            if (reset_input.lower() == "yes" or reset_input.lower() == "sure"):
                b64_program()
                break
            if (reset_input.lower() == "no" or reset_input.lower() == "nope"):
                print("bye, thanks for using this")
                input("press enter to exit")
                break
b64_program()


    
