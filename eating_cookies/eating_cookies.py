#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution


def eating_cookies(n, cache={}):
    #base case looking for less than zero or less equal or less than 2
    if n <= 0:
        n = 0
        return n + 1
    if n <= 2:
        return n
        # if the key of n is not in the dictionary 
    if n not in cache:
        # then n as a key of cache will be equal to the recursive calls adding each recursive iteration onto itself
        cache[n] = eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)
    return cache[n]

    # This works for the first test, but need the cache for the big tests
    # if n <= 0:
    #     n = 0
    #     return n + 1
    # if n <= 2:
    #     return n
    # else:
    #     n = eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)
    # return n


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
