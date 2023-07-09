"""
Find nth element of the Fibonnaci Sequence.

Expected time complexity: O(n)
"""

from typing import Dict, List

def nth_fibonnaci_element_recurse(n: int) -> int:
    if n <= 2:
        return 1
    return nth_fibonnaci_element_recurse(n-1) + nth_fibonnaci_element_recurse(n-2)


def nth_fibonnaci_element_dp(n: int, memo: Dict[int, int] = {}) -> int:
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = nth_fibonnaci_element_dp(n-1, memo) + nth_fibonnaci_element_dp(n-2, memo)
    return memo[n]

def nth_fibonnaci_element_tabular(n: int) -> int:
    table: List[int] = [0] * (n+1)
    table[1] = 1
    for i in range(2, n+1):
        table[i] = table[i-1] + table[i-2]
    
    return table[n]



print(f'7th fibonnaci element is: {nth_fibonnaci_element_recurse(7)}')
print(f'7th fibonnaci element is: {nth_fibonnaci_element_dp(7)}')
print(f'7th fibonnaci element is: {nth_fibonnaci_element_tabular(7)}')
print(f'50th fibonnaci element is: {nth_fibonnaci_element_dp(50)}')
print(f'50th fibonnaci element is: {nth_fibonnaci_element_tabular(50)}')

