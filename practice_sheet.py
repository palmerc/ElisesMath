#!/usr/bin/env python3

import random
import math

numExamples = int(input('How many examples you would like to produce?'))
#check if numExamples >0 and <100
if numExamples < 1 or numExamples > 100:
    print('Number of examples must be in range from 1 to 100. 15-30 examples are recommended.')
    exit()

theSign = input('What action would you like to practice? +/-')
if theSign != '+' and theSign != '-' :
    print('Wrong sign is provided')
    exit()

lowerLimit = int(input('You want to practice with numbers from '))
upperLimit = int(input('to '))
if lowerLimit >= upperLimit:
    print('Wrong range was provided. From must be lower number than To.')
    exit()

roundNumber="N"
resultLimit = int(input('Do you wish result to be under (enter 0 if no total limit required)'))
if resultLimit != 0 and resultLimit <= upperLimit:
    print('Result must be higher than upper limit of your numbers range.')
    exit()


if theSign == "+":
    roundNumber = input('Do you want sum to add up to round number? Type Y for Yes and N for No')
    if roundNumber != 'Y' and roundNumber != 'N':
        print('Wrong input provided. You must enter either Y or N.')
        exit()

fileName = input('Provide file name without extension:')

f = open(f'{fileName}.txt', 'w+')
f.write('Math practice\n\n')

for x in range(1, numExamples):
    theX = random.randrange(lowerLimit, upperLimit)
    theResultLowerLimit = theX + lowerLimit
    if resultLimit == 0 :
        theResultUpperLimit = theX + upperLimit
    else:
        theResultUpperLimit = min(theX + upperLimit, resultLimit)
    theResult = random.randrange(theResultLowerLimit, theResultUpperLimit)

    if roundNumber == 'Y':
        theResult=math.ceil(theResult / 10.0) * 10

    theY = theResult - theX

    if theSign == '+':
        example = f'{theX} + {theY}'
    else:
        example = f'{theResult} - {theY}'

    f.write(f'{example} =\n\n')

f.close()
