#!/usr/bin/env python3

__author__ = 'Cameron Lowell Palmer'

import random
import math

numExamples = 100
lowerLimit = 0
upperLimit = 20
roundNumber = True

worksheet_header = '''\
\\documentclass{article}
\\usepackage[utf8]{inputenc}
\\usepackage[margin=2cm]{geometry}
\\usepackage{longtable}

\\title{Subtraction with 2-digit numbers}
\\date{}

\\begin{document}
\\pagenumbering{gobble}
'''

worksheet_footer = '''\
\\end{document}
'''

problems_header = '''\
\\maketitle
\\section*{Problems}
\\renewcommand\\arraystretch{3.0}

\\setlength\\LTleft{0pt}
\\setlength\\LTright{0pt}
\\begin{longtable}{@{\\extracolsep{\\fill}}l l@{}}
'''

problem_left_sign_right_format = '\hline $$ \huge %d%s%d= $$ \\\\[48pt]'

problems_footer = '''\
\\hline
\\end{longtable}
'''

d = []
d.append(worksheet_header)
d.append(problems_header)
for x in range(1, numExamples):
    theX = random.randrange(lowerLimit, upperLimit)
    if roundNumber:
        theY=random.randrange(math.ceil(theX/10.0+lowerLimit/10),math.ceil((theX+upperLimit)/10))*10-theX
    else:
        theY=random.randrange(lowerLimit, upperLimit)

    d.append(problem_left_sign_right_format % (theX, '-', theY) + '\n')
d.append(problems_footer)
d.append(worksheet_footer)

f = open('arithmetic.tex', 'w')
f.write(''.join(d))
f.flush()
f.close()
