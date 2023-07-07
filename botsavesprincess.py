def rescue_princess(n, grid):
    # Find bot 'm' and princess 'p' positions
    bot_position = None
    princess_position = None

    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'm':
                bot_position = (i, j)
            elif grid[i][j] == 'p':
                princess_position = (i, j)

    # Determine relative positions and calculate moves
    moves = []
    bot_row, bot_col = bot_position
    princess_row, princess_col = princess_position

    # Move the bot towards the princess
    while bot_row != princess_row:
        if bot_row < princess_row:
            moves.append('DOWN')
            bot_row += 1
        else:
            moves.append('UP')
            bot_row -= 1

    while bot_col != princess_col:
        if bot_col < princess_col:
            moves.append('RIGHT')
            bot_col += 1
        else:
            moves.append('LEFT')
            bot_col -= 1

    return moves


# Get the input from the user
n = int(input())
grid = []

print(f"Enter the {n}x{n} grid:")
for _ in range(n):
    row = list(input())
    grid.append(row)

rescue_moves = rescue_princess(n, grid)

# Print the moves
for move in rescue_moves:
    print(move)
