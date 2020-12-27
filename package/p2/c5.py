# import file
import sys, os
DIR_PATH = os.path.dirname(os.path.abspath(__file__))
DIR_PATH = DIR_PATH[:-1] + "1"
sys.path.insert(0, DIR_PATH)
import c1

# create class definition
class C5():
    def __init__(self,x=0,y=0,z=0,u=0):
        self.o = c1.C1(x,y,z,u)

