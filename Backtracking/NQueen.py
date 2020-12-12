def isSafe(row, col, board, n):
    # check upper horizontal
    x= row-1
    y = col
    while x >= 0:
        if board[x][y] == 1: return False
        x-=1

    # left horizontal direction
    x = row -1
    y = col -1

    while x>=0 and y>=0:
        if board[x][y] == 1: return False
        x-=1
        y-=1

    # check right  horizontal direction
    x = row -1
    y = col +1
    while x >=0 and y <n:
        if board[x][y] == 1: return False
        x -= 1
        y += 1

    return True

# https://leetcode.com/problems/n-queens/discuss/562194/Clean-python-backtrack-40ms





from copy import copy
def printPaths(n):
    board = [[ 0 for j in range(n)] for i in range(n)]
    result = []
    def printPathHelper(row, n, board):
        if row == n:
            #print(board)
            print(board[:])
            result.append(copy(board))
            return  # print board before return

        for col in range(n):
            if isSafe(row, col, board, n):
                board[row][col] = 1
                printPathHelper(row + 1, n, board)
                board[row][col] = 0

    printPathHelper(0, n, board)
    return result


print(printPaths(4))

