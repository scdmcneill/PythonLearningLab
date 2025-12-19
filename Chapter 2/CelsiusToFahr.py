# Write a program that converts Celsius temperatures to Fahrenheit temperatures. The formula is as follows:
# F = 9/5(C + 32)
# The program should ask the user to enter a temperature in Celsius, then display the temperature converted
# to Fahrenheit

def convertToFahr(celsius) :
    fahr = (9/5) * celsius + 32
    return format(fahr, '.2f')

celsiusTemp = float(input('Enter the temperature in Celsius to convert to Fahrenheit: '))

print('Temperature in Fahrenheit:', convertToFahr(celsiusTemp))