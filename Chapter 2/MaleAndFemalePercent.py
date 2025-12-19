# Write a program that asks the user for the numbver of males and the number of females in a registered class
# The program should display the percentage of males and females in a class.

numberFemales = int(input('Enter the number of females in the class: '))
numberMales = int(input('Enter the number of males in the class: '))

totalStudents = numberFemales + numberMales

percentFemale = (numberFemales / totalStudents) * 100
percentMale = (numberMales / totalStudents) * 100

print('Percent Female Students: ', format(percentFemale, '.2f'), '%')
print('Percent Male Students: ', format(percentMale, '.2f'), '%')