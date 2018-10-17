#!/usr/bin/env python

import random 

f = open("math.txt","w+")
print("Math practice")
for x in range(1,31):
    theX=random.randrange(10, 51)
    theY=random.randrange(10, 51)
    f.write(str(theX)+'+'+str(theY)+'='+'\n\n')

f.close()
