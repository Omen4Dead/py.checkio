def checkio(words: str) -> bool:
    # add your code here
    res = 0
    for i in enumerate(words.split()):
        if i[1].isdigit():
            res = 0
        else:
            res += 1
        if res > 2:
            return True
    return res > 2


print("Example:")
print(checkio("Hello World 213 hello"))

# These "asserts" are used for self-checking
assert checkio("Hello World hello") == True
assert checkio("He is 123 man") == False
assert checkio("1 2 3 4") == False
assert checkio("bla bla bla bla") == True
assert checkio("Hi") == False
assert checkio('one two 3 four five six 7 eight 9 ten eleven 12') == True

print("The mission is done! Click 'Check Solution' to earn rewards!")
