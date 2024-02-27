def count_occurrences(main_str: str, sub_str: str) -> int:
    # your code here
    main_str = main_str.lower()
    sub_str = sub_str.lower()
    res = 0
    for i in range(len(main_str)):
        # print(main_str[i:len(sub_str)+i], ' - ', i)
        if main_str[i:len(sub_str)+i] == sub_str:
            res += 1
        # print('res = ', res)
    return res


print("Example:")

# These "asserts" are used for self-checking
assert count_occurrences("hello world hello", "hello") == 2
assert count_occurrences("Hello World hello", "hello") == 2
assert count_occurrences("hello", "world") == 0
assert count_occurrences("hello world hello world hello", "world") == 2
assert count_occurrences("HELLO", "hello") == 1
assert count_occurrences("appleappleapple", "appleapple") == 2
assert count_occurrences("HELLO WORLD", "WORLD") == 1
assert count_occurrences("hello world hello", "o w") == 1
assert count_occurrences("apple apple apple", "apple") == 3
assert count_occurrences("apple Apple apple", "apple") == 3
assert count_occurrences("apple", "APPLE") == 1

print("The mission is done! Click 'Check Solution' to earn rewards!")
