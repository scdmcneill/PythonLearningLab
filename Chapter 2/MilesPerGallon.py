# A car's miles-per-gallon (MPG) can be calculated with the following formula: MPG = miles driven / gallon of gas used
# Write a program that asks the user for the number of miles driven and the gallons of gas used.
# It should calculate the car's MPG and display the result

milesDriven = float(input('Enter the amount of miles driven: '))
gallonsUsed = float(input('Enter the gallons of gas used: '))

mpg = milesDriven / gallonsUsed

print('MPG:', format(mpg, '.2f'))