# N皇后问题是指在N*N的棋盘上摆放N个皇后，要求任何两个皇后不同行、不同列、不在同一条斜线上。给定一个整数n，返回n皇后的摆法有多少种
def N_Queen(n):
    if n == 0:
        return []
    if n == 1:
        return [['Q']]

    def dfs(x_row, y_row, chessboard):
        pass

    def is_valid(chessboard):
        for i in range(len(chessboard)):
            for j in range(len(chessboard)):
                if chessboard[i][j] == 'Q':
                    pass

    result = []
    dfs(0, 0, [[]])
    return result
