'''
Problem 2 - Paying Debt Off in a Year

Now write a program that calculates the minimum fixed monthly payment
needed in order pay off a credit card balance within 12 months.
By a fixed monthly payment, we mean a single number which does not change each month,
but instead is a constant amount that will be paid each month.

In this problem, we will not be dealing with a minimum monthly payment rate.

The following variables contain values as described below:

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

The program should print out one line: the lowest monthly payment that will pay off all debt in under 1 year, for example:

Lowest Payment: 180
'''

# function that calculate remaining amount on the defined monthly payment amount
def minimum_payment(balance,annualInterestRate,monthlyPayment):
    monthlyInterestRate = annualInterestRate/12.0

    for month in range(12):
        balance = balance - monthlyPayment
        balance += monthlyInterestRate * balance

    return balance

loanAmount = float(input("Enter the amount: "))
annualInterestRate = float(input("Enter the anual interest rate: "))
monthlyPayment = 10

# checks whether monthly payment is enough to clear off the loan,
# if not increases the monthly amount by 10
while minimum_payment(loanAmount,annualInterestRate,monthlyPayment) > 0:
    balance = loanAmount
    monthlyPayment += 10
    month = 0

print(monthlyPayment)
