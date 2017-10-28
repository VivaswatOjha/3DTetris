import numpy as np
from tetris import TetrisGame


#
# 1
# 2 1
#
fbi_block = np.array([[0,0,0],[1,0,0],[0,1,0],[0,0,1]], np.int) 

#
# 1
# 1 2
#
z_block = np.array([[0,0,0],[0,1,0],[1,0,0],[1,0,1]], np.int)

#
# 1 1
# 1 1
#
square_block = np.array([[0,0,0],[1,0,0],[0,1,0],[1,1,0]], np.int)    

#
# 1
# 1
# 1 1
#
l_block = np.array([[0,0,0],[0,1,0],[0,2,0],[1,0,0]], np.int)
    
# 1
# 1
# 1
# 1
tall_block = np.array([[0,0,0],[1,0,0], [2,0,0], [3,0,0]], np.int)

# 
#     1
#   1 1 1
# 
turn_block = np.array([[0,0,0], [1,0,0], [1,1,0], [2,0,0]], np.int)

#
#   1 1
# 1 1
#                  
snake_block = np.array([[0,0,0], [1,0,0], [1,1,0], [2,1,0]], np.int)
                  
                  
block_types = [fbi_block, square_block, l_block,
               tall_block, turn_block, snake_block]

tetris_game = TetrisGame(block_types)
tetris_game.run()