# -*- coding: utf-8 -*-
"""
Created on Sat May  9 15:57:29 2020

@author: Aleks
"""

b0 = [  # Sudoku written as a nettle list, empty spaces I replace by 0.
         [0,0,0,  0,0,0,  0,0,0],
         [0,0,0,  0,0,0,  0,0,0],
         [0,0,0,  0,0,0,  0,0,0],
         
         [0,0,0,  0,0,0,  0,0,0],
         [0,0,0,  0,0,0,  0,0,0],
         [0,0,0,  0,0,0,  0,0,0],
         
         [0,0,0,  0,0,0,  0,0,0],
         [0,0,0,  0,0,0,  0,0,0],
         [0,0,0,  0,0,0,  0,0,0]
         ]

b1 = [
         [0,0,0,  2,6,0,  7,0,1],
         [6,8,0,  0,7,0,  0,9,0],
         [1,9,0,  0,0,4,  5,0,0],
         
         [8,2,0,  1,0,0,  0,4,0],
         [0,0,4,  6,0,2,  9,0,0],
         [0,5,0,  0,0,3,  0,2,8],
         
         [0,0,9,  3,0,0,  0,7,4],
         [0,4,0,  0,5,0,  0,3,6],
         [7,0,3,  0,1,8,  0,0,0]
         ]

b2 = [
         [0,2,0,  0,0,0,  0,0,0],
         [0,0,0,  6,0,0,  0,0,3],
         [0,7,4,  0,8,0,  0,0,0],
         
         [0,0,0,  0,0,3,  0,0,2],
         [0,8,0,  0,4,0,  1,0,0],
         [6,0,0,  5,0,0,  0,0,0],
         
         [0,0,0,  0,1,0,  7,8,0],
         [5,0,0,  0,0,9,  0,0,0],
         [0,0,0,  0,0,0,  0,4,0]
         ]

table_3 =   [
             [2,0,0,  3,0,0,  0,0,0],
             [8,0,4,  0,6,2,  0,0,3],
             [0,1,3,  8,0,0,  2,0,0],
             
             [0,0,0,  0,2,0,  3,9,0],
             [5,0,7,  0,0,0,  6,2,1],
             [0,3,2,  0,0,0,  0,0,0],
             
             [0,2,0,  0,0,9,  1,4,0],
             [6,0,1,  2,5,0,  8,0,9],
             [0,0,0,  0,0,1,  0,0,1]
             ]



def print_sudoku(tbl):   # function, which prints sudoku in a grid
       
    print ('--------------------------')
                        
    for i in range(len(tbl)):  # len(tbl) = 9, the number of rows or collomns in Sudoku
        if i% 3 == 0 and i != 0:
            print ('------------------------')
            print ('                         ')            
        for j in range(len(tbl[0])):
            if j % 3 == 0: 
                print ('|', end = " ") 

            if j == 8:   # 8 is the last number in Sudoku, because python starts counting from zero.
                if tbl[i][j]==0:  # empty Sudoku spaces I represent by "."
                    print ('.')
                else:
                    print (str(tbl[i][j]) + ' |')
                                              
            if j != 8:
                if tbl[i][j] == 0:
                    print ('.' + ' ', end ="" )
                else:
                    print (str(tbl[i][j]), end= " " )
    print (' _ _ _ _ _ _ _ _ _ _ _ _ _ ')


def find_zero(tbl): # THis fubction finds empty spaces in Sedoku
    for i in range(len(tbl)):   # tbl is for table (Sudoku)
        for j in range(len(tbl[0])):
            if tbl[i][j] == 0:
                return (i, j)
    return None  # it means that we slove the Sudoku

def check(tbl, num, pos_x , pos_y): # the main function.
#where tbl is list of numbers( Sudoku), num is a number in a cell,
# pos_x and pos_y is the position of  the cell with number num.
# This function is checkung whether the number satisfies the Sudoku game rules. 
    #check row
    for i in range(len(tbl[0])):
        if tbl[pos_x   ][i] == num and pos_y !=i:
            return False
    # check collumn  
    for i in range(len(tbl)):
        if tbl[i][pos_y  ] == num and pos_x !=i:
            return False        
   #Check boxes / blocks/ squares which have dimention 3 x 3
    square_x = pos_y//3  # number of the box, which can be 1, 2, 3
    square_y = pos_x//3
    for i in range(square_y * 3, square_y*3 + 3):
         for j in range(square_x * 3, square_x * 3 + 3):
             if tbl[i][j] == num and (i,j) != (pos_x, pos_y):
                 return False # False means that the number is not suitable and vilate the Seduku rules.
    return True # It means the number is good.
    
def solve_puzzle(tbl):  # This the main function in my algorimth
    find = find_zero(tbl) #  Checking if there emty cells inthe puzzle.
    if not  find:
        return True
    else: # if not, start finding that eempty cell.
        row, col = find
        
    for i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:  # trying to check all numbers from 1 to 9.
        if check(tbl, i, row, col):
            tbl[row][col] = i
            if solve_puzzle(tbl):  #  This is a recursion, calling to the same function inside  the function.
                return True # if the function is True, we solved the puzle, if not, it goes False, and we start the process again.
            tbl[row][col] = 0 # in case the number we suggested is not good, so we 
    return False

print_sudoku(b1) # before solution, the Seduku with empty cells.
solve_puzzle(b1) # calling function, solve_puzzle, which fills empy cells.
print_sudoku(b1)                      
                    
        
        
        
        
        
    
    
    