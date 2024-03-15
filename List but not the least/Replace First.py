from collections.abc import Iterable


def replace_first(items: list) -> Iterable:
    # your code here
    if len(items) < 2:
        return items
    else:
        first = items[0]
        new_list = items[1:]
        new_list.append(first)
        return new_list


# These "asserts" are used for self-checking
print("Example:")
print(replace_first([1, 2, 3, 4]))

assert replace_first([1, 2, 3, 4]) == [2, 3, 4, 1]
assert replace_first([1]) == [1]
assert replace_first([]) == []

print("The mission is done! Click 'Check Solution' to earn rewards!")
