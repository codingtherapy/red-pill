# Number spiral diagonals
# Problem 28
#
# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
#
# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13
#
# It can be verified that the sum of the numbers on the diagonals is 101.
#
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?


# 43 44 45 46 47 48 49
# 42 21 22 23 24 25 26
# 41 20 07 08 09 10 27
# 40 19 06 01 02 11 28
# 39 18 05 04 03 12 29
# 38 17 16 15 14 13 30
# 37 36 35 34 33 32 31
#
# 1  2  3  4
# 01 09 25 49 -> (2k-1)**2
# 01 07 21 43 -> (2k-1)**2 - 2*(k-1)
#                 - [0, 2, 4, 6]
# 01 05 17 37 -> (2k-1)**2 - [0, 4, 8, 12]
#                (2k-1)**2 - 4*(k-1)
# 01 03 13 31    (2k-1)**2 - [0, 6, 12, 18]
#                (2k-1)**2 - 6*(k-1)
#
# 1 +
# k = 2,3,4
# (2k-1)^2
# (2k-1)^2 - 2*(k-1)
# (2k-1)^2 - 4*(k-1)
# (2k-1)^2 - 6*(k-1)
#
# 4 * (2*k-1)^2 - (k-1)*(2+4+6)
# 4 * (2*k-1)^2 - 12 * (k-1)
#
#
# sum(1) 1x1 -> 1
# sum(2) 3x3 -> 25
# sum(3) 5x5 -> 101
# sum(4) 7x7 -> 261

def spiral(n):
    if n%2 == 1:
        return 1 + sum([4 * (2*k-1)**2 - 12 * (k-1) for k in range(2,n/2+1)])
    else:
        return -1

if __name__ == '__main__':
    print spiral(1001)
