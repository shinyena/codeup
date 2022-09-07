n = int(input())

pascal = []
for i in range(n):
    pascal.append([])
    for j in range(i+1):
        pascal[i].append(1)

for i in range(n):
    for j in range(i+1):
        if i == 0 or j in [0, i]:
            pascal[i][j] = 1
        else:
            pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]

for i in range(n):
    for j in range(i+1):
        print(pascal[i][j], end=" ")
    print()
