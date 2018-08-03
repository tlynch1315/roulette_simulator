import random
import argparse
import sys

#print "Please enter a starting amount: $",
def get_arguments():
    strategy = raw_input("Please enter a strategy: \t")
    stack = float(raw_input("Please enter a starting amount: \t$"))
    starting_bet = float(raw_input("Please enter a starting bet: \t\t$"))
    goal = float(raw_input("Please enter a winnings goal: \t\t$"))
    num_simulations = int(raw_input("Please enter number of simulations:  "))
    return stack, starting_bet, goal, num_simulations, strategy



def play_martingale(stack, starting_bet, goal):
    '''

    :param stack: starting money stack
    :param starting_bet: the initial bet
    :param goal: end if goal reached
    :return: win or lose (True or False)
    '''
    start = stack
    winnings = 0
    curr_bet = starting_bet
    while stack > 0 and stack > curr_bet and (winnings < goal):
        # simulate the ball landing in 1 of 38 spots
        result = random.randint(1, 38)

        if result > 36:
            stack -= curr_bet
            curr_bet *= 2
        elif result % 2 == 0:
            stack += curr_bet
            winnings += starting_bet
            curr_bet = starting_bet
        else:
            stack -= curr_bet
            curr_bet *= 2


    if stack > curr_bet:
        return winnings
    else:
        return start - stack


if __name__ == "__main__":
    # get arguments from command line
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--strategy', type=str)
    parser.add_argument('-sb', '--starting_bet', type=float)
    parser.add_argument('-a', '--starting_amount', type=float)
    parser.add_argument('-g', '--goal', type=float)
    parser.add_argument('-n', '--num_simulations', type=int)

    # if arguments not provided on command line request them
    args = parser.parse_args()
    if len(sys.argv) < 5:
        stack, starting_bet, goal, num_simulations = get_arguments()
    else:
        stack = args.starting_amount
        starting_bet = args.starting_bet
        goal = args.goal
        num_simulations = args.num_simulations
        strategy = args.strategy


    wins = 0
    losses = 0
    net = 0
    winnings = 0
    losings = 0
    # play game by game
    for num in range(num_simulations):
        result = play_martingale(stack, starting_bet, goal)
        if result == goal:
            net += goal
            winnings += goal
            wins += 1
        else:
            net -= result
            losings += result
            losses += 1


    print "\nRESULTS:"
    print "Number of Wins: \t{}".format(wins)
    print "Number of Losses: \t{}".format(losses)
    print "Win percentage: \t{}%".format(float(wins)/float(num_simulations)*100)
    print "Profit: \t\t\t${0:.2f}".format(winnings)
    print "Losses: \t\t\t${0:.2f}".format(losings)
    print "Net winnings: \t\t${0:.2f}".format(net)

    with open('results.csv', 'a') as f:
        f.write('{},{},{},{},{}\n'.format(stack, starting_bet, goal, num_simulations, net))

    f.close()


