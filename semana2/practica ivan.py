from operator import itemgetter

matriz = [[1, 2, 3, 4], [0, 21, 34, 2], [4, 5, 5, 10], [10, 60, 600, 100]]

print(max(matriz, key=itemgetter(2))[2])