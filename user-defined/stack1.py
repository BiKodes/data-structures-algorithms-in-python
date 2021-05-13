#LIFO(Last In First Out)
#Lis as stack:

s = []

s.append('https://v3.vuejs.org/guide/introduction.html')
s.append('https://v3.vuejs.org/style-guide/')
s.append('https://v3.vuejs.org/cookbook/')
s.append('https://v3.vuejs.org/examples/markdown.html')

#getting last element from the list:
s[-1]

#removing elements from stack list
s.pop()
    'https://v3.vuejs.org/examples/markdown.html'
s.pop()
    'https://v3.vuejs.org/examples/markdown.html'
s.pop()
    'https://v3.vuejs.org/style-guide/'
s.pop()
    'https://v3.vuejs.org/guide/introduction.html'


# using deque as a stack:
from collections import deque

stack = deque()

stack.append('https://readthedocs.org/')


#implementing stack class using deque:

class Stack:
    def __init__(self):
        self.container = deque()

    def pop(self):
        return self.container.pop()

    def peek(self():
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

s = Stack()

s.peek()

s

s.peek()

s.pop()

s.is_empty()

s.push(30)