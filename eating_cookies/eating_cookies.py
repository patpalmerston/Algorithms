#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution


def eating_cookies(n, cache={}):
    if n <= 0:
        n = 0
        return n + 1
    if n <= 2:
        return n
    if n not in cache:
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
