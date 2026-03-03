cost = float(input("Enter the cost of the meal: $"))
tip_percentage = float(input("Enter the percentage you would like for the tip: "))

tip_amount = (tip_percentage/100)*cost
print(f"The tip amount is: ${tip_amount}")