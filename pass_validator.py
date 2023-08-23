import re
import os

print('enter the file name and extension or skip if your file name has the word "pass" in it ')
pass_file = input('file: ') 
print('\n')

# function create a generator object to read passwords in a file
def return_passwords(file):
    with open(validate_pass_file(file), "r") as passwords:
        for password in passwords:
            yield password.strip('\n')

# function to check if user chose an existing file
def validate_pass_file(file):
    global pass_file
    if file == locate_pass_file(pass_file):
        return file
    else:
        file = locate_pass_file(pass_file)
        if len(file) > 1:
            if file.count(pass_file):
                return pass_file
            else:
                print('There are ' + str(len(file)) + ' password files: ' + str(file))
                pass_file = input('which file would you like to select: ')
        else:
            pass_file = file[0]
        return pass_file
    
# function to automatically find a password file if user does not specify an existing file
def locate_pass_file(file):
    file = [txt_file for txt_file in os.listdir() if txt_file.endswith('.txt') and re.search('.*[pP][aA][sS]+[Ww]*.', txt_file)]
    return file

# function to check password strength with regex
def validate_passwords():
    for password in return_passwords(pass_file):
        password = password.strip('\n')
        print('\n\n' + password + '\n', '-' * 12)
        if not len(password) >= 12:
            print(' •password length is less than 12 characters')
        if not re.search("[a-z]", password):
            print(' •missing a lowercase letter')
        if not re.search("[A-Z]", password):
            print(' •missing an uppercase letter')
        if not re.search("[0-9]", password):
            print(' •missing a number')
        if not re.search("[!@#$%^&\*\(\)\-\[\]:;',.?~]", password):
            print(' •missing a special character')
        else: 
            print("✓ is very secure and meets all requirements")
    return True

if validate_passwords():
    print('\n\n',' finished succesfully ','', sep='-*-' * 3)
    print('file checked: ' + validate_pass_file(pass_file) + '\n')
