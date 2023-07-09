"""
Write a function `can_construct(target, word_bank)` that accepts a target string and an array of strings

The function should return a boolean indicating whether or not the target can be constructed by concatenating elements of the 
word bank array

Reuse of elements in word_back is allowed.
"""

from typing import Dict, List


def can_construct(target: str, word_bank: List[str]) -> bool:
    if len(target) == 0:
        return True
    for word in word_bank:
        if target.startswith(word):
            if can_construct(target.removeprefix(word), word_bank):
                return True
            
    return False

def can_construct_memo(target: str, word_bank: List[str], memo: Dict[str, bool] = {}) -> bool:
    if target in memo:
        return memo[target]
    
    if len(target) == 0:
        return True
    
    for word in word_bank:
        if target.startswith(word):
            if can_construct_memo(target.removeprefix(word), word_bank, memo): 
                memo[target] = True
                return True
    memo[target] = False
    return False

def can_construct_tabular(target: str, word_bank: List[str]):
    table: List[bool] = [False] * (len(target)+1)
    table[0] = True
    for i in range(len(target)+1):
        if table[i]:
            for word in word_bank:
                if target[i:].startswith(word) and i + len(word) <= len(target):
                    table[i+len(word)] = True
    return table[len(target)]
    
print(can_construct(target="abcdef", word_bank=["ab", "abc", "cd", "def", "abcd"]))
print(can_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(can_construct_memo(target="abcdef", word_bank=["ab", "abc", "cd", "def", "abcd"]))
print(can_construct_memo("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(can_construct_tabular(target="abcdef", word_bank=["ab", "abc", "cd", "def", "abcd"]))
print(can_construct_tabular("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))