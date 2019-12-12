#!/usr/bin/python

import sys

def rock_paper_scissors(n):
    if n == 0:
        return [[]]
#current results list
    curr_results = []
#n is equivalent to the rounds/players in the game
    rounds = [0]*n
# call the function that takes in the number of rounds, its index and the current results
    play_game(rounds, 0, curr_results) 
    return curr_results

def play_game(rounds_played, played_index, curr):
    # a list of possible choices
    possibilites = ['rock', 'paper', 'scissors']
    # if our played index is equal to the length of rounds to be played then send the result to our current list.
    if played_index == len(rounds_played):
        curr.append(list(rounds_played))
        return rounds_played
    
    # loop through the list of possibilites
    for item in possibilites:
      #every iteration need to be equal to the round being played, and at what index
        rounds_played[played_index] = item
        #add to the index for recursive call executed from the value of n 
        play_game(rounds_played, played_index + 1, curr)
       

print(rock_paper_scissors(2))


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')