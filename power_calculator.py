base = int(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))
answer = 1
for i in range(exponent):
    answer = answer*base
    print(answer)