def checkio(array: list[int]) -> int:
    # your code here
    if array.__len__() == 0:
        return 0
    pr_res = 0
    for n, num in enumerate(array):
        if n % 2 == 0:
            pr_res += num
    return pr_res * array[-1]


print("Example:")
print(checkio([0, 1, 2, 3, 4, 5]))

# These "asserts" are used for self-checking
assert checkio([0, 1, 2, 3, 4, 5]) == 30
assert checkio([1, 3, 5]) == 30
assert checkio([6]) == 36
assert checkio([]) == 0

print("The mission is done! Click 'Check Solution' to earn rewards!")
