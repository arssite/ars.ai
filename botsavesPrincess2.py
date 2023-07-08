def nextMove(n, bot_row, bot_col, grid):
    princess_row, princess_col = None, None

    # Find the position of the princess 'p'
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'p':
                princess_row, princess_col = i, j
                break

    # Calculate the difference between bot and princess positions
    row_diff = princess_row - bot_row
    col_diff = princess_col - bot_col

    # Determine the next move based on the difference
    if row_diff > 0:
        return 'DOWN'
    elif row_diff < 0:
        return 'UP'
    elif col_diff > 0:
        return 'RIGHT'
    elif col_diff < 0:
        return 'LEFT'


    

n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))
