# Create a change-counting game that gets the user to enter the number of coins required to make exactly one dollar.
# The program should prompt the user to enter the number of pennies, nickels, dimes, and quarters. If the total
# value of the coins entered is eual to a dollar, the program should congratulate the user for winning the game.
# Otherwise, the program should display a message indicating whether the amount entered was more or less than one dollar.

PENNY_VALUE = 1
NICKEL_VALUE = 5
DIME_VALUE = 10
QUARTER_VALUE = 25

pennyCount = int(input('Enter the number of pennies:'))
nickelCount = int(input('Enter the number of nickels:'))
dimeCount = int(input('Enter the number of dimes:'))
quarterCount = int(input('Enter the number of quarters:'))

pennySum = pennyCount * PENNY_VALUE
nickelSum = nickelCount * NICKEL_VALUE
dimeSum = dimeCount * DIME_VALUE
quarterSum = quarterCount * QUARTER_VALUE

totalSum = pennySum + nickelSum + dimeSum + quarterSum

if totalSum == 100:
    print('You Win!')
elif totalSum > 100:
    print('You lose. Try again!')
    print('Your total sum was:', totalSum)
elif totalSum < 100:
    print('You lose. Try again!')
    print('Your total sum was:', totalSum)