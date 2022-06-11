print('''
-----------------------------------------
    Email Slicer Using Python
-----------------------------------------
''')

def email_slicer(email):
    '''
        This function slices the Email Address into two parts :- Username and Domain from the position of the '@' sign.

        Argument : Email Address
        Return: Username, Domain
    
    '''
    split_index = email.index('@')
    return email[:split_index], email[split_index + 1:]

entry_text = input("Press U to Use or Press Q to Exit: ")
if entry_text.upper() == 'Q':
    quit()

email=input("Enter your Email:- ")
username, domain = email_slicer(email)
print("Your username is {0} and domain is {1}".format(username, domain))

