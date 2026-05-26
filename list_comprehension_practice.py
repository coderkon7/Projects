num = int(input("Enter a number: "))

odd_numbers = [i for i in range(1, num) if i % 2 != 0]

print("\nOdd numbers below", num, ":")
print(odd_numbers)



fruits = input("\nEnter fruit names separated by space: ").split()

updated_fruits = [fruit.capitalize() for fruit in fruits]

print("\nUpdated Fruit List: ")
print(updated_fruits)