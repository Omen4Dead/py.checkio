# Taken from mission Goes Right After (simplified)

def goes_after(word: str, first: str, second: str) -> bool:
    # your code here
    f = word.find(first)
    s = word.find(second)
    if f != -1 and s != -1:
        if s - f == 1:
            return True
    return False


print("Example:")
print(goes_after("world", "w", "o"))

# These "asserts" are used for self-checking
assert goes_after("world", "w", "o") == True
assert goes_after("world", "w", "r") == False
assert goes_after("world", "l", "o") == False
assert goes_after("panorama", "a", "n") == True
assert goes_after("list", "l", "o") == False
assert goes_after("", "l", "o") == False
assert goes_after("list", "l", "l") == False
assert goes_after("world", "d", "w") == False
assert goes_after("Almaz", "a", "l") == False
assert goes_after('world', 'w', 'o') == True
assert goes_after('world', 'w', 'r') == False
assert goes_after('world', 'l', 'o') == False
assert goes_after('panorama', 'a', 'n') == True
assert goes_after('list', 'l', 'o') == False
assert goes_after('', 'l', 'o') == False
assert goes_after('list', 'l', 'l') == False
assert goes_after('world', 'd', 'w') == False
assert goes_after('Almaz', 'a', 'l') == False
assert goes_after('transport', 'r', 't') == False
assert goes_after('almaz', 'a', 'l') == True
assert goes_after('almaz', 'm', 'a') == False

print("The mission is done! Click 'Check Solution' to earn rewards!")
