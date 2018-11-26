import random
import argparse
import sys


# print "Please enter a starting amount: $",
def get_arguments():
    strategy = raw_input("Please enter a strategy: \t\t\t ")
    stack = float(raw_input("Please enter a starting amount: \t$"))
    starting_bet = float(raw_input("Please enter a starting bet: \t\t$"))
    goal = float(raw_input("Please enter a winnings goal: \t\t$"))
    num_simulations = int(raw_input("Please enter number of simulations:  "))
    return stack, starting_bet, goal, num_simulations, strategy


# simulate game using martingale strategy
def play_martingale(stack, starting_bet, goal):
    '''

    :param stack: starting money stack
    :param starting_bet: the initial bet
    :param goal: end if goal reached
    :return: amount won or lost, number of turns
    '''
    turns = 0
    start = stack
    winnings = 0
    curr_bet = starting_bet
    while stack > 0 and stack > curr_bet and (winnings < goal):
        # simulate the ball landing in 1 of 38 spots
        turns += 1
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
        return winnings, turns, True
    else:
        return start - stack, turns, False


# gives fibonacci number of index n
def F(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return F(n - 1) + F(n - 2)


# simulate game with fibonacci approach
def play_fibonacci(stack, starting_bet, goal):
    turns = 0
    start = stack
    winnings = 0
    curr_index = 1
    curr_bet = F(curr_index)
    while stack > 0 and stack > curr_bet and (stack - start) < goal:
        turns += 1
        result = random.randint(1, 38)
        if result > 36:
            stack -= curr_bet
            curr_index += 1
        elif result % 2 == 0:
            stack += curr_bet
            if curr_index - 2 > 0:
                curr_index -= 2
            else:
                curr_index = 1
        else:
            stack -= curr_bet
            curr_index += 1
        curr_bet = F(curr_index)

    if stack > start:
        return stack - start, turns, True
    else:
        return start - stack, turns, False


# simulate game with paroli approach
def play_paroli(stack, starting_bet, goal, num_wins):
    turns = 0
    start = stack
    curr_bet = starting_bet
    streak = 0
    while stack > 0 and curr_bet <= stack and (stack - start) < goal:
        turns += 1
        result = random.randint(1, 38)
        if result > 36:
            stack -= curr_bet
            curr_bet = starting_bet
            streak = 0
        elif result % 2 == 0:
            stack += curr_bet
            streak += 1
            if streak == num_wins:
                curr_bet = starting_bet
                streak = 0
            else:
                curr_bet *= 2
        else:
            stack -= curr_bet
            curr_bet = starting_bet
            streak = 0

    if stack > start:
        return stack - start, turns, True
    else:
        return start - stack, turns, False

# simulate game with alembert approach
def play_alembert(stack, starting_bet, goal):
    turns = 0
    start = stack
    curr_bet = starting_bet
    while stack > 0 and stack >= curr_bet and (stack - start) < goal:
        turns += 1
        result = random.randint(1, 38)
        if result > 36:
            stack -= curr_bet
            curr_bet += starting_bet
        elif result % 2 == 0:
            stack += curr_bet
            if curr_bet != starting_bet:
                curr_bet -= starting_bet
        else:
            stack -= curr_bet
            curr_bet += starting_bet

    if stack > start:
        return stack - start, turns, True
    else:
        return start - stack, turns, False




if __name__ == "__main__":
    # get arguments from command line
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--strategy', type=str)
    parser.add_argument('-sb', '--starting_bet', type=float)
    parser.add_argument('-a', '--starting_amount', type=float)
    parser.add_argument('-g', '--goal', type=float)
    parser.add_argument('-n', '--num_simulations', type=int)
    parser.add_argument('-ws', '--num_wins', type=int)

    # if arguments not provided on command line request them
    args = parser.parse_args()
    num_wins = 0
    if len(sys.argv) < 5:
        stack, starting_bet, goal, num_simulations, strategy = get_arguments()
    else:
        stack = args.starting_amount
        starting_bet = args.starting_bet
        goal = args.goal
        num_simulations = args.num_simulations
        strategy = args.strategy
        num_wins = args.num_wins

    if strategy == 'paroli' and num_wins == 0:
        num_wins = int(raw_input("How many wins before cashing out: \t "))

    wins = 0
    losses = 0
    net = 0
    winnings = 0
    losings = 0
    total_turns = 0

    # play game by game
    for num in range(num_simulations):
        if strategy == 'martingale':
            result, game_length, decision = play_martingale(stack, starting_bet, goal)
        elif strategy == 'fibonacci':
            result, game_length, decision = play_fibonacci(stack, starting_bet, goal)
        elif strategy == 'paroli':
            result, game_length, decision = play_paroli(stack, starting_bet, goal, num_wins)
        elif strategy == 'alembert':
            result, game_length, decision = play_alembert(stack, starting_bet, goal)

        total_turns += game_length

        if decision == True:
            net += goal
            winnings += goal
            wins += 1
        else:
            net -= result
            losings += result
            losses += 1

    average_turns = float(total_turns) / float(num_simulations)
    average_winnings = net/num_simulations

    print "\nRESULTS:"
    print "Number of Wins: \t{}".format(wins)
    print "Number of Losses: \t{}".format(losses)
    print "Win percentage: \t{0:.2f}%".format(float(wins) / float(num_simulations) * 100)
    print "Profit: \t\t\t${0:.2f}".format(winnings)
    print "Losses: \t\t\t${0:.2f}".format(losings)
    print "Net winnings: \t\t${0:.2f}".format(net)
    print "Average Winnings: \t\t${0:.2f}".format(average_winnings)

    if strategy == 'martingale':
        with open('martingale.csv', 'a') as f:
            f.write('{},{},{},{},{}, {}\n'.format(stack, starting_bet, goal, num_simulations, net, average_winnings))
    elif strategy == 'fibonacci':
        with open('fibonacci.csv', 'a') as f:
            f.write('{},1,{},{},{},{}\n'.format(stack, goal, num_simulations, net, average_winnings))
    elif strategy == 'paroli':
        with open('paroli.csv', 'a') as f:
            f.write('{},{},{},{},{},{},{}\n'.format(stack, starting_bet, goal, num_simulations, net, num_wins, average_winnings))
    elif strategy == 'alembert':
        with open('alembert.csv', 'a') as f:
            f.write('{},{},{},{},{},{}\n'.format(stack, starting_bet, goal, num_simulations, net, average_winnings))


    f.close()
