# import file
import sys, os
DIR_PATH = os.path.dirname(os.path.abspath(__file__))
DIR_PATH_P2 = DIR_PATH + "/p2"
DIR_PATH_P1 = DIR_PATH + "/p1"
sys.path.insert(0, DIR_PATH_P2)
sys.path.insert(0, DIR_PATH_P1)
import c4, c5, c2

# run program
print("++++ C2 ++++")
prog2 = c2.C2()
prog2.o.m()
print(prog2.o.x)
print(prog2.o._y)
print(prog2.o.z)

# run program
print("++++ C3 ++++")
prog4 = c4.C4()
prog4.m()
print(prog4.x)
print(prog4._y)
print(prog4.z)

# run program
print("++++ C4 ++++")
prog5 = c5.C5()
prog5.o.m()
print(prog5.o.x)
print(prog5.o._y)
print(prog5.o.z)