from collections import deque

MAX_DIM = 8

movimentos = [
    (1, 2),
    (1, -2),
    (-1, 2),
    (-1, -2),
    (2, 1),
    (2, -1),
    (-2, 1),
    (-2, -1)
]


def bfs(startx, starty, finalx, finaly):
    if (startx == finalx and starty == finaly):
        return 0
    fila = deque()
    visited = [[0] * MAX_DIM for _ in range(MAX_DIM)]
    fila.append((startx, starty, 0))
    while fila:
        aux_x, aux_y, moves_aux = fila.popleft()
        visited[aux_x][aux_y] = 1
        for x in range(MAX_DIM):
            new_x = aux_x + movimentos[x][0]
            new_y = aux_y + movimentos[x][1]
            moves = moves_aux + 1
            if (MAX_DIM > new_x >= 0 and MAX_DIM > new_y >= 0 and visited[new_x][new_y] != 1):
                visited[new_x][new_y] = 1
                if (new_x == finalx and new_y == finaly):
                    return moves
                fila.append((new_x, new_y, moves))


while True:
    try:
        start, end = [x for x in input().split(' ')]
        start_x = ord(start[0]) % 97
        start_y = int(start[1]) - 1
        end_x = ord(end[0]) % 97
        end_y = int(end[1]) - 1
        moves = bfs(startx=start_x, starty=start_y,
                    finalx=end_x, finaly=end_y)
        print(f"To get from {start} to {end} takes {moves} knight moves.")

    except EOFError:
        break
