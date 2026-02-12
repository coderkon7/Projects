import random

num = int(input("Welcome to the city! Here, if you type the wrong number, you will be sent to prison!!! Choose wisely: "))

jailNumChance = random.randint(1,10)
if jailNumChance == 5:
    jailNum = 5
else:
    jailNum = num

if jailNum == num:
    print("Oops!!! You picked", num, ", which is a number that sends you to JAIL!!!!!")
    
else:
    print("WOW!!! You are safe!! You picked the right number!!! YOU ARE A GENIUS!!!! I'll buy you a donut:)")