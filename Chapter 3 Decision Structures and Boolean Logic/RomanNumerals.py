# Write a program that prompts the user to enter a numebr within the range of 1 through 10.
# The program should display the Roman numeral version of that number. If the number is outside
# of the range of 1 through 10, the program should display an error message.

userNumber = int(input('Enter a number between 1 and 10 to cast to a Roman Numeral: '))

if userNumber == 1:
    romanNumeral = 'I'
elif userNumber == 2:
    romanNumeral = 'II'
elif userNumber == 3:
    romanNumeral = 'III'
elif userNumber == 4:
    romanNumeral = 'IV'
elif userNumber == 5:
    romanNumeral = 'V'
elif userNumber == 6:
    romanNumeral = 'VI'
elif userNumber == 7:
    romanNumeral = 'VII'
elif userNumber == 8:
    romanNumeral = 'VIII'
elif userNumber == 9:
    romanNumeral = 'IX'
elif userNumber == 10:
    romanNumeral = 'X'
else:
    print('Error: Please enter a number between 1 and 10')

print('Number Entered:', userNumber)
print('Roman Numeral:', romanNumeral)
