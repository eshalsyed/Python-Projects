# Password strength checker program


# Users password requirements
password_requirements = print("""\nInclude at least 8 characters and the followings:
                               \n- Numbers 
                              \n- Capital letters 
                              \n- Lower case letters 
                              \n- Speacial characters \n""")

# List of speacial characters to be checked
special_characters = "!@£$%&*#€÷/≠=-_:;<>.,|/±§~`"

# ALL requirements
def all_requirements(password):
        length = len(password) >=8
        numbers = any(characters.isdigit() for characters in password)
        capital = any(characters.isupper() for characters in password)
        lower = any(characters.islower() for characters in password)
        special = any(characters in special_characters for characters in password)

        return length and numbers and capital and lower and special

# if user doesnt input valid password
while True:

    password = input("Enter password: ")

    # checks for ALL requirements
    if all_requirements(password):
        print("\nMeets all requirements \nStrong password!")
        break
        
    # Checks length short
    if len(password) <8:
        print("\nInclude 8 characters")
        continue

    # Checks for no specials
    if not any(characters in special_characters for characters in password):
        print("\nInclude special characters")
            
    # Checks for no numbers 
    if not any(characters.isdigit() for characters in password):
        print("\nIncludes numbers")
            
    # Checks for no upper case
    if not any(characters.isupper() for characters in password):
        print("\nInclude upper case letters")
            
    # Checks for no lower case
    if not any (characters.lower() for characters in password):
        print("\nIncludes lower case letters")
