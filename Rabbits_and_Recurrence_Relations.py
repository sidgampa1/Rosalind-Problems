import sys

'''
This script takes 2 numbers n,k as command line args

It calculates the nth fibonacci number, modified by a factor of k each iteration
'''

n = (int)(sys.argv[1])
k = (int)(sys.argv[2])

current = 1 ## start with first two numbers of fibonacci (n = 1)
prev = 0 ## n = 0

counter = 2 ## current generation term (n = 2)
while (counter < n):
    if (current == 1):
        prev = current
        current += (current * k)
    else:
        temp = current
        current += (prev * k)
        prev = temp

    counter += 1

print(current)
