from random import randint

def gen_matrix():
    matrix = [
        [4, 4, 3, 2, 1],
        [5, 3, 3, 5, 3],
        [2, 2, 1, 4, 4],
        [5, 1, 3, 4, 1],
        [5, 2, 4, 5, 2]
    ]
    transposed_matrix = [[0 for i in range(5)] for j in range(5)]
    #print(transposed_matrix)
    #for i in range(5):
    #    matrix.append([randint(1, 5) for i in range(5)])

    print_matrix(matrix)
    print("")
    for row in range(5):
        for col in range(5):
            transposed_matrix[row][col]=matrix[col][row]
    
    print_matrix(transposed_matrix)
    
    offset = 4
    for row in range(5):
        for col in range(2):
            item = matrix[row][col]
            if matrix[row][col:offset + col] == [item, item + 1, item + 2, item + 3]:
                print(f"4 en linea horizontal desde [{row}][{col}] hasta [{row}][{col + offset -1}]")
            elif matrix[row][col:offset + col] == [item , item - 1, item -2, item-3]:
                print(f"4 en linea horizontal desde [{row}][{col + offset -1}] hasta [{row}][{col}]")
    
    for row in range(5):
        for col in range(2):
            item = transposed_matrix[row][col]
            if transposed_matrix[row][col:offset + col] == [item, item + 1, item + 2, item + 3]:
                print(f"4 en linea vertical desde [{row}][{col}] hasta [{row}][{col + offset -1}]")
            elif transposed_matrix[row][col:offset + col] == [item , item - 1, item -2, item-3]:
                print(f"4 en linea vertical desde [{row}][{col + offset -1}] hasta [{row}][{col}]")
            


def print_matrix(matrix):
    for row in matrix:
        print(row)

if __name__=='__main__':
    gen_matrix()