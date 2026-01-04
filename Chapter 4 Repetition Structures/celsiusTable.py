# Write a program that displays a table of the Celsius temperatures 0 through 20 and their Fahrenheit equivalents. 
# The formula for converting a temperature from Celsius to Fahrenheit is where F is the Fahrenheit temperature, 
# and C is the Celsius temperature. Your program must use a loop to display the table.

def convertToFahr(celsius):
    fahrenheit = (9/5) * celsius + 32
    return fahrenheit

rowCount = 20

for degree in range(0, rowCount + 1, 1):
    print('Celsius Temperature:', degree, 'Fahrenheit Temperature:', convertToFahr(degree) )