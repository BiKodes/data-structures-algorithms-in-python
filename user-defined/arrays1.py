#storing prices & retrieving specific days pprices:

stock_prices = [235, 354, 301, 272]

#day one price
stock_prices[0] 

#day three price
stock_prices[2] 

#the day price was 301:

for i in range(len(stock_prices)):
    if stock_prices[i] == 301:
        return i

#print all prices:

for price in stock_prices:
    print(price)

#insert new price 568 at index 1:

stock_prices.insert(1, 284)

#delete element:
stock_prices.remove(stock_prices[1])