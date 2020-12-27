# import c1
import sys, os
DIR_PATH = os.path.dirname(os.path.abspath(__file__))
# home/user/..../folder/p2 -> p1
DIR_PATH_P1 = DIR_PATH[:-1] + "1"
sys.path.insert(0, DIR_PATH_P1)
import c1

# class definition
class C4(c1.C1):
    def __init__(self,x=0,y=0,z=0,u=0):
        super().__init__(x,y,z,u)
