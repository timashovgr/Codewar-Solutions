#And here is Fibonacci again. This time we want to go one step further. Our fib() function must be faster! Can you do it?
#In case you don't know, what the Fibonacci number is:
#The nth Fibonacci number is defined by the sum of the two previous Fibonacci numbers. In our case: fib(1) := 0 and fib(2) := 1. 
#With these initial values you should be able to calculate each following Fibonacci number.

def fib(n):
    if n == 1:
        return 0
    else:
        a, b = 0, 1
        for i in range(2, n):
            a, b = b, a + b
        return b