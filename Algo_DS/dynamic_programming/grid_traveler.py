"""
Given a mxn grid. An agent needs to travel from top left to bottom right of the grid. Agent can only travel right or down.
Find the number of ways agent can travel.
"""

from typing import Dict, List, Tuple

def num_ways_recurse(m: int, n: int) -> int:
    if m == 0 or n == 0:
        return 0
    if m == 1 and n == 1:
        return 1
    return num_ways_recurse(m-1, n) + num_ways_recurse(m, n-1)

def num_ways_memo(m: int, n: int, memo: Dict[Tuple[int, int], int] = {}) -> int:
    key = (m, n)
    if key in memo:
        return memo[key]
    if m == 0 or n == 0:
        return 0
    if m == 1 and n == 1:
        return 1
    memo[key] = num_ways_memo(m-1, n, memo) + num_ways_memo(m, n-1, memo)
    return memo[key]

def num_ways_tabular(m: int, n: int):
    table: List[List[int]] = [[0] * (n+1)] * (m+1)
    table[1][1] = 1
    for i in range(1, m+1):
        for j in range(1, n+1):
            table[i][j] = table[i-1][j] + table[i][j-1]
    return table[m][n]


print(f'For a grid of size 3 x 3, the agent can traverse in {num_ways_recurse(3, 3)} ways')
print(f'For a grid of size 2 x 4, the agent can traverse in {num_ways_recurse(2, 4)} ways')
print(f'For a grid of size 3 x 3, the agent can traverse in {num_ways_memo(3, 3)} ways')
print(f'For a grid of size 2 x 4, the agent can traverse in {num_ways_memo(2, 4)} ways')
print(f'For a grid of size 3 x 3, the agent can traverse in {num_ways_tabular(3, 3)} ways')
print(f'For a grid of size 2 x 4, the agent can traverse in {num_ways_tabular(2, 4)} ways')
print(f'For a grid of size 18 x 18, the agent can traverse in {num_ways_memo(18, 18)} ways')
print(f'For a grid of size 18 x 18, the agent can traverse in {num_ways_tabular(18, 18)} ways')