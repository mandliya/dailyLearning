"""
Write a function `howSum(targetSum, numbers)` that takes in a targetSum and an array of numbers as arguments.
The function should return an array containing any combination of elements that add up exactly to targetSum. If there is no
combination that adds up to the targetSum, then return empty list
"""

from typing import Dict, List, Optional

def how_sum_recur(target_sum: int, numbers: List[int]) -> Optional[List[int]]:
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None
    
    for num in numbers:
        remainder = target_sum - num
        remainder_result = how_sum_recur(remainder, numbers) 
        if remainder_result is not None:
            return remainder_result + [num]
    
    return None

def how_sum_memo(target_sum: int, numbers: List[int], memo: Dict[int, Optional[List[int]]] = {}) -> Optional[List[int]]:
    if target_sum in memo:
        return memo[target_sum]
    
    if target_sum == 0:
        return []
    
    if target_sum < 0:
        return None
    
    for num in numbers:
        remainder = target_sum - num
        remainder_result = how_sum_memo(remainder, numbers, memo)
        if remainder_result is not None:
            memo[target_sum] = remainder_result + [num]
            return memo[target_sum]
        
    memo[target_sum] = None
    return None

def how_sum_tabular(target_sum: int, numbers: List[int]) -> Optional[List[int]]:
    if target_sum < 0:
        return None
    
    table: Optional[List[int]] = [None] * (target_sum + 1)
    table[0] = []
    for cur in range(target_sum + 1):
        if table[cur] is not None:
            for num in numbers:
                if cur + num <= target_sum:
                    table[cur + num] = table[cur] + [num]
    
    return table[target_sum]


print(how_sum_recur(7, [4, 6, 7]))
print(how_sum_recur(7, [4, 5, 9]))
print(how_sum_memo(7, [4, 6, 7], {}))
print(how_sum_memo(7, [4, 5, 9], {}))
print(how_sum_tabular(7, [4, 6, 7]))
print(how_sum_tabular(7, [4, 5, 9]))

print(how_sum_recur(8, [2, 3, 5]))
print(how_sum_memo(8, [2, 3, 5], {}))
print(how_sum_tabular(8, [2, 3, 5]))