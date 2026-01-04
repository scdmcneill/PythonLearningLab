# Write a program that keeps a running total of the number of bugs collected during the five days.
# The loop should ask for the number of bugs collected for each day, and when the loop is finished,
# the program should display the total number of bugs collected.

totalBugsCollected = 0

for day in range(0, 5):
    bugsCollected = int(input('Enter the number of bugs collected:'))
    totalBugsCollected += bugsCollected

print('Total Bugs Collected:', totalBugsCollected)