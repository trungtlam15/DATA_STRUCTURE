def create_map(row, column):
    rows = []
    for i in range(row):
        columns = []
        for j in range(column):
            columns.append(0)
            # print("0", end="")
        rows.append(columns)
        # print()
    return rows


def print_map(map):
    for rows in range(len(map)):
        for columns in range(len(map[rows])):
            print(map[rows][columns], "\t", end="")
        print()
    print("----------------------")


def get_move():
    x = [-2, -2, -1, -1, 1, 1, 2, 2]
    y = [-1, 1, -2, 2, -2, 2, -1, 1]
    return [x, y]


def move(map, x, y, n, m, count):
    count += 1
    map[x][y] = count
    moves = get_move()
    # print_map(map)
    for i in range(len(moves[0])):
        move_x = moves[0][i]
        move_y = moves[1][i]
        if count == n * m:
            print_map(map)
            return
        new_x = x + move_x
        new_y = y + move_y

        if new_x >= 0 and new_y >= 0 \
                and new_x < n and new_y < m \
                and map[new_x][new_y] == 0:
            move(map, new_x, new_y, n, m, count)
    count -= 1
    map[x][y] = 0


if __name__ == '__main__':
    map = create_map(3, 4)
    print_map(map)
    move(map, 1,3, 3, 4, 0)
