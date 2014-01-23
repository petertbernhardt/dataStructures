from __future__ import print_function

class recursion:
    def __init__(self):
        # nothing to initialize, return
        return
    
    def writeNums(self, x):
        if x < 1:
            raise Exception("Illegal Argument Exception")
        if x == 1:
            print(x, end='')
        else:
            self.writeNums(x - 1),
            print(", " + str(x), end='')