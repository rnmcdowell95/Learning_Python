# Working with a given "picture" in list form that will be printed out using loops.

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

for y in range(0,6): 


        for x in range (0,9):        

                if (x == 8):
                        print(grid[x][y])
                
                else:
                        print(grid[x][y], end='')
    

# print(grid[0][0])