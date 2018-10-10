'''
Problem 3 - Using Bisection Search to Make the Program Faster

You'll notice that in Problem 2, your monthly payment had to be a multiple of $10. Why did we make it that way?
You can try running your code locally so that the payment can be any dollar and cent amount (in other words,
the monthly payment is a multiple of $0.01). Does your code still work?
It should, but you may notice that your code runs more slowly, especially in cases with very large balances and
interest rates.

Well then, how can we calculate a more accurate fixed monthly payment than we did in Problem 2 without
running into the problem of slow code? We can make this program run faster using a technique introduced in
lecture - bisection search!

The following variables contain values as described below:

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

To recap the problem: we are searching for the smallest monthly payment such that we can pay off the
entire balance within a year. What is a reasonable lower bound for this payment value? $0 is the obvious anwer,
but you can do better than that. If there was no interest, the debt can be paid off by monthly payments of one-twelfth of
the original balance, so we must pay at least this much every month. One-twelfth of the original balance is a good lower bound.

What is a good upper bound? Imagine that instead of paying monthly, we paid off the entire balance at the end of the year.
What we ultimately pay must be greater than what we would've paid in monthly installments,
because the interest was compounded on the balance we didn't pay off each month.
So a good upper bound for the monthly payment would be one-twelfth of the balance,
after having its interest compounded monthly for an entire year.

In short:

Monthly interest rate = (Annual interest rate) / 12.0
Monthly payment lower bound = Balance / 12
Monthly payment upper bound = (Balance x (1 + Monthly interest rate)12) / 12.0

Write a program that uses these bounds and bisection search
to find the smallest monthly payment to the cent (no more multiples of $10) such that we can pay off the debt within a year.
'''

def minimum_payment(balance,annualInterestRate,monthlyInterestRate,minPay):
    for month in range(12):
        balance = balance - minPay
        balance += monthlyInterestRate * balance
    return balance

loanAmount = float(input("Enter the amount: "))
annualInterestRate = float(input("Enter the annual interest rate: "))
IntialLoanAmount = loanAmount
epsilon = 0.03

monthlyInterestRate = annualInterestRate/12.0
lowerBound = loanAmount/12.0
upperBound = (loanAmount * ((1.0 + monthlyInterestRate)**12))/12.0


# Bisection Search loop
while abs(loanAmount) > epsilon:
    minPay = (lowerBound + upperBound)/2
    loanAmount = IntialLoanAmount
    loanAmount = minimum_payment(loanAmount,annualInterestRate,monthlyInterestRate,minPay)
    if loanAmount > epsilon:
        lowerBound = minPay
    elif loanAmount < -epsilon:
        upperBound = minPay
    else:
        break

print("Minimum amount to be payed: ",round(minPay,2))
