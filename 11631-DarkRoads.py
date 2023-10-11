# encontra o ciclo atraves da ED disjointed sets
# union find
# simula uma estrutura de arvore e a busca dá-se até a raíz -> O(log n)
def find(parent, a):
    if parent[a] == a:
        return a
    return find(parent, parent[a])


def union(parent, a, b):
    parent[find(parent, a)] = find(parent, b)


while True:
    m, n = [
        int(x) for x in input().split(' ')]
    if m == n and m == 0:
        break

    # lendo args
    # kruskal algorithm
    matriz = []
    ans = 0
    for x in range(n):
        row, col, price = [int(x) for x in input().split(' ')]
        matriz.append([row, col, price])
        ans += price
    # primeiro passo - ordenar os pesos
    # timsort O(nlogn)
    matriz.sort(key=lambda x: x[2])
    max_index = 0
    parent = [x for x in range(m)]
    aux = 0
    total_items = 0
    while len(total_items) < m - 1:
        new_item = matriz[aux]
        first_item = find(parent, new_item[0])
        second_item = find(parent, new_item[1])
        # caso nao pertencam ao mesmo DS -> incluir
        if first_item != second_item:
            parent[first_item] = second_item
            ans -= new_item[2]
            total_items += 1
        aux += 1
    print(ans)
