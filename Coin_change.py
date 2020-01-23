"""
Leet code: 322. Coin Change
Problem Statement: ou are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.
"""
def change_coins(coins, amount):
  dp_array = [10000 for _ in range(amount+1)] # Fill in the dp_array with some random big number
  dp_array[0] = 0 # Number of coins needed to make amount 0 is at index 0 and so on.

  for i in range(1, len(dp_array)):
    for j in range(len(coins)):
      if coins[j] <= amount:
        dp_array[i] = min(dp_array[i], 1+dp_array[i-coins[j]])
  
  if dp_array[len(dp_array)-1] >= amount:
    return -1
  return dp_array[len(dp_array)-1]
