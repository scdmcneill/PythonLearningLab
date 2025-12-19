# Write a program that will ask the user to enter the amount of a purchase. The program should then compute the state 
# and county sales tax. Assume the state sales tax is 5 percent, county sales tax is 2.5 percent. The program 
# should display the amount of the purchase, state sales tax, county sales tax, and total sales tax, and total of sale

STATE_TAX = 0.05
COUNTY_TAX = 0.025

purchaseAmount = float(input('Enter the amount of a purchase: '))

stateTax = purchaseAmount * STATE_TAX
countyTax = purchaseAmount * COUNTY_TAX
totalTax = stateTax + countyTax

totalAmount = purchaseAmount + totalTax

print('Purchase Amount: $', format(purchaseAmount, '.2f'), sep ='')
print('State Tax: $', format(stateTax, '.2f'), sep = '')
print('County Tax: $', format(countyTax, '.2f'), sep = '')
print('Total Tax: $', format(totalTax, '.2f'), sep = '')

print('\nTotal: $', format(totalAmount, '.2f'), sep ='')

