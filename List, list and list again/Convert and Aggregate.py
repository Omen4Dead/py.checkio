def conv_aggr(data: list[tuple[str, int]]) -> dict[str, int]:
    # your code here
    df = {}
    for k, v in data:
        if k == '':
            continue
        if k not in df: df[k] = v
        else: df[k] = df[k] + v
    df_copy = df.copy()
    for k, v in df_copy.items():
        if v == 0:
            df.pop(k)
    return df


print("Example:")

# These "asserts" are used for self-checking
assert conv_aggr([("a", 7), ("b", 8), ("a", 10)]) == {"a": 17, "b": 8}
assert conv_aggr([]) == {}
assert conv_aggr([("a", 5), ("a", -5)]) == {}
assert conv_aggr([("a", 5), ("a", 5), ("a", 0)]) == {"a": 10}
assert conv_aggr([("a", 5), ("", 15)]) == {"a": 5}

print("The mission is done! Click 'Check Solution' to earn rewards!")
