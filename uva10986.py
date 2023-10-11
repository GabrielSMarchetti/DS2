from collections import deque


def dijkstra(matrix, start, end, time):
    if (start == end):
        return 1
    visited = [0 for _ in range(len(matrix))]
    min_time = [time + 1 for _ in range(len(matrix))]
    min_time[start] = 0
    queue = deque()
    queue.append(start)
    visited[start] = 1
    while queue or min_time[end] > time:
        node = queue.popleft()
        for x in range(matrix[node]):
            if (matrix[node][x] != 0):
                min_time[x] = min(
                    min_time[x], min_time[node] + matrix[node][x])
                if (visited[x] != 1):
                    visited[x] = 1
                    queue.append(x)
    return min_time[end] <= time


cases = int(input())

for x in range(cases):
    input()
    count = 0
    cages = int(input())
    exit_index = int(input())
    limit = int(input())
    conn = int(input())
    cages_matrix = [[0] * cages for _ in range(cages)]
    for i in range(conn):
        start, end, time = [int(x) for x in input().split(' ')]
        cages_matrix[start][end] = time
    for i in range(len(cages_matrix)):
        if (dijkstra(cages_matrix, i, exit_index, limit)):
            count += 1
    print(count)
