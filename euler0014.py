# Longest Collatz sequence
# Problem 14
#
# The following iterative sequence is defined for the set of positive integers:
#
# n -> n/2 (n is even)
# n -> 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
# 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
#
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
# Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.

# def collatz(n):
#     if n==1:
#         return [1]
#     elif n==2:
#         return [2, 1]
#     else:
#         if n%2 == 0:
#             c = collatz(n/2)
#             c.insert(0,n)
#         else:
#             c = collatz(3*n + 1)
#             c.insert(0,n)
#         return c
#
#
# print collatz(1)
# print collatz(2)
# print collatz(4)
# print collatz(5)
# print collatz(1000000)
#
#
# lengths = {1: 0, 2: 1}
#
# def length(n):
#     if n in lengths:
#         return lengths[n]
#     else:
#         if n%2 == 0:
#             lengths[n] = length(n/2) + 1
#         else:
#             lengths[n] = length(3*n + 1) + 1
#         return lengths[n]


lengths = {1: 0, 2: 1}

def length(n):
    if n in lengths:
        return lengths[n]
    else:
        if n%2 == 0:
            lengths[n] = length(n/2) + 1
        else:
            lengths[n] = length(3*n + 1) + 1
        return lengths[n]


for n in range(1,1000001):
    if n%2 == 0:
        lengths[n] = length(n/2) + 1
    else:
        lengths[n] = length(3*n + 1) + 1
maxv = 0
for k, v in lengths.items():
    if v >= maxv:
        maxk = k
        maxv = v
print maxk, maxv

def collatz(n):
    if n==1:
        return [1]
    elif n==2:
        return [2, 1]
    else:
        if n%2 == 0:
            c = collatz(n/2)
            c.insert(0,n)
        else:
            c = collatz(3*n + 1)
            c.insert(0,n)
        return c
#maxv = 524
print collatz(837799)
