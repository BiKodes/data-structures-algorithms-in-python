#uses FIFO principle.

nse_stock_prices_queue = []

nse_stock_prices_queue.insert(0, 131.0)
nse_stock_prices_queue.insert(0, 125.5)
nse_stock_prices_queue.insert(0, 145.0)

nse_stock_prices_queue

nse_stock_prices_queue.pop()


#using collection.deque as a queue:
from collections import deque

q = deque()

q.appendleft(5)
q.appendleft(10)
q.appendleft(27)

q

q.pop()

# queue class using collections.deque:

from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)

pq =  Queue()

pq.enqueue({
    'company': 'Ad Astra Tech',
    'timestamp': '05 Jan, 7.05 AM',
    'price': 135.52
})

pq.enqueue({
    'company': 'Ad Astra Tech',
    'timestamp': '05 Jan, 7.06 AM',
    'price': 132.07
})

pq.enqueue({
    'company': 'Ad Astra Tech',
    'timestamp': '05 Jan, 7.07 AM',
    'price': 140.26
})
