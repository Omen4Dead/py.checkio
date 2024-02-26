# Taken from mission Just Fizz!

def checkio(num: int) -> str:
    div_3 = num % 3
    div_5 = num % 5
    if div_3 == 0 and div_5 == 0:
        return "Fizz Buzz"
    elif div_3 == 0:
        return "Fizz"
    elif div_5 == 0:
        return "Buzz"
    else:
        return str(num)


print("Example:")
print(checkio(15))

# These "asserts" are used for self-checking
assert checkio(15) == "Fizz Buzz"
assert checkio(6) == "Fizz"
assert checkio(10) == "Buzz"
assert checkio(7) == "7"

print("The mission is done! Click 'Check Solution' to earn rewards!")
