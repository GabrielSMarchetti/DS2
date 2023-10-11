import sys


tudo = sys.stdin.readlines()
casos = -1
for x in tudo:
    if (casos == -1):
        casos = x
        continue
    if (x == '\n'):
        continue
    if (len(x) == 1):
        maior = ord(x) % 65 + 1
        matriz = []
        for i in range(maior):
            matriz[i].append([])
            for k in range(maior):
                matriz[i][k] = 0
        break
print(matriz)
