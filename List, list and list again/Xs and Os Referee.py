def checkio(game_result: list[str]) -> str:
    # your code here
    len_x = len(game_result[0])
    len_y = len(game_result)
    if "XXX" in game_result:
        return "X"
    if "OOO" in game_result:
        return "O"
    for y in range(len_y):
        res = ''
        diag_res1 = ''
        for x in range(len_x):
            print(('x: ', x, 'y: ', y), game_result[x][y])
            res = res + game_result[x][y]
            diag_res1 = diag_res1 + game_result[x][x]
        print('res: ', res)
        print('diag_res1: ', diag_res1)
        if res == "XXX":
            return "X"
        if res == "OOO":
            return "O"
    return "D"


print("Example:")

# These "asserts" are used for self-checking
assert checkio(["X.O", "XX.", "XOO"]) == "X"
assert checkio(["OO.", "XOX", "XOX"]) == "O"
assert checkio(["OOX", "XXO", "OXX"]) == "D"
assert checkio(["O.X", "XX.", "XOO"]) == "X"

print("The mission is done! Click 'Check Solution' to earn rewards!")
