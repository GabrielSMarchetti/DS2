
def calculate_number(z, l, i, m):
    aux = z * l
    aux += i
    return aux % m


count = 1
while True:
    line = [float(x) for x in input().strip().split(' ')]
    if line == [0, 0, 0, 0]:
        break
    z, i, m, l = [x for x in line]
    slow = calculate_number(z=z, l=l, i=i, m=m)
    fast = calculate_number(z=z, l=slow, i=i, m=m)
    cycle = 1
    while slow != fast:
        slow = calculate_number(z=z, l=slow, i=i, m=m)
        fast = calculate_number(z=z, l=fast, i=i, m=m)
        fast = calculate_number(z=z, l=fast, i=i, m=m)
        cycle += 1
    print(f"Case {count}: {cycle}")
    count += 1
