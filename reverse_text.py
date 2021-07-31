# Creative Commons Zero v1.0 Universal
# By: AtlasWiki
# reverse text
num_input = int(input("\n# of texts to encode/decode: "))

# prints inputs/outputs based on user's number input
for number in range(1, num_input + 1):
    text_input = input("\ntext" + str([number]) + ": ")
    # reverses text
    print("  \n result: " +  text_input[::-1])
    
input("\npress enter to exit")