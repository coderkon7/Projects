# ignore the code below in triple quotes (''')
'''print("Half Pyramid Pattern of Stars (*):")
#n = int(input("Enter the number of rows: "))
rows = 5
n = 5
#space = " "
#spaceAmount = 5
for i in range(rows):
    for l in range(n, 0, -1):
        print("*" * l, end="")
        #spaceAmount -= 1
    for j in range(i+1):
        print("* ", end="")
    print()'''


print("Mirrored Triangle")
rows = int(input("Enter the number of rows: "))
for i in range(rows, 0, -1):
    print("*" * i)