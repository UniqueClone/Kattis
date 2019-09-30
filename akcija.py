noOfBooks = int(input())

books = []
for i in range(noOfBooks):
    books.append(int(input()))

books.sort(reverse=True)

total = 0
for i in range(len(books)+1):
    if i % 3 != 0:
        total += books[i-1]
print(total)
