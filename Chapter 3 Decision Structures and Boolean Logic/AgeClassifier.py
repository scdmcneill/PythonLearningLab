# Write a program that asks the suer to enter a person's age. The program should display a message indicating
# whether the person is an infant, a child, a teenager, or an adult.
#   - If 1 year or less, infant
#   - If 1 year+ but < 13 years, child
#   - > 13 years, < 20 years, teenager
#   - < 20, adult

age = float(input('Enter the age of the person to classify:'))


if age < 1:
    ageClass = 'Infant'
elif age >= 1 and age < 13:
    ageClass = 'Child'
elif age >= 13 and age <= 20:
    ageClass = 'Teenager'
else:
    ageClass = 'Adult'


print('The person you entered is a', ageClass)