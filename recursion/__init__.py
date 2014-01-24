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
            
    def fibonacci(self, x):
        if x == 0:
            return 0
        elif x == 1:
            return 1
        else:
            return self.fibonacci(x - 1) + self.fibonacci(x- 2)
        
    def pow(self, base, power):
        if power != 1:
            return (base * self.pow(base, power - 1))
        else:
            return 1