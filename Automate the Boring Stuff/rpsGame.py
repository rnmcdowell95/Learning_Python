# Creating a rock paper scisccors game for practice
# Testing my own implementation and then comparing to the source doe provided.

import random, sys

print('ROCK, PAPER, SCISSORS')
print()

# Initializes the variables to track wins, losses, and ties

wins = 0
losses = 0
ties = 0

# Loop runs into player indidicaties they would like to quick.
while True:

    # Displaying the wins, losses, and ties
    print(str(wins) + ' Wins, ' + str(losses) + ' Losses, ' + str(ties) + ' Ties')

    # Sets computerChoice to a random int 1 - 3 to correspond to one of the three options.
    computerChoice = random.randint(1, 3)

    # If computerChoice equals 1 it is set to ROCK.
    if computerChoice == 1:
        computerChoice = 'ROCK'
    
    # If computerChoice equals 2 it is set to PAPER.
    elif computerChoice == 2:
        computerChoice = 'PAPER'

    # Sets computerChoice to SCISSORS since 3 is the only value left.
    else:
        computerChoice = 'SCISSORS'

    playerChoice = ''

    while True:

        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        print()

        playerChoice = input()

        # Checks if the player's choice is equal to r to set it to ROCK
        if playerChoice == 'r':
            playerChoice = 'ROCK'
            break

        # Checks if the player's choice is equal to p to set it to PAPER
        elif playerChoice == 'p':
            playerChoice = 'PAPER'
            break

        # Checks if the player's choice is equal to s to set it to SCISSORS
        elif playerChoice == 's':
            playerChoice = 'SCISSORS'
            break

        # Checks if the player's choice is equal to q and quits the program
        elif playerChoice == 'q':
            sys.exit()

    print(playerChoice + ' versus...')
    print()

    print(computerChoice)

    # Checks results and updates the counters.

    # Checks if it is a tie.
    if playerChoice == computerChoice:

        print('It is a tie!')
        ties += 1

    # This section checks for player win conditions

    elif playerChoice == 'ROCK' and computerChoice == 'SCISSORS':

        print('You win!')
        wins += 1

    elif playerChoice == 'PAPER' and computerChoice == 'ROCK':

        print('You win!')
        wins += 1
        
    elif playerChoice == 'SCISSORS' and computerChoice == 'PAPER':

        print('You win!')
        wins += 1    
    
    # This section checks for player lose conditions

    elif playerChoice == 'SCISSORS' and computerChoice == 'ROCK':

        print('You lose.')
        losses += 1

    elif playerChoice == 'ROCK' and computerChoice == 'PAPER':

        print('You lose.')
        losses += 1

    elif playerChoice == 'PAPER' and computerChoice == 'SCISSORS':

        print('You lose.')
        losses += 1





    