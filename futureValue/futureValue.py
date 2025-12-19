futureValue = float(input('Enter the desired future value: '))

# Get annual interest rate
interestRate = float(input('Enter the annual interest rate: '))

# Get number of years money will appreciate
years = int(input('Enter the number of years the money will grow'))

# Calculate the amount needed to deposit today
presentValue = futureValue / (1 + interestRate) ** years

# Display the amount needed to deposit today
print('You need to deposit: $', format(presentValue, ',.2f'))
