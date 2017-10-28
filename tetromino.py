import numpy as np

class Tetromino:
    def __init__(self, block, cube, x, y, z):
        self.block = block
        self.cube = cube
        self.pos = np.array([x,y,z])

    def can_fall(self):
        """
            Given the current state of the cube, determines whether
            the tetromino can fall another step down or if it has stopped.
        """        
        self.pos[2] -= 1
        
        pieces = self.cube_locations()
        
        if not self.is_valid_position() or np.any(self.cube[pieces[:, 0], pieces[:, 1], pieces[:, 2]]):
            self.pos[2] += 1
            return False
        
        self.pos[2] += 1
        return True
    
    def fall(self):
        """
            Drops the tetromino by one level.
        """
        self.pos[2] -= 1
    
    def rotate_x_forward(self):
        """
            Checks if it can rotate the tetromino x axis forward. If it can
            then it does.
        """
        self._do_rotation(np.array([[1, 0, 0], [0, 0, 1], [0, -1, 0]], np.int))
    
    def rotate_x_backward(self):
        """
            Check if it can rotate the tetromino about the x axis
            backward. If it can then it does.
        """
        self._do_rotation(np.array([[1, 0, 0], [0, 0, -1], [0, 1, 0]], np.int))
        
    def rotate_y_forward(self):
        """
            Check if it can rotate the tetromino about the y axis
            forward. If it can then it does.
        """
        self._do_rotation(np.array([[0, 0, -1], [0, 1, 0], [1, 0, 0]], np.int))
    
    def rotate_y_backward(self):
        """
            Check if it can rotate the tetromino about the y axis
            backward. If it can then it does.
        """
        self._do_rotation(np.array([[0, 0, 1], [0, 1, 0], [-1, 0, 0]], np.int))
    
    def rotate_z_forward(self):
        """
            Check if it can rotate the tetromino about the z axis
            forward. If it can then it does.
        """
        self._do_rotation(np.array([[0, 1, 0], [-1, 0, 0], [0, 0, 1]], np.int))
    
    def rotate_z_backward(self):
        """
            Check if it can rotate the tetromino about the z axis
            backward. If it can rotate then it does.
        """
        self._do_rotation(np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]], np.int))
                                 
    def _do_rotation(self, rotation_matrix):
        """
            Try and do the rotation corresponding to the given rotation matrix.
            If that leads to an invalid position, undo the rotation.
        """
        old_block = self.block
        self.block = (rotation_matrix @ self.block.T).T
        
        pieces = self.cube_locations()

        if not self.is_valid_position() or np.any(self.cube[pieces[:, 0], pieces[:, 1], pieces[:, 2]]):
            self.block = old_block

    def move_forward(self):
        """
            Try and move forward. If that leads to an invalid position undo the movement.
        """
        self.pos[0] += 1

        if not self.is_valid_position():
            self.pos[0] -= 1

    def move_backward(self):
        """
            Try and move backward. If that leads to an invalid position undo the movement.
        """
        self.pos[0] -= 1

        if not self.is_valid_position():
            self.pos[0] += 1
        
    def move_left(self):
        """
            Try and move left. If that leads to an invalid position undo the movement.
        """
        self.pos[1] -= 1

        if not self.is_valid_position():
            self.pos[1] += 1

    def move_right(self):
        """
            Try and move right. If that leads to an invalid position undo the movement.
        """
        self.pos[1] += 1

        if not self.is_valid_position():
            self.pos[1] -= 1

    def drop(self):
        while(self.can_fall()):
            self.fall()

    def cube_locations(self):
        """
            Returns the location of the tetromino cubes on the cube.
        """
        return self.block + self.pos
    
    def is_valid_position(self):
        positions = self.cube_locations()
        return np.all((0 <= positions[:, 0:2]) & (positions[:, 0:2] <= 7)) and np.all(positions[:,2] >= 0)
    
    def within_board(self):
        positions = self.cube_locations()
        return np.all((0 <= positions) & (positions <= 7))