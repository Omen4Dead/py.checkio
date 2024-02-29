def translation(text: str) -> str:
    # your code here
    copy_text = list(text)
    vowels_letters = "aeiouy"
    for k in range(len(copy_text)):
        if copy_text[k] not in vowels_letters and copy_text[k].isalpha():
            copy_text[k + 1] = ''
    for i in range(len(copy_text)):
        if copy_text[i] in vowels_letters and copy_text[i].isalpha():
            copy_text[i + 1] = ''
            copy_text[i + 2] = ''
    return ''.join(copy_text)


print("Example:")
print(translation("hieeelalaooo"))
# These "asserts" are used for self-checking
assert translation("hieeelalaooo") == "hello"
assert translation("hoooowe yyyooouuu duoooiiine") == "how you doin"
assert translation("aaa bo cy da eee fe") == "a b c d e f"
assert translation("sooooso aaaaaaaaa") == "sos aaa"

print("The mission is done! Click 'Check Solution' to earn rewards!")
