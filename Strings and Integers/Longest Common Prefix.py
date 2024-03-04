def longest_prefix(arr: list[str]) -> str:
    # your code here
    if not arr:
        return ""

        # Используем первую строку в качестве основы для сравнения
    prefix = arr[0]

    for string in arr[1:]:
        index = 0
        # Сравниваем символы до тех пор, пока не достигнем конца строки или не найдем различие
        while index < len(prefix) and index < len(string) and prefix[index] == string[index]:
            index += 1

        # Обновляем префикс до последнего совпадающего символа
        prefix = prefix[:index]

    return prefix


print("Example:")
print(longest_prefix(["flower", "flow", "flight"]))

# These "asserts" are used for self-checking
assert longest_prefix(["flower", "flow", "flight"]) == "fl"
assert longest_prefix(["dog", "racecar", "car"]) == ""
assert longest_prefix(["apple", "application", "appetizer"]) == "app"
assert longest_prefix(["a"]) == "a"
assert longest_prefix(["", "b"]) == ""
assert longest_prefix(["same", "same", "same"]) == "same"
assert longest_prefix(["mismatch", "mister", "miss"]) == "mis"
assert longest_prefix(["alphabet", "alpha", "alphadog"]) == "alpha"
assert longest_prefix(["book", "boot", "booster"]) == "boo"
assert longest_prefix(["short", "shore", "shot"]) == "sho"

print("The mission is done! Click 'Check Solution' to earn rewards!")
