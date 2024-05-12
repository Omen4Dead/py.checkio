from collections.abc import Iterable
from itertools import chain


def flat_list_v1(array: list) -> Iterable[int]:
    fl_list = []
    for item in array:
        if isinstance(item, list):
            fl_list.extend(flat_list_v1(item))
        else:
            fl_list.append(item)
    return fl_list


def flat_list_v2(array) -> Iterable[int]:
    new_array = chain.from_iterable(array)
    return new_array


print("Example:")

# These "asserts" are used for self-checking
assert list(flat_list_v1([[1], [2, 2, 2], [4]])) == [1, 2, 2, 2, 4]
assert list(flat_list_v1([1, 2, 3])) == [1, 2, 3]
assert list(flat_list_v1([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]])) == [2, 4, 5, 6, 6, 6, 6, 6, 7]
assert list(flat_list_v1([-1, [1, [-2], 1], -1])) == [-1, 1, -2, 1, -1]

assert list(flat_list_v2([[1], [2, 2, 2], [4]])) == [1, 2, 2, 2, 4]
assert list(flat_list_v2([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]])) == [2, 4, 5, 6, 6, 6, 6, 6, 7]
assert list(flat_list_v2([1, 2, 3])) == [1, 2, 3]
assert list(flat_list_v2([-1, [1, [-2], 1], -1])) == [-1, 1, -2, 1, -1]

print("The mission is done! Click 'Check Solution' to earn rewards!")
