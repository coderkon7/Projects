# if input_num//x and input_num//y
# x (first number) = 10 and y (second number) = 10
#  if x and y both equal 10 and when multiplied they equal the user input (input_num)...
# it could then tell the user that there is a valid square root for that number, and tell the user what that number is

# if number times 2 equals input_num, then it's found the square root

'''while sqrt != inputNum:
    sqrt *= 2
    if sqrt == inputNum:
        print(sqrt, "is the square root of ", inputNum)
    if sqrt != inputNum:
        sqrt //= 2
        sqrt += 1
        print("Haven't found the square root of that number yet")'''


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