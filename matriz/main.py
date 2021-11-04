from random import randint

def gen_matrix():    
    for i in range(5):
        matrix.append([randint(1, 10) for i in range(5)])

    print_matrix(matrix)
    return matrix

            
def get_four_in_line(matrix):
    """ This methods loops around the matrix and finds if there are 4 numbers align verically/horizontally"""
    transposed_matrix = [[0 for i in range(5)] for j in range(5)]
    four_in_line_set = set() # we use a set so we dont have to put the 4-in-line items in order when testing 
    
    for row in range(5):
        for col in range(5):
            transposed_matrix[row][col]=matrix[col][row]
    
    offset = 4
    for row in range(5):
        for col in range(2): 
            #since matrix is 5x5 and we need to get 4-in-line. we only need to analize the first 2 items back and forth
            item = matrix[row][col] 
            if matrix[row][col:offset + col] == [item, item + 1, item + 2, item + 3]: #checking 4 in line from 1st to 4th and 2nd to 5th element
                four_in_line_set.add(((row,col),(row,col + offset -1)))
            elif matrix[row][col:offset + col] == [item , item - 1, item -2, item-3]: #checking 4 in line from 1st to 4th and 2nd to 5th element backwards
                four_in_line_set.add(((row,col + offset -1),(row,col)))
    
    #we repeat the process with the transposed matrix
    for row in range(5):
        for col in range(2):
            item = transposed_matrix[row][col]
            if transposed_matrix[row][col:offset + col] == [item, item + 1, item + 2, item + 3]:
                four_in_line_set.add(((row,col),(row,col + offset -1)))
            elif transposed_matrix[row][col:offset + col] == [item , item - 1, item -2, item-3]:
                four_in_line_set.add(((row,col + offset -1),(row,col)))
    return four_in_line_set

def print_matrix(matrix):
    for row in matrix:
        print(row)

if __name__=='__main__':
    matrix = gen_matrix()
    get_four_in_line(matrix)