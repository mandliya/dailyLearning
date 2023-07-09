"""
Write a function `all_construct(target, word_bank)` that accepts a target string and an array of strings
The function should return a 2D array containing all the ways that the `target` can be constructed by
concatenating elements of word_bank array. 
Each element of the 2D array should represent one combination that constructs the target.
Reuse the words as many times as you need.
"""

from typing import Dict, List, Optional

def all_construct(target: str, word_bank: List[str]) -> List[List[str]]:
    if target == "":
        return [[]]
    all_combinations: List[List[str]] = []
    for word in word_bank:
        if target.startswith(word):
            remainder_combinations = all_construct(target.removeprefix(word), word_bank)
            for combination in remainder_combinations:
                all_combinations.append([word] + combination)

    return all_combinations

def all_construct_memo(target: str, word_bank: List[str], memo: Dict[str, List[List[str]]] = {}) -> List[List[str]]:
    if target in memo:
        return memo[target]
    if target == "":
        return [[]]
    
    all_combinations: List[List[str]] = []

    for word in word_bank:
        if target.startswith(word):
            remainder_combinations = all_construct_memo(target.removeprefix(word), word_bank, memo)
            for combination in remainder_combinations:
                all_combinations.append([word] + combination)
    
    memo[target] = all_combinations
    return all_combinations

def all_construct_tabular(target: str, word_bank: List[str]) -> List[List[str]]:
    table: List[List[List[str]]] = [[] for _ in range(len(target) + 1)]
    table[0] = [[]]

    for i in range(len(target) + 1):
        for word in word_bank:
            if target[i:i+len(word)] == word and i + len(word) <= len(target):
                new_combinations = [combination + [word] for combination in table[i]]
                table[i + len(word)] += new_combinations
    return table[len(target)]



print(all_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c']))
print(all_construct_memo('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c']))
print(all_construct_tabular('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c']))