# Get desired future value
futureValue  = float(input('Enter the desired future value: '))

# Get annual interest rate
interestRate = float(input('Enter the annual interest rate: ')) / 100

# Get number of years
years = int(input('Enter the number of years the money will grow: '))

# Calculate amount needed to deposit
presentValue = futureValue / (1 + interestRate) ** years

# Display amount needed to deposit
print('You will need to deposit: $', format(presentValue, ',.2f'), sep = '')