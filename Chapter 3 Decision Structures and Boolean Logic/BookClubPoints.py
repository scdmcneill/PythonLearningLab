# Write a program that asks the user to enter the number of books that he or she has purchased this month,
# then display the number of points awarded.

booksPurchased = int(input('Enter the number of books purchased this month:'))

if booksPurchased < 2:
    bookClubPoints = 0
elif booksPurchased < 4:
    bookClubPoints = 5
elif booksPurchased < 6:
    bookClubPoints = 15
elif booksPurchased < 8:
    bookClubPoints = 30
else:
    bookClubPoints = 60

print('Number of points earned this month:', bookClubPoints)