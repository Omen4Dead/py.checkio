def end_zeros(a: int) -> int:
    # your code here
    nums = [int(i) for i in str(a)]
    cnt = 0
    for ind, num in enumerate(nums[::-1]):
        if num == 0:
            cnt += 1
        else:
            break
    return cnt


print("Example:")
print(end_zeros(0))

# These "asserts" are used for self-checking
assert end_zeros(0) == 1
assert end_zeros(1) == 0
assert end_zeros(10) == 1
assert end_zeros(101) == 0
assert end_zeros(245) == 0
assert end_zeros(100100) == 2

print("The mission is done! Click 'Check Solution' to earn rewards!")
