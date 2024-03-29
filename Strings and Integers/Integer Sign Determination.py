def determine_sign(num: int) -> str:
    if num > 0:
        return 'positive'
    elif num < 0:
        return 'negative'
    else:
        return "zero"


def determine_sign_v2(num: int) -> str:
    cmp = lambda x: (x > 0) - (x < 0)

    return {1: "positive", -1: "negative", 0: "zero"}[cmp(num)]


print("Example:")
print(determine_sign(11))

# These "asserts" are used for self-checking
assert determine_sign(5) == "positive"
assert determine_sign(0) == "zero"
assert determine_sign(-10) == "negative"
assert determine_sign(1) == "positive"
assert determine_sign(-1) == "negative"
assert determine_sign(999) == "positive"
assert determine_sign(-1000) == "negative"
assert determine_sign(123456789) == "positive"
assert determine_sign(-987654321) == "negative"
assert determine_sign(2) == "positive"

print("The mission is done! Click 'Check Solution' to earn rewards!")
