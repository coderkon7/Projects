bill = float(input("How much did the item cost? $"))
payment = float(input("How much did you pay the shopkeeper? $"))

amount_due = payment - bill
print("The shopkeeper owes you: $", round(amount_due, 2))