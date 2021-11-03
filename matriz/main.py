from random import randint

def gen_matrix():
    matrix = []
    transposed_matrix = [[0 for i in range(5)] for j in range(5)]
    #print(transposed_matrix)
    for i in range(5):
        matrix.append([randint(1, 5) for i in range(5)])

    print_matrix(matrix)

    for row in range(5):
        for col in range(5):
            transposed_matrix[row][col]=matrix[col][row]
    
    print_matrix(transposed_matrix)
    


def print_matrix(matrix):
    for row in matrix:
        print(row)



if __name__=='__main__':
    gen_matrix()