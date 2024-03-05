from collections.abc import Iterable
from itertools import permutations


def string_permutations(s: str) -> Iterable[str]:

    if len(s) < 2:
        return list(s)

    perms = permutations(s)
    sorted_perms = sorted([''.join(p) for p in perms])

    return sorted_perms


print("Example:")
print(list(string_permutations("ab")))

# These "asserts" are used for self-checking
assert list(string_permutations("ab")) == ["ab", "ba"]
assert list(string_permutations("abc")) == ["abc", "acb", "bac", "bca", "cab", "cba"]
assert list(string_permutations("a")) == ["a"]
assert list(string_permutations("abcd")) == ["abcd", "abdc", "acbd", "acdb", "adbc", "adcb", "bacd", "badc", "bcad",
                                             "bcda", "bdac", "bdca", "cabd", "cadb", "cbad", "cbda", "cdab", "cdba",
                                             "dabc", "dacb", "dbac", "dbca", "dcab", "dcba" ]

print("The mission is done! Click 'Check Solution' to earn rewards!")
