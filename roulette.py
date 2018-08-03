import random
import os


#print "Please enter a starting amount: $",
def get_arguments():
    stack = float(raw_input("Please enter a starting amount: \t$"))
    starting_bet = float(raw_input("Please enter a starting bet: \t\t$"))
    goal = float(raw_input("Please enter a winnings goal: \t\t$"))
    num_simulations = int(raw_input("Please enter number of simulations:  "))
    return stack, starting_bet, goal, num_simulations



def play_game(stack, starting_bet, goal):
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

    #print 4 % 2
    # get numbers required from user
    stack, starting_bet, goal, num_simulations = get_arguments()
    wins = 0
    losses = 0
    net = 0
    winnings = 0
    losings = 0
    # play game by game
    for num in range(num_simulations):
        result = play_game(stack, starting_bet, goal)
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
        f.write('{},{},{},{},{} \n'.format(stack, starting_bet, goal, num_simulations, net))

    f.close()


