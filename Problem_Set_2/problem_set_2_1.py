'''
Problem 1 - Paying Debt off in a Year

Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment
required by the credit card company each month.

The following variables contain values as described below:

balance - the outstanding balance on the credit card
annualInterestRate - annual interest rate as a decimal
monthlyPaymentRate - minimum monthly payment rate as a decimal

For each month, calculate statements on the monthly payment and remaining balance. At the end of 12 months,
print out the remaining balance. Be sure to print out no more than two decimal digits of accuracy - so print

Remaining balance: 813.41

instead of

Remaining balance: 813.4141998135

So your program only prints out one thing: the remaining balance at the end of the year in the format:

Remaining balance: 4784.0
'''
#function to calculate credit card balance at the end of the year
def balance_calculator(balance, annualInterestRate, monthlyPaymentRate):
    monthlyInterestRate = annualInterestRate/12.0

    for month in range(12):
        monthlyPayment = monthlyPaymentRate * balance
        balance = balance - monthlyPayment
        balance += monthlyInterestRate * balance

    return balance

loanAmount = float(input("Enter the amount: "))
annualInterestRate = float(input("Enter the anual interest rate: "))
monthlyPaymentRate = float(input("Enter the monthly payment rate: "))

remainingAmount = round(balance_calculator(loanAmount,annualInterestRate,monthlyPaymentRate),2)

print("Remaining amount at year end:",remainingAmount)
