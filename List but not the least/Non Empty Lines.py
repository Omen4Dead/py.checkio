def non_empty_lines(text: str) -> int:
    # your code here
    if len(text) == 0:
        return 0
    lst = text.split('\n')
    cnt = 0
    for i in lst:
        if len(i.strip()) != 0:
            cnt += 1
    return cnt


print("Example:")
print(non_empty_lines("one\n simple line\n"))
print(non_empty_lines("\nLorem ipsum dolor sit amet,\n\nconsectetur adipiscing elit\nNam odio nisi, aliquam\n            "))

# These "asserts" are used for self-checking
assert non_empty_lines("one simple line\n") == 1
assert non_empty_lines("") == 0
assert non_empty_lines("\nonly one line\n            ") == 1
assert non_empty_lines("\nLorem ipsum dolor sit amet,\n\nconsectetur adipiscing elit\nNam odio nisi, aliquam\n            ")== 3

print("The mission is done! Click 'Check Solution' to earn rewards!")
