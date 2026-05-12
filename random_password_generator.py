import random
password = ""
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['1','2','3','4','5','6','7','8','9']

print("Welcome to my password generator!")
print("This will generate a password with both uppercase and lowercase letters, along with numbers. You can also choose the length of the generated password.")
length = int(input("How long would you like the length of the password to be (including all letters and numbers)? "))

for i in range(length):
    letter_or_integer = random.randint(1,2)
    if letter_or_integer == 1:
        caseType = random.randint(1,2)
        if caseType == 1:
            password += alphabet[random.randint(0,25)]
        elif caseType == 2:
            password += alphabet[random.randint(0,25)].upper()

    elif letter_or_integer == 2:
        password += numbers[random.randint(0,8)]

print("Here is your generated password: ", password)