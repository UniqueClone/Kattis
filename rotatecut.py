tests = int(input())

for test in range(tests):
    line = input().split()
    rotates = int(line[0])
    for rotate in range(rotates):
        s = line[1]
        s = s[::-1]
        x = len(s) // 4
        s = s[:len(s)-x:]
    if rotates % 2 != 0:
        s = s[::-1]
    print(s)