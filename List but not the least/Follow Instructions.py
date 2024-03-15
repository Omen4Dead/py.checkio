from __future__ import annotations


def follow(instructions: str) -> tuple[int, int] | list[int]:
    # your code here
    x = 0
    y = 0
    for i in instructions:
        if i == 'f':
            y += 1
        elif i == 'b':
            y -= 1
        elif i == 'l':
            x -= 1
        elif i == 'r':
            x += 1
    return [x, y]


print("Example:")
print(list(follow("fflff")))

# These "asserts" are used for self-checking
assert list(follow("fflff")) == [-1, 4]
assert list(follow("ffrff")) == [1, 4]
assert list(follow("fblr")) == [0, 0]

print("The mission is done! Click 'Check Solution' to earn rewards!")


# «f» - вперед
# «b» - назад
# «l» - влево
# «r» - вправо
