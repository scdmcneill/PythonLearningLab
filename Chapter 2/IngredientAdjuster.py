# A cookie recipe calls for the following ingredients:
#   - 1.5 cups of sugar
#   - 1 cup of butter
#   - 2.75 cups of flour
# The recipe produces 48 cookies with this amount of ingredients. Write a program that asks the user
# how many cookies he or she wants to make, then displays the number of cups of each ingredient needed.

#Recipe
CUPS_SUGAR = 1.5
CUPS_BUTTER = 1
CUPS_FLOUR = 2.75
MAKES = 48

cookieCount = float(input('Enter the number of cookies you would like to make: '))

sugarNeeded = (CUPS_SUGAR * cookieCount) / MAKES
butterNeeded = (CUPS_BUTTER * cookieCount) / MAKES
flourNeeded = (CUPS_FLOUR * cookieCount) / MAKES

print('Cups of Sugar Needed:', format(sugarNeeded, '.2f'))
print('Cups of Butter Needed:', format(butterNeeded, '.2f'))
print('Cups of Flour Needed:', format(flourNeeded, '.2f'))
