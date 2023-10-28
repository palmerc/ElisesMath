#!/usr/bin/env python3

__author__ = 'Cameron Lowell Palmer'

import numpy as np

document_header = '''
\\documentclass[letter,20pt]{extarticle}
\\usepackage{amsmath,multicol}
\\usepackage[margin=1.0in]{geometry}

\\begin{document}
\\pagenumbering{gobble}
'''

equation = '''
\\begin{equation*}
\\begin{array}{c}
\\phantom{\\timesTOP_PADDING}TOP\\\\
\\underline{\\times\\phantom{BOTTOM_PADDING}BOTTOM}\\\\
\\end{array}
\\end{equation*}
'''

solved = '''
\\begin{equation*}
\\begin{array}{c}
\\phantom{\\timesTOP_PADDING}TOP\\\\
\\underline{\\times\\phantom{BOTTOM_PADDING}BOTTOM}\\\\
\\phantom{\\timesTOP_RESULT_PADDING}TOP_RESULT\\\\
\\underline{\\phantom{\\timesBOTTOM_RESULT_PADDING_LEFT}BOTTOM_RESULT\\phantom{BOTTOM_RESULT_PADDING_RIGHT}}\\\\
\\phantom{\\timesANSWER_PADDING}ANSWER
\\end{array}
\\end{equation*}
'''

document_footer = '''
\\end{document}
'''

number_of_problems = 16
padding_character = '0'
characters_per_line = 5
columns_per_line = 4

sections = []
sections.append(document_header)

problems = []
for count in range(0, number_of_problems):
    top = np.random.randint(10, 99)
    bottom = np.random.randint(10, 99)
    problem = [top, bottom]
    problems.append(problem)

questions_header = '''
\\section*{Questions}
\\begin{multicols}{COLUMNS_PER_LINE}
'''
questions_header = questions_header.replace('COLUMNS_PER_LINE', str(columns_per_line), 1)
sections.append(questions_header)

equations = []
for count in range(0, number_of_problems):
    [top, bottom] = problems[count]

    top_string = str(top)
    bottom_string = str(bottom)
    top_padding = characters_per_line - len(top_string)
    top_padding_string = padding_character * top_padding
    bottom_padding = characters_per_line - len(bottom_string)
    bottom_padding_string = padding_character * bottom_padding

    updated_equation = equation
    updated_equation = updated_equation.replace('TOP_PADDING', top_padding_string)
    updated_equation = updated_equation.replace('BOTTOM_PADDING', bottom_padding_string)
    updated_equation = updated_equation.replace('TOP', top_string)
    updated_equation = updated_equation.replace('BOTTOM', bottom_string)
    equations.append(updated_equation)
    equations.append('\\vspace{20 mm}')


sections.append('\n'.join(equations))

questions_footer = '''
\\end{multicols}
'''
sections.append(questions_footer)

answers_header = '''
\\pagebreak
\\section*{Answers}
\\begin{multicols}{COLUMNS_PER_LINE}
'''
answers_header = answers_header.replace('COLUMNS_PER_LINE', str(columns_per_line), 1)
sections.append(answers_header)

solved_equations = []
for count in range(0, number_of_problems):
    [top, bottom] = problems[count]

    top_string = str(top)
    bottom_string = str(bottom)
    top_result = int(bottom_string[1]) * top
    top_result_string = str(top_result)
    bottom_result = int(bottom_string[0]) * top
    bottom_result_string = str(bottom_result)
    answer = top * bottom
    answer_string = str(answer)

    top_padding = characters_per_line - len(top_string)
    top_padding_string = padding_character * top_padding
    bottom_padding = characters_per_line - len(bottom_string)
    bottom_padding_string = padding_character * bottom_padding

    top_result_padding = characters_per_line - len(top_result_string)
    top_result_padding_string = padding_character * top_result_padding

    bottom_result_padding_left = characters_per_line - len(bottom_result_string) - 1
    bottom_result_padding_left_string = padding_character * bottom_result_padding_left

    bottom_result_padding_right = 1
    bottom_result_padding_right_string = padding_character * bottom_result_padding_right
    answer_padding = characters_per_line - len(answer_string)
    answer_padding_string = padding_character * answer_padding

    updated_equation = solved
    updated_equation = updated_equation.replace('TOP_RESULT_PADDING', top_result_padding_string, 1)
    updated_equation = updated_equation.replace('BOTTOM_RESULT_PADDING_LEFT', bottom_result_padding_left_string, 1)
    updated_equation = updated_equation.replace('BOTTOM_RESULT_PADDING_RIGHT', bottom_result_padding_right_string, 1)
    updated_equation = updated_equation.replace('TOP_PADDING', top_padding_string, 1)
    updated_equation = updated_equation.replace('BOTTOM_PADDING', bottom_padding_string, 1)
    updated_equation = updated_equation.replace('TOP_RESULT', top_result_string, 1)
    updated_equation = updated_equation.replace('BOTTOM_RESULT', bottom_result_string, 1)
    updated_equation = updated_equation.replace('TOP', top_string, 1)
    updated_equation = updated_equation.replace('BOTTOM', bottom_string, 1)
    updated_equation = updated_equation.replace('ANSWER_PADDING', answer_padding_string, 1)
    updated_equation = updated_equation.replace('ANSWER', answer_string)
    solved_equations.append(updated_equation)
sections.append('\n'.join(solved_equations))

answers_footer = '''
\\end{multicols}
'''
sections.append(answers_footer)
sections.append(document_footer)

file = open('worksheet.tex', 'w')
file.write('\n'.join(sections))
file.close()
