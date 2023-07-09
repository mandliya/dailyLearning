"""
Write a function `can_sum(target_sum, numbers)` that takes in a target_sum and an array of numbers as arguments.
The function should return a boolean indicating whether or not it is possible to generate a target_sum using numbers from the array.
"""

from typing import Dict, List

def can_sum_recur(target_sum: int, numbers: List[int]) -> bool:
    if target_sum < 0:
        return False
    if target_sum == 0:
        return True
    for num in numbers:
        remainder = target_sum - num
        if can_sum_recur(remainder, numbers):
            return True
    
    return False

def can_sum_memo(target_sum: int, numbers: List[int], memo: Dict[int, bool] = {}) -> bool:
    if target_sum in memo:
        return memo[target_sum]
    if target_sum < 0:
        return False
    if target_sum == 0:
        return True
    for num in numbers:
        remainder = target_sum - num
        if can_sum_memo(remainder, numbers, memo):
            memo[target_sum] = True
            return True
    memo[target_sum] = False
    return False

def can_sum_tabular(target_sum: int, numbers: List[int]) -> bool:
    if target_sum < 0:
        return False
    table: List[bool] = [False] * (target_sum + 1)
    table[0] = True
    for curr in range(target_sum + 1):
        for num in numbers:
            if table[curr]:
                if num + curr <= target_sum:
                    table[num + curr] = True
        
    return table[target_sum]
            
    




print(can_sum_recur(4, [1, 2]))
print(can_sum_recur(7, [3, 6]))
print(can_sum_memo(4, [1, 2], {}))
print(can_sum_memo(7, [3, 6], {}))
print(can_sum_tabular(4, [1, 2]))
print(can_sum_tabular(7, [3, 6]))

