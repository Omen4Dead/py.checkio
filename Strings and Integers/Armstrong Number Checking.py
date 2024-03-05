def is_armstrong(num: int) -> bool:
    # your code here
    num_str = str(num)
    digits = [int(digit) for digit in num_str]
    res = 0
    for i in digits:
        res += i**len(num_str)
    if num == res:
        return True
    else:
        return False


print("Example:")
print(is_armstrong(11))

# These "asserts" are used for self-checking
assert is_armstrong(153) == True
assert is_armstrong(370) == True
assert is_armstrong(947) == False
assert is_armstrong(371) == True
assert is_armstrong(407) == True
assert is_armstrong(163) == False
assert is_armstrong(100) == False
assert is_armstrong(8208) == True
assert is_armstrong(930) == False
assert is_armstrong(4) == True

print("The mission is done! Click 'Check Solution' to earn rewards!")
