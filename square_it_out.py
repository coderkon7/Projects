import random
print("Welcome! This program will generate a list of random numbers between a range you enter, square each number, and seperate the odd numbers from the even numbers.")

startNum = int(input("Enter the beginning number for the range: "))
endNum = int(input("Enter the ending number for the range: "))


random_numbers = []
for i in range(5):
    randomNum = random.randint(startNum, endNum)
    random_numbers.append(randomNum)

print(f"These are 5 random numbers generated between {startNum} and {endNum}: {random_numbers}")

def square(num):
    return num * num

# Squaring the numbers
squared_random_numbers = []

for num in random_numbers:
    squared_random_numbers.append(square(num))            

print("These are the random numbers squared: ", squared_random_numbers)

# Seperating Odd and Even square values
odd_numbers = []
even_numbers = []

for squared_num in squared_random_numbers:
    if squared_num % 2 == 0:
        even_numbers.append(squared_num)
    elif squared_num % 2 != 0:
        odd_numbers.append(squared_num)

print(f"Odd numbers: {odd_numbers}")
print(f"Even numbers: {even_numbers}")