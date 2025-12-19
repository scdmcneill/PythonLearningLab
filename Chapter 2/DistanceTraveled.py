# Assuming there are not accidents or delays, the distance that a car travels down the interstate can be calculated
# with the following formula: d = s * t. A car is travelling at 70 miles per hour. Write a program that displays the following:
#   - The distance a car will travel in 6 hours
#   - The distance a car will travel in 10 hours
#   - The distance a car will travel in 15 hours

speed = 70 # miles/hour

def distanceCalculator(speed, time) :
    DISTANCE = speed * time
    return DISTANCE

print('The car will travel', distanceCalculator(speed, 6), 'miles.')
print('The car will travel', distanceCalculator(speed, 10), 'miles.')
print('The car will travel', distanceCalculator(speed, 15), 'miles.')