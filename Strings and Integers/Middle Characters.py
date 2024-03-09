def middle(text: str) -> str:
    # replace this for solution
    if len(text) % 2 == 0:  # 2 letters
        index = len(text) // 2
        return text[index-1:index+1]
    else:  # 1 letter
        index = len(text) // 2
        return text[index]


print("Example:")
print(middle("example"))

# These "asserts" are used for self-checking
assert middle("example") == "m"
assert middle("test") == "es"

print("The mission is done! Click 'Check Solution' to earn rewards!")
