dists = input().split()

dists = [float(i) for i in dists]

while dists[0] != 0:
    x = (abs(dists[0] - dists[2]) ** dists[4])
    y = (abs(dists[1] - dists[3]) ** dists[4])
    bigger = (x+y) ** (1/dists[4])
    print(round(bigger, 10))

    dists = input().split()
    dists = [float(i) for i in dists]