#Any problem that can be divided into further small and simpler problem can be solved using a recursion.
#Divide big problem into small and simple problems
#Find a base condition with simple answer
#Return or roll back answer for base condition to solve all sub problems

def find_sum(n):
    if n == 1:
        return 1
    return n + find_sum(n-1)

def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n - 1) + fib(n - 2)

if __name__ == '__main__':
    print(find_sum(6))
    print(fib(6))