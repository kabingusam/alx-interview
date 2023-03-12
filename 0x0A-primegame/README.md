### Prime Game
This program implements a game in which two players, Maria and Ben, take turns choosing prime numbers from a set of consecutive integers starting from 1 up to and including n. The player that cannot make a move loses the game. The program determines the winner of x rounds of the game, where n may be different for each round.

- Usage

The program can be run from the command line as follows:


    python prime_game.py

The isWinner() function can be imported and used in other Python programs as follows:

    from prime_game import isWinner

    winner = isWinner(3, [4, 5, 1])
    print(winner)

The isWinner() function takes two arguments: x, the number of rounds, and nums, a list of n for each round. It returns the name of the player that won the most rounds. If the winner cannot be determined, it returns None.


### Functionality

The isWinner function works as follows:

- It generates primes with a limit of the maximum number in nums
- For each round in nums, it filters the number of primes less than n
- It counts the number of primes and checks if it is even or odd
- It updates the score of Maria or Ben accordingly
- It returns the winner or None if it is a draw


### Authors & Contributers:
*kabingu Sammy* - [Github](https://github.com/kabingusam) || [twitter](https://twitter.com/Kabingusammy)

### Acknowledgments 
***
Alx SE Program.