while True:
    lenght, n = [int(x) for x in input().split(' ')]
    if lenght == 0 and n == 0:
        break
    intervals = []
    for x in range(n):
        loc, radius = [int(x) for x in input().split(' ')]
        intervals.append((loc - radius, loc + radius))
    intervals.sort(key=lambda x: x[0])
    position = 0
    min_excluded = 0
    aux = 0
    while aux < n and position < lenght:
        if intervals[aux][0] > position:
            break
        aux_position = intervals[aux][1]
        while aux + 1 < len(intervals) and intervals[aux + 1][0] <= position:
            aux_position = max(aux_position, intervals[aux + 1][1])
            aux += 1
        position = aux_position
        min_excluded += 1
        aux += 1
    if position < lenght:
        print("-1")
    else:
        print(n - min_excluded)
