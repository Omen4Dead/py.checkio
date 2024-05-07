def checkio(game_result: list[str]) -> str:
    # your code here
    rows = game_result
    for i in rows:
        if i == 'XXX': return 'X'
        if i == 'OOO': return 'O'
    len_x = len(rows[0])
    cols = []
    for idx in range(len_x):
        col = ''
        for idx2 in range(len_x):
            col = col + rows[idx2][idx]
        cols.append(col)
        if col == 'XXX': return 'X'
        if col == 'OOO': return 'O'
    # print(cols, rows)
    diag_lr = ''
    for i in range(len_x):
        diag_lr = diag_lr + rows[i][i]
    if diag_lr == 'XXX': return 'X'
    if diag_lr == 'OOO': return 'O'

    diag_rl = ''
    for i in range(len_x):
        diag_rl = diag_rl + rows[i][::-1][i]
    diag_lr = diag_lr + rows[i][i]
    if diag_rl == 'XXX': return 'X'
    if diag_rl == 'OOO': return 'O'
    return "D"


print("Example:")

# These "asserts" are used for self-checking
assert checkio(["X.O", "XX.", "XOO"]) == "X"
assert checkio(["OO.", "XOX", "XOX"]) == "O"
assert checkio(["OOX", "XXO", "OXX"]) == "D"
assert checkio(['XOO', '.X.', 'X.X']) == 'X'
assert checkio(["O.X", "XX.", "XOO"]) == "X"

print("The mission is done! Click 'Check Solution' to earn rewards!")
