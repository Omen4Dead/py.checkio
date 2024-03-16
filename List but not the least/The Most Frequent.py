
def most_frequent(data: list[str]) -> str:
    # your code here
    cnt = dict()
    for i in data:
        if i in cnt:
            cnt[i] += 1
        else:
            cnt[i] = 1
    sorted_data = list(sorted(cnt.items(), key=lambda item: item[1], reverse=True))
    return sorted_data[0][0]


print("Example:")
print(most_frequent(["a", "b", "c", "a", "b", "a"]))

# These "asserts" are used for self-checking
assert most_frequent(["a", "b", "c", "a", "b", "a"]) == "a"
assert most_frequent(["a", "a", "bi", "bi", "bi"]) == "bi"

print("The mission is done! Click 'Check Solution' to earn rewards!")
