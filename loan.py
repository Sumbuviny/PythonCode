amount = float(input("Loan amount: ")) # Enter loan amount
annualInterestRate = float(input("Annual Interest rate: ")) # Enter annual interest rate
numberOfYears = int(input("Number of Years:")) # Enter number of years
monthlyInterestRate = annualInterestRate / 1200 # obtain monthly interest rate
# calculate Monthly Payment
monthlyPayment = amount * monthlyInterestRate / (1 - 1 / pow (1 + monthlyInterestRate, numberOfYears * 12))
# calculate Total Payment
totalPayment = monthlyPayment * numberOfYears * 12
# print results
print("The monthly payment is R", round(monthlyPayment,2))
print("The total payment is R", round(totalPayment,2))

