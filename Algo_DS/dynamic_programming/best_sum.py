"""
Write a function `bestSum(targetSum, numbers)` that takes in a target_sum and an array of numbers as arguments.

The function should return an array containing the shortest combination of numbers that add up exactly the target_sum.

If there is a tie for the shortest combination, return any of the shortest.
"""

from typing import Dict, List, Optional

def best_sum(target_sum: int, numbers: List[int]) -> Optional[List[int]]:
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None
    
    best_combination: Optional[List[int]] = None
    for num in numbers:
        remainder = target_sum - num
        remainder_result = best_sum(remainder, numbers)
        if remainder_result is not None:
            combination = remainder_result + [num]
            if best_combination is None or len(best_combination) > len(combination):
                best_combination = combination
    
    return best_combination

def best_sum_memo(target_sum: int, numbers: List[int], memo: Dict[int, Optional[List[int]]] = {}) -> Optional[List[int]]:
    
    if target_sum in memo:
        return memo[target_sum]
    
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None

    best_combination: Optional[List[int]] = None
    for num in numbers:
        remainder = target_sum - num
        remainder_result = best_sum_memo(remainder, numbers, memo)
        if remainder_result is not None:
            combination: List[int] = remainder_result + [num]
            if best_combination is None or len(best_combination) > len(combination):
                best_combination = combination
                memo[target_sum] = best_combination
    
    memo[target_sum] = best_combination
    return best_combination

def best_sum_tabular(target_sum: int, numbers: List[int]) -> Optional[List[int]]:
    table: Optional[List[int]] = [None] * (target_sum + 1)
    table[0] = []
    for cur in range(target_sum + 1):
        if table[cur] is not None:
            for num in numbers:
                if cur + num <= target_sum:
                    new_combination = table[cur] + [num]
                    if table[cur + num] is None or len(table[cur + num]) > len(new_combination):
                        table[cur + num] = new_combination
    return table[target_sum]

print(best_sum(7, [5, 3, 4, 7]))
print(best_sum(8, [2, 3, 5]))
print(best_sum(8, [1, 4, 5]))


print(best_sum_memo(7, [5, 3, 4, 7], {}))
print(best_sum_memo(8, [2, 3, 5], {}))
print(best_sum_memo(8, [1, 4, 5], {}))
print(best_sum_memo(100, [1, 2, 5, 25], {}))


print(best_sum_tabular(7, [5, 3, 4, 7]))
print(best_sum_tabular(8, [2, 3, 5]))
print(best_sum_tabular(8, [1, 4, 5]))
print(best_sum_tabular(100, [1, 2, 5, 25]))