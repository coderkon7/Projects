Invoice = input("Please enter your subtotal for the bill, I will calculate the tax: ")
TaxRate = input("Thank you for that amount. Now, please enter the tax rate percentage of your province: ")
TaxAmount = float(Invoice) * float(TaxRate) / 100
Payment = float(Invoice) + float(TaxAmount)
print("Here is the amount of tax that will be added to your bill", TaxAmount) 
print("Here is the total amount of your payment", Payment)
