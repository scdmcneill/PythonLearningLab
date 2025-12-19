# Last month, Joe Purchased some stock in Acme Software, INC. Here are the details of the purchase:
#   - Number of shares that Joe purchased was 2,000
#   - When Joe purchased the stock, he paid $40.00 per share
#   - Joe paid his stockbroker a commission that amounted to 3 percent of amount he paid for the stock
# Two weeks later, Joe sold the stock. Here are the details of the sale:
#   - The number of shares that Joe sold was 2,000
#   - He sold the stock for $42.75 per share
#   - He paid his stockbroker another commission that amounted to 3 percent of the amount he received for the stock
# Write a program that displays the following information:
#   - amount Joe paid for the stock
#   - amount of commission paid to broker when stock was bought
#   - amount for which Joe sold the stock
#   - amount of commission Joe paid his broker when stock sold
#   - amount of money joe had left when he sold the stock, paid broker (both times). 
#   - If amount positive, he made a profit, if negative, lost money

from os import scandir


PURCHASE_COMMISSION = 0.03
SALE_COMMISSION = 0.03

sharesPurchased = 2000
sharePurchasePrice = 40.00

sharesSold = 2000
shareSellPrice = 42.50

amountPaidForStock = (sharesPurchased * sharePurchasePrice) 
purchaseCommissionPaid = amountPaidForStock * PURCHASE_COMMISSION
totalPurchase = amountPaidForStock + purchaseCommissionPaid

saleAmount = sharesSold * shareSellPrice
saleCommissionPaid = saleAmount * SALE_COMMISSION
totalSale = saleAmount - saleCommissionPaid

print('\n----- Purchase Information -----')
print('Shares Purchased:', sharesPurchased, 'shares')
print('Share Purchase Price: $', format(sharePurchasePrice, '.2f'), sep = '')
print('Stock Purchase Price: $', format(amountPaidForStock, '.2f'), sep = '')
print('Commission Paid: $', format(purchaseCommissionPaid, '.2f'), sep = '')
print('Total Paid: $', format(totalPurchase, '.2f'), sep = '')

print('\n----- Sale Information -----')
print('Shares Sold:', sharesSold, 'shares')
print('Share Sell Price: $', format(shareSellPrice, '.2f'), sep = '')
print('Stock Sale Price: $', format(saleAmount, '.2f'), sep = '')
print('Sale Commission Paid: $', format(saleCommissionPaid, '.2f'), sep = '')
print('Gross Income: $', format(totalSale, '.2f'), sep ='')

profit = totalSale - totalPurchase

if profit >= 0: 
    print('\nProfit: $', format(profit, '.2f'))
else:
    print('\nLoss: $', format(profit, '.2f'))