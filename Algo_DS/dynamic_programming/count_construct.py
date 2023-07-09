"""
Write a function `count_construct(target, word_bank)` that accepts a target string and an array of strings.
The function should return the number of ways that the target can be constructed by cancatenating elements of the word bank array

Reuse of the elements is allowed.
"""

from typing import Dict, List

def count_construct(target: str, word_bank: List[str]) -> int:
    if target == "":
        return 1
    count: int = 0
    for word in word_bank:
        if target.startswith(word):
            count += count_construct(target.removeprefix(word), word_bank)
    return count

def count_construct_memo(target: str, word_bank: List[str], memo: Dict[str, int] = {}) -> int:
    if target in memo:
        return memo[target]
    if target == "":
        return 1
    
    count: int = 0
    for word in word_bank:
        if target.startswith(word):
            count += count_construct_memo(target.removeprefix(word), word_bank, memo)
    
    memo[target] = count
    return count


def count_construct_tabular(target: str, word_bank: List[str]):
    table: List[int] = [0] * (len(target) + 1)
    table[0] = 1

    for i in range(len(target) + 1):
        if table[i] > 0:
            for word in word_bank:
                if target[i:].startswith(word) and i + len(word) <= len(target):
                    table[i + len(word)] = table[i] +  table[i + len(word)]

    return table[len(target)]

print(count_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(count_construct("purple", ["purp", "p", "ur", "le", "purpl"]))
print(count_construct_memo("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(count_construct_memo("purple", ["purp", "p", "ur", "le", "purpl"]))
print(count_construct_tabular("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(count_construct_tabular("purple", ["purp", "p", "ur", "le", "purpl"]))