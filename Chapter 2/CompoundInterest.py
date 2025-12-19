# When a bank account pays compound interest, it pays interest not only on the principle amount that was desposited into
# the account, but also on the interest that has accumulated over time. Suppose you want to deposit some money into a savings
# account, and let the account earn compound interest for a certain number of years. The formula for calculating the balance
# of the account after a specified number of years is:
# A = P (1 + (r/n)**(n*t))
#   - P = principal amount
#   - r = annual interest rate
#   - n = number of times per year interest compounded
#   - t = number of years
# Write a program that makes the calculation for you. The program should ask the user to input the following:
#   - Amount of principal originally deposited
#   - Annual interest Rate
#   - Compound Rate
#   - Number of years account will be left to earn interest
# Once input data has been entered, program should calculate and display the amount of money that will be in the account
# after the specified number of years

principalAmount = float(input('Enter the Principal Amount: $'))
annualInterestRate = float(input('Enter the annual interest rate as a percent:')) / 100
compoundRate = float(input('Enter the amount of times interest is compounded each year:'))
time = int(input('Enter the number of years the money will be in the account: '))

amount = (principalAmount * (1 + (annualInterestRate/compoundRate)) ** (compoundRate * time))

print('Amount of money in account after', time, 'years: $', format(amount, '.2f'))