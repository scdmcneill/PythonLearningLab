# Write a program that asks the user to enter a pocket number and displays whether the pocket is green,
# red or black. The program should display an error message is the user enter a number that is outside the 
# range of 0 through 36

pocketNumber = int(input('Enter a pocket number to display the pocket color:'))

if pocketNumber == 0:
    pocketColor = 'Green'
elif pocketNumber > 0 and pocketNumber <= 10:
    pocketColor = 'Black'
elif pocketNumber >= 11 and pocketNumber <= 18:
    pocketColor = 'Red'
elif pocketNumber >= 19 and pocketNumber <= 28:
    pocketColor = 'Black'
elif pocketNumber >= 29 and pocketNumber <= 36:
    pocketColor = 'Red'
else:
    print('Error: Number is outside of range 0-36')

print('The pocket color is:', pocketColor)