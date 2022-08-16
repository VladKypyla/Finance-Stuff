from math import *

def slice(symb, val, ang):
    for i in range(len(val)):
        if val[i] * 360 >= ang:
            return symb[i]
        else:
            ang -= val[i] * 360
    return " "

def pie(symb, val, r):
    for i in range(2*r+1):
        for j in range(2*r+1):
            x = j-r
            y = r-i
            if x ** 2 + y ** 2 <= r ** 2+1:
                ang = degrees(atan2(y, x)) % 360
                color = slice(symb, val, ang)
                print(color, end=color)
            else:
                print(" ", end=" ")
        print()

pie("R#O", [0.30,0.45,0.25], 10)
