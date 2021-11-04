from random import randint

def gen_matrix():
    matrix = [
        #[1, 4, 4, 3, 1],
        #[3, 2, 5, 3, 4],
        #[2, 4, 2, 3, 5],
        #[5, 4, 3, 2, 1],
        #[3, 3, 4, 4, 3]
    ]    
    for i in range(5):
        matrix.append([randint(1, 5) for i in range(5)])

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
                four_in_line_set.add(((row,col + offset -1 ),(row,col)))
    
    #we repeat the process with the transposed matrix
    for row in range(5):
        for col in range(2):
            item = transposed_matrix[row][col]
            if transposed_matrix[row][col:offset + col] == [item, item + 1, item + 2, item + 3]:
                four_in_line_set.add(((col,row),(col + offset -1,row)))
            elif transposed_matrix[row][col:offset + col] == [item , item - 1, item -2, item-3]:
                four_in_line_set.add(((col + offset -1, row),(col,row)))
    return four_in_line_set

def print_matrix(matrix):
    for row in matrix:
        print(row)

if __name__=='__main__':
    matrix = gen_matrix()
    print_matrix(matrix)
    
    four_in_line = get_four_in_line(matrix)
    
    if not four_in_line:
        print("there are no 4 consecutive numbers")
    else:
        print("lines found")
        for line in four_in_line:
            print(line)