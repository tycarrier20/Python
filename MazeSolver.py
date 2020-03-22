# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 11:19:56 2018

@author: sport
"""

# create maze here
# S = starting point
# F = endpoint
# + = maze walls
# . = maze path 

maze1 = """
+S+++++++++++++++++
+.+...............+
+.+++++++++++++++.+
+...............+.+
+.+.+.+++++++++.+.+
+.+.+.+.........+.+
+.+.+++++++++++.+.+
+.+.+...........+.+
+.+.+.+++++++++++.+
+.+.+...........+.+
+.+.+++++++++++.+.+
+.+.+...........+.+
+.+.+++++++++++++.+
+.+.............+.+
+.+++++++++++++.+.+
+...............+.+
+.+.+++++++++++.+.+
+.+.+...........+.+
+.+.+++++++++++++.+
+.+...............+
+.+++++++++++++++++
+.................+
+.+++++++++++++++.+
+...............+.+
+++++++++++++++++F+
"""

#these variables portray all significant locations and moves within the maze

PATH = "."
START = "S"
FINISH = "F"
VISITED = "-"
SOLUTION = "0"

#this class identifies the maze solver itself

class mazeSolver():
    
#these functions make a grid for the maze so it is able to be iterated
    
    def __init__(self, maze1):
        self.mazeSolver = [list(row) for row in maze1.splitlines()]
        self.start_y = [row.count(START) for row in self.mazeSolver].index(1)
        self.start_x = self.mazeSolver[self.start_y].index(START)
        
    def __repr__(self):
        return "\n".join("".join(row) for row in self.mazeSolver)

#this function iterates the maze

    def solve(self, x=None, y=None):
        if x == None:
            x,  y = self.start_x, self.start_y
        if self.mazeSolver[y][x] in (PATH, START):
            self.mazeSolver[y][x] = VISITED
            if (self.solve(x+1, y) or self.solve(x-1, y) or
                self.solve(x, y+1) or self.solve(x, y-1)):
                self.mazeSolver[y][x] = SOLUTION
                return True
        elif self.mazeSolver[y][x] == FINISH:
            return True
        return False

#this function returns the solved maze once the solution is found

if __name__ == "__main__":
    mazeSolver = mazeSolver(maze1)
    if mazeSolver.solve():
        print (mazeSolver)