matriz = [[1,2,3,4],[5,6,7,8],[9,8,7,6],[4,3,6,3]]

for j in range(0,4):
    for i in range(0,4):
        matriz[j][i] += 10
        print(matriz[j][i], end=" ")
    print()