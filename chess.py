board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
for i in board:
    for j in i:
        if j == 'R':
             col_R = i.index(j)
             row_R = board.index(i)


print(col_R)
print(row_R)


