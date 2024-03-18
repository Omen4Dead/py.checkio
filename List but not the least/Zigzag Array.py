def create_zigzag(rows: int, cols: int, start: int = 1) -> list[list[int]]:
    # your code here
    numbers = list(range(start, rows*cols + start))
    zig = []
    while len(numbers) > 0:
        zig.append(numbers[:cols])
        numbers = numbers[cols:]
    zag = []
    for idx, val in enumerate(zig):
        if idx % 2 == 0:
            zag.append(sorted(val))
        else:
            zag.append(sorted(val, reverse=True))
    return zag


print("Example:")
print(create_zigzag(3, 3, 5))

# These "asserts" are used for self-checking
assert create_zigzag(3, 5) == [[1, 2, 3, 4, 5], [10, 9, 8, 7, 6], [11, 12, 13, 14, 15]]
assert create_zigzag(5, 1) == [[1], [2], [3], [4], [5]]
assert create_zigzag(3, 3, 5) == [[5, 6, 7], [10, 9, 8], [11, 12, 13]]
assert create_zigzag(3, 0) == [[], [], []]

print("The mission is done! Click 'Check Solution' to earn rewards!")
