import numpy as np
import random
import time
from enum import Enum
from tetromino import Tetromino

class UserAction(Enum):
    ROTATE_X_LEFT = 0
    ROTATE_X_RIGHT = 1
    ROTATE_Y_LEFT = 2
    ROTATE_Y_RIGHT = 3
    ROTATE_Z_LEFT = 4
    ROTATE_Z_RIGHT = 5
    PLANE_MOVE_UP = 6
    PLANE_MOVE_DOWN = 7
    PLANE_MOVE_LEFT = 8
    PLANE_MOVE_RIGHT = 9
    DROP = 10
    NONE = 11

class TetrisGame:
    def __init__(self, block_types):
        # A binary array representing whether an LED is on or off
        self.cube = np.zeros((8,8,8), np.bool)
        # types of blocks allowed in this tetris game
        self.block_types = block_types
        
        # the type of the block that is currently being controlled
        self.init_tetromino()
        
    def init_tetromino(self):
        start_x = random.randint(0,7)
        start_y = random.randint(0,7)
        start_z = 7
        
        current_block = random.choice(self.block_types)
        self.current_tetromino = Tetromino(current_block, self.cube, start_x, start_y, start_z)
        
        while not self.current_tetromino.is_valid_position():
            start_x = random.randint(0,7)
            start_y = random.randint(0,7)
            self.current_tetromino = Tetromino(current_block, self.cube, start_x, start_y, start_z)
            
    def get_user_action(self):
        """
        Evaluate the user action
        """
        pass
        
    def step(self):
        """
        Moves active tetronimo down by one timestep
        """
        # Fall one step
        self.current_tetromino.fall()
        self.reached_bottom()
    
    def reached_bottom(self):
        """
        Checks if active tetromino has reached the bottom and, if so, puts it in the board 
        and switches to a new tetromino
        """
        if not self.current_tetromino.can_fall():
            pieces = self.current_tetromino.cube_locations()
            self.cube[pieces[:, 0], pieces[:, 1], pieces[:, 2]] = True
            self.init_tetromino()
            
                                     
    def is_step_possible(self):
        """
        Checks whether there is another step is possible
        """
        return self.current_tetromino.can_fall() or self.current_tetromino.within_board()
        
    def run(self):
        """
        Start and loop game.
        """
        while (True):
            if self.is_step_possible():
                #TODO: Get user action
                self.step()
            else:
                break
                
        self.trigger_game_over()
            
    def trigger_game_over(self):
        """
        A game-over animation and reset of the game board 
        """
        print("Game Over")