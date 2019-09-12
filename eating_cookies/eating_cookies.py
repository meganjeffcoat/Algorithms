#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution

# n-1, n-2, n-3 n= num of cookies
# cookie = [0] * (n + 1)
# cookie[0] = 1
# cookie[1] = 1
# cookie[2] = 2

# for i in range(3, n + 1):
#     cookie[i] = cookie[i - 1] + cookie[i - 2] + cookie[i - 3]
# return cookie[n]


def eating_cookies(n, cache=None):
    # set up number of cookies at a time
    if (n == 1 or n == 0):
        return 1
    elif (n == 2):
        return 2
    else:
        return eating_cookies(n - 3) + eating_cookies(n - 2) + eating_cookies(n - 1)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
