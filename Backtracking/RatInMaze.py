def printHelper(x, y, maze, n, solution):
    # reached the solution
    # base case
    if x == n-1 and y == n-1:
        solution[x][y] = 1
        print(solution)
        # this step is not necessary because it is base case
        solution[x][y] = 0
        return
    # base case - blocking cases
    # maze[x][y] - if there is block on the road
    # solution[x][y] == 1 - already visited not explore this
    if x < 0 or y < 0 or x>= n or y>= n or maze[x][y] == 0 or solution[x][y] == 1:
        return

    solution[x][y] = 1
    printHelper(x+1, y, maze, n , solution)
    printHelper(x-1, y, maze, n, solution)
    printHelper(x, y+1, maze, n, solution)
    printHelper(x, y-1, maze, n, solution)
    # very important step

    solution[x][y] = 0
    pass

def printPath(maze):
    n = len(maze)

    #initialy every solution filled by 0
    solution = [ [ 0 for j in range(n)] for i in range(n)]
    printHelper(0, 0, maze, n, solution)



printPath([
        [1,1,0],
        [1,0,1],
        [1,1,1]
       ])