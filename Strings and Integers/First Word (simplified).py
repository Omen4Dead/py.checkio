def first_word(text: str) -> str:
    return text.split()[0]


def first_word_v2(text: str) -> str:
    idx = text.find(' ')
    if idx == -1:
        return text
    else:
        return text[:idx]


def first_word_v3(text: str) -> str:
    """
    sugar simply version of v2
    """
    index = text.find(" ")
    return text[:index] if index != -1 else text


print("Example:")
print(first_word("Hello world"))

# These "asserts" are used for self-checking
assert first_word("Hello world") == "Hello"
assert first_word_v2("a word") == "a"
assert first_word_v2("greeting from CheckiO Planet") == "greeting"
assert first_word_v2("hi") == "hi"

print("The mission is done! Click 'Check Solution' to earn rewards!")

word = 'helloworld'
print(word.find(' '))
