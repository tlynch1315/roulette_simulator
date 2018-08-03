import os
import sys
import numpy as np

stacks = np.arange(50, 500, 50)
starting_bets = np.arange(50, 500, 50)
goals = np.arange(50, 500, 50)

for stack in stacks:
    for starting_bet in starting_bets:
        for goal in goals:
            os.system('python roulette.py -s martingale -sb {} -a {} -g {} -n 500'.format(starting_bet, stack, goal))
