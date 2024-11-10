data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(data[1][1])
print()

for i in range(len(data)):
    for j in range(len(data[i])):
        print(data[i][j], end=" ")
    print()
