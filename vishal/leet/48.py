#run in terminal: python "vishal/leet/48.py"
def rotate(matrix):
        row = len(matrix)
        col = len(matrix[0])

        for i in range(row):
            for j in range(i + 1, col):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for k in range(row):
            matrix[k].reverse()
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Original matrix:")
for row in matrix:
    print(row)
rotate(matrix)
print("Matrix after 90-degree clockwise rotation:")
for row in matrix:
    print(row)