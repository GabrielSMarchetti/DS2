while True:
    size, erase = [int(x) for x in input().split(' ')]
    if size == 0 and erase == 0:
        break
    numbers = [int(x) for x in input()]
    erased = 0
    ans = []
    for x in numbers:
        while erased < erase and ans and ans[-1] < x:
            ans.pop()
            erased += 1
        ans.append(x)
    while erased < erase:
        ans.pop()
        erased += 1
    print(*ans, sep='')
