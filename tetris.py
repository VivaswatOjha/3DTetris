import numpy as np
import random
import time
import keyboard
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from enum import Enum
from tetromino import Tetromino

class TetrisGame:
    def __init__(self, block_types):
        # A binary array representing whether an LED is on or off
        self.cube = np.zeros((8,8,11), np.int)
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
            
    def process_user_action(self):
        """
        Evaluate the user action
        """
        if keyboard.is_pressed('q'):
            self.current_tetromino.rotate_x_forward()
        elif keyboard.is_pressed('a'):
            self.current_tetromino.rotate_x_backward()
        elif keyboard.is_pressed('w'):
            self.current_tetromino.rotate_y_forward()
        elif keyboard.is_pressed('s'):
            self.current_tetromino.rotate_y_backward()
        elif keyboard.is_pressed('e'):
            self.current_tetromino.rotate_z_forward()
        elif keyboard.is_pressed('d'):
            self.current_tetromino.rotate_z_backward()
        elif keyboard.is_pressed('up'):
            self.current_tetromino.move_forward()
        elif keyboard.is_pressed('down'):
            self.current_tetromino.move_backward()
        elif keyboard.is_pressed('left'):
            self.current_tetromino.move_left()
        elif keyboard.is_pressed('right'):
            self.current_tetromino.move_right()
        elif keyboard.is_pressed('space'):
            self.drop()
        
    def step(self):
        """
        Moves active tetronimo down by one timestep. Checks if active tetromino has reached the bottom 
        and, if so, puts it in the board and switches to a new tetromino. If it has not reached the
        bottom lets it fall one.
        """
        if self.current_tetromino.can_fall():
            self.current_tetromino.fall()
        else:
            pieces = self.current_tetromino.cube_locations()
            self.cube[pieces[:, 0], pieces[:, 1], pieces[:, 2]] = 1
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
            for _ in range(4):
                time.sleep(0.25)
                self.process_user_action()
            
            if self.is_step_possible():
                self.step()
            else:
                break
                
        self.trigger_game_over()
            
    def trigger_game_over(self):
        """
        A game-over animation and reset of the game board 
        """
        print("Game Over")