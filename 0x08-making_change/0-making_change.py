#!/usr/bin/python3
'''
funtion to determine the fewest number of coins needed to meet a given amount total
'''

def makeChange(coins, total):
    n = len(coins)
    # Create a table to store the minimum number of coins needed for each total
    # Table size is (n+1) x (total+1)
    dp = [[0]*(total+1) for _ in range(n+1)]
    
    # Initialize the first row to infinity (except for the first cell, which is 0)
    for j in range(1, total+1):
        dp[0][j] = float('inf')
    
    # Fill in the table using bottom-up dynamic programming
    for i in range(1, n+1):
        for j in range(1, total+1):
            # If the coin value is greater than the total, we cannot use it
            if coins[i-1] > j:
                dp[i][j] = dp[i-1][j]
            # Otherwise, we can choose to use the coin or not use it
            # We take the minimum of the two options
            else:
                dp[i][j] = min(dp[i-1][j], 1 + dp[i][j-coins[i-1]])
    
    # Return the result (if it is infinity, that means the total cannot be met)
    return dp[n][total] if dp[n][total] != float('inf') else -1

