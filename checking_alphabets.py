

userinput = input("Please type what you would like to check is a letter/alphabet.").lower()

if userinput.isalpha():
    print("You typed: ", userinput, "\nThat is in the alphabet.")

else:
    print("You typed: ", userinput, "\nThat is not a known letter in the alphabet.")