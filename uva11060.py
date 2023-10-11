import heapq
count = 1
ans_list = []
while True:
    try:
        bev_qtd = int(input())
        names = {}
        indexes = {}
        for x in range(bev_qtd):
            beverage = input()
            names[beverage] = x
            indexes[x] = beverage
        graph = [[0] * bev_qtd for _ in range(bev_qtd)]
        conn = int(input())
        graus = [0 for _ in range(bev_qtd)]
        for x in range(conn):
            less_alc, greater_alc = [x for x in input().split(' ')]
            if(graph[names[less_alc]][names[greater_alc]] == 0):
                graph[names[less_alc]][names[greater_alc]] = 1
                graus[names[greater_alc]] += 1
        heap = []
        order = []
        for x in range(bev_qtd):
            if graus[x] == 0:
                heapq.heappush(heap, x)
        while heap:
            node = heapq.heappop(heap)
            order.append(node)
            for x in range(len(graph[node])):
                if graph[node][x]:
                    graus[x] -= 1
                    if (graus[x] == 0):
                        heapq.heappush(heap, x)
        ans_str = ''
        for x in order:
            ans_str += ' ' + indexes[x]
        ans_str += '.'
        ans_list.append(
            f"Case #{count}: Dilbert should drink beverages in this order:{ans_str}")
        count += 1
        input()
    except Exception:
        print(*ans_list, sep="\n\n")
        print("")
        break
