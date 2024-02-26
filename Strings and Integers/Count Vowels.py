def count_vowels(text: str) -> int:
    cnt_vowels = 0
    for i in text.lower():
        if i in ('a', 'e', 'i', 'o', 'u'):
            cnt_vowels += 1
    return cnt_vowels


print("Example:")
print(count_vowels("Hello"))

# These "asserts" are used for self-checking
assert count_vowels("hello") == 2
assert count_vowels("openai") == 4
assert count_vowels("typescript") == 2
assert count_vowels("a") == 1
assert count_vowels("b") == 0
assert count_vowels("aeiou") == 5
assert count_vowels("AEIOU") == 5
assert count_vowels("The quick brown fox") == 5
assert count_vowels("Jumps over the lazy dog") == 6
assert count_vowels("") == 0

print("The mission is done! Click 'Check Solution' to earn rewards!")
