# Write a program that calculates the total amount of a meal purchased at a restaurant.
# The program should ask the user to enter the charge for the food, calculate the 
# amounts of a 18 percent tip, and 7 percent sales tax. Display each of these amounts
# and the total.

mealPrice = float(input('Enter the price of the meal:'))

TIP = 0.18
SALES_TAX = 0.07

tipAmount = mealPrice * TIP
taxAmount = mealPrice * SALES_TAX
totalAmount = mealPrice + tipAmount + taxAmount

print('Meal Price:', mealPrice)
print('Tip: $', format(tipAmount, '.2f'), sep = '')
print('Tax: $', format(taxAmount, '.2f'), sep = '')
print('Total: $', format(totalAmount, '.2f'), sep = '')