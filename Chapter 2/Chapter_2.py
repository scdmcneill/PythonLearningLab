# Chapter 2 - Input, Processing, and Output
print('Hello world!')

#variables
age = 25
print(age, ' you are old...')

#reading input from keyboard
name = input('What is your name? ')
print('Nice to meet you,', name)

#reading numbers with the input function
hours = int(input('How many hours did you work this week? '))
print('You worked', hours, 'hours this week.')

payRate = float(input('What is your hourly pay rate? '))

grossPay = hours * payRate
print('Your gross pay is: $', grossPay)

# Performing calculations
surgePay = grossPay * 0.2
print('Your surge pay is: $', surgePay)
totalPay = grossPay + surgePay 
print('Your total pay is: $', totalPay)

surgeHourlyRate = totalPay / hours
print('Your surge hourly rate is: $', surgeHourlyRate)