times = int(input())
for _ in range(times):
    teste = str(input())
    stack = teste.split(' ')
    print(len(stack))
    hand = stack[:52 - 25].copy()
    stack = stack[52 - 25:]
    y = 0
    card = stack.pop(-1)
    if card[0] in ['A', 'K', 'Q', 'T']:
        x = 10
        y += x
    else:
        x = int(card[0])
        y += x
    stack = stack[:10 - x]
    stack.append(hand)
    print(stack[y])
