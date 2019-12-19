num_in = int(input())

num2 = int(bin(num_in)[:1:-1], 2)

print(num2)