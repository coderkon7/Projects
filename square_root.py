inputNum= int(input("Enter the number you wish to find the square root of: "))

sqrt = 1
while sqrt != inputNum:    
    if sqrt * sqrt == inputNum:
        print(sqrt, "is the square root of ", inputNum)
        break
    elif sqrt * sqrt != inputNum:
        sqrt += 1
#    print("Current value of variable sqrt: ", sqrt)
#    print("Current value of variable inputNum: ", inputNum)