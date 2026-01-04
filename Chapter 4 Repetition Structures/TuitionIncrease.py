# At one college, the tuition for a full-time student is $8,000 per semester. It has been announced that the tuition 
# will increase by 3 percent each year for the next 5 years. Write a program with a loop that displays the projected 
# semester tuition amount for the next 5 years.

tuition = 8000
tuitionIncrease = 0.03
years = 5

for year in range(1, years + 1, 1):
    tuition = tuition + (tuition * tuitionIncrease)
    print('Year', year)
    print('Tuition: $', format(tuition, '.2f'))