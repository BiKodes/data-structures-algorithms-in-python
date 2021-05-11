#stock price are imported from a cdv file:

stock_prices = []
with open("stock_prices.csv", "r") as f:
    for line in f:
        tokens = line.split(',')
        day = tokens[0]
        price = float(tokens[1])
        stock_prices.append([day,price])

print(stock_prices)

# getting specific stock prices on specific days:

for element in stock_prices:
    if element[0] == 'Jan 9':
        print(element[1])

# processing using the dictionary

stock_prices = {}
with open("stock_prices.csv", "r") as f:
    for line in f:
        tokens = line.split(',')
        day = tokens[0]
        price = float(tokens[1])
        stock_prices.append[day] = price


#getting keys & values

print(stock_prices)

#getting specific values:

print(stock_prices['Jan 9'])

#Dictionaries use Hash-Tables.Hash Table implimentation:

class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr(h)

    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] =None


t = HashTable()
t['Jan 6'] = 130
t['Jan 7'] = 340

print(t.arr)
print(t['Jan 7'])
