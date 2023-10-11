from collections import deque

MAX_INT = 10001


entries = int(input())
count = 1
for x in range(entries):
    servers_cont, conns, start, end = [int(x) for x in input().split(' ')]
    servers = [[0] * servers_cont for _ in range(servers_cont)]
    for x in range(conns):
        first, second, weight = [int(x) for x in input().split(' ')]
        servers[first][second] = weight
        servers[second][first] = weight
    visited = [0 for _ in range(servers_cont)]
    min_dist = [MAX_INT for _ in range(servers_cont)]
    min_dist[start] = 0
    fila = deque()
    fila.append(start)
    while (fila):
        next = fila.popleft()
        for i in range(len(servers[next])):
            if (servers[next][i] != 0):
                min_dist[i] = min(
                    min_dist[next] + servers[next][i], min_dist[i])
                if (visited[i] != 1):
                    visited[i] = 1
                    fila.append(i)
    if (min_dist[end] == MAX_INT):
        print(f'Case #{count}: unreachable')
        count += 1
        continue
    print(f'Case #{count}:', min_dist[end])
    count += 1
