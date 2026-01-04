# Write a program that asks the user for the speed of a vehicle (in miles per hour) and the number of hours it has travelled.
# It should then use a loop to display the distance the vehicle has traveled for each hour of that time period.

speed = float(input('Enter the speed of the vehicle '))

timeTravelled = int(input('Enter the amount of time the vehicle is traveling for '))

for hour in range(1, timeTravelled + 1, 1):
    distance = hour * speed
    print('Hour', hour, ' | ','Distance Travelled:', distance)