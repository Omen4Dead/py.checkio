import re


def checkio(text: str) -> str:
    # your code here
    count = {}
    lst = re.findall('[a-z]', text.lower())
    for i in lst:
        if i not in count.keys():
            count[i] = 1
        else:
            count[i] += 1
        print(count)
    max_cnt = 0
    first_letter = 'z'
    for k, v in count.items():
        if v > max_cnt:
            max_cnt = v
            first_letter = k
        elif v == max_cnt:
            if k < first_letter:
                first_letter = k
        print(max_cnt, first_letter)
    return first_letter


print("Example:")

# These "asserts" are used for self-checking
assert checkio("Hello World!") == "l"
assert checkio("How do you do?") == "o"
assert checkio("One") == "e"
assert checkio("Oops!") == "o"
assert checkio("AAaooo!!!!") == "a"
assert checkio("abe") == "a"

print("The mission is done! Click 'Check Solution' to earn rewards!")
