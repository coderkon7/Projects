try:
    age = int(input("Enter your age: "))

    if age%2 == 0:
        print("Your age is an even number.")
    elif age%2 != 0:
        print("Your age is an odd number.")
except ValueError:
    print("ERROR: Please make sure your number is an integer value.")