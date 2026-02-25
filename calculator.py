print("Welcome to Amazing Dad's Calculator, where it figures out what you don't know")
Number1 = int(input("Please enter your absolute favorite number - "))
Number2 = int(input("Please enter another amazing number :-) - "))
operator = input("Select the operator that you would like to use: 1 for Addition, 2 for Subtraction, 3 for Multiplication, or 4 for Division - ")
if operator == "1":
    print (f"Your favorite number ({Number1}) added to the amazing number ({Number2}) equals", Number1+Number2)
if operator == "2":
    print (f"Your favorite number ({Number1}) subtacted by the amazing number ({Number2}) equals", Number1-Number2)
if operator == "3":
    print (f"Your favorite number ({Number1}) multiplied by the amazing number ({Number2}) equals", Number1*Number2)
if operator == "4":
    print (f"Your favorite number ({Number1}) divided by the amazing number ({Number2}) equals", Number1/Number2)
print("Thank you for using the best calculator you've ever seen. Have a splendid day!")
