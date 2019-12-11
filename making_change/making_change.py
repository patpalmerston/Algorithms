#!/usr/bin/python

import sys


def making_change(amount, denominations):
    #create a cache list that starts with an index value of 1 and auto generates index values of 0 equal to the length of the amount parameter
    ways = [1] + [0]*amount
    #iterate through denominations list looking at each coin value
    for coin in denominations:
        #iterate through the the length of the amount parameter and compare each coin that fits within every iteration to the length of amount incrementing amount for every iteration.
        for i in range(coin, amount+1):
            #define the index value of ways as each iteration of amount subtracting the times coin fits with range index.
            ways[i] += ways[i-coin]
            #return the result from subtracting coin against the index length of amount
    return ways[amount]


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print("There are {ways} ways to make {amount} cents.".format(
            ways=making_change(amount, denominations), amount=amount))
    else:
        print("Usage: making_change.py [amount]")
