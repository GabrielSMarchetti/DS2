
def fibonacci(number):
    if number == 0:
        return 0
    if number == 1:
        return 1
    return fibonacci(number - 1) + fibonacci(number - 2)


def fibonacci_dp(number):
    if matriz_solucoes[number] != -1:
        return matriz_solucoes[number]
    matriz_solucoes[number] = fibonacci_dp(
        number - 1) + fibonacci_dp(number - 2)
    return matriz_solucoes[number]


matriz_solucoes = [-1] * 5001
matriz_solucoes[0] = 0
matriz_solucoes[1] = 1

while True:
    try:
        n = int(input().strip().replace("\n", "")
        print(f"The Fibonacci number for {n} is {fibonacci_dp(n)}")
    except EOFError:
        break
