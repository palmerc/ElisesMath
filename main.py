#!/usr/bin/env python

import random
import math
numExamples=input("How many examples you would like to produce?")
lowerLimit=input("You want to practice adding numbers from ")
upperLimit=input("to ")
roundNumber=raw_input("Do you want sum to add up to round number? Type Y for Yes and N for No")

f = open("math.txt","w+")
f.write("Math practice"+"\n\n")

for x in range(1,numExamples):
    theX = random.randrange(lowerLimit, upperLimit)
    if roundNumber == "Y":
        theY=random.randrange(math.ceil(theX/10.0+lowerLimit/10),math.ceil((theX+upperLimit)/10))*10-theX
    else:
        theY=random.randrange(lowerLimit, upperLimit)

    f.write(str(theX)+'+'+str(theY)+'='+'\n\n')

f.close()
