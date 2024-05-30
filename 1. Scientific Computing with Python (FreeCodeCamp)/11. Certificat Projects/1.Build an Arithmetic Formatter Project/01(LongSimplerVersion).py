def arithmetic_arranger(problems, show_answers = False):
    arranged_problem = []
    first_line = ''
    second_line = ''
    third_line =  ''
    fourth_line = '\n'
    column = '    '
    first = ''

    if len(problems) > 5:
        return 'Error: Too many problems.'
        
    for problem in problems:
        number1 = problem.split(' ')[0]
        sign = problem.split(' ')[1]
        number2 = problem.split(' ')[2]
        if sign == '/' or sign == '*':
            return "Error: Operator must be '+' or '-'."
        elif not (number1.isnumeric() and number2.isnumeric()):
            return 'Error: Numbers must only contain digits.'
        elif len(number1) > 4 or len(number2) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        if len(number1) == 4:
            third_line += '------    '
            if len(number2) == 4:
                first_line += f'  {number1}'
                second_line += f'{sign} {number2}'

            elif len(number2) == 3:
                first_line += f'  {number1}    '
                second_line += f'{sign}   {number2}'
            elif len(number2) == 2:
                first_line += f'  {number1}'
                second_line += f'{sign}    {number2}'
            elif len(number2) == 1:
                first_line += f'  {number1}'
                second_line += f'{sign}    {number2}'

        elif len(number1) == 3:  
            if len(number2) == 4:
                first_line += f'     {number1}'
                second_line += f'{sign} {number2}'
                third_line += '------    '
            elif len(number2) == 3:
                first_line += f'  {number1}'
                second_line += f'{sign} {number2}'
                third_line += '-----    '
            elif len(number2) == 2:
                first_line += f'  {number1}'
                second_line += f'{sign}  {number2}'
                third_line += '-----    '
            elif len(number2) == 1:
                first_line += f'  {number1}'
                second_line += f'{sign}   {number2}'
                third_line += '-----    '

        elif len(number1) == 2:
            if len(number2) == 4:
                first_line += f'     {number1}'
                second_line += f'{sign} {number2}'
                third_line += '------    '
            elif len(number2) == 3:
                first_line += f'   {number1}'
                second_line += f'{sign} {number2}'
                third_line += '-----    '
            elif len(number2) == 2:
                first_line += f'  {number1}'
                second_line += f'{sign} {number2}'
                third_line += '----    '
            elif len(number2) == 1:
                first_line += f'  {number1}'
                second_line += f'{sign}  {number2}'
                third_line += '----    '
        
        elif len(number1) == 1:  
            if len(number2) == 4:
                first_line += f'     {number1}'
                second_line += f'{sign} {number2}'
                third_line += '------    '
            elif len(number2) == 3:
                first_line += f'    {number1}'
                second_line += f'{sign} {number2}'
                third_line += '-----    '
            elif len(number2) == 2:
                first_line += f'   {number1}'
                second_line += f'{sign} {number2}'
                third_line += '----    '
            elif len(number2) == 1:
                first_line += f'  {number1}'
                second_line += f'{sign} {number2}'
                third_line += '---    ' 
        first_line += column
        second_line += column

        if show_answers:
            if sign == '-':
                result = int(number1) - int(number2)
                if len(str(result)) == 5:
                    fourth_line += f' {result}    '
                if len(str(result)) == 4:
                    fourth_line += f' {result}    '    
                if len(str(result)) == 3:
                    fourth_line += f' {result}    '
                if len(str(result)) == 2:
                    fourth_line += f'    {result}    '
                if len(str(result)) == 1:
                    fourth_line += f'     {result}    '

            elif sign == '+': 
                result = int(number1) + int(number2)
                if len(str(result)) == 5:
                    fourth_line += f' {result}    '
                if len(str(result)) == 4:
                    fourth_line += f' {result}    '    
                if len(str(result)) == 3:
                    fourth_line += f'  {result}    '
                if len(str(result)) == 2:
                    fourth_line += f'  {result}    '
                if len(str(result)) == 1:
                    fourth_line += f'     {result}    '
        else:
            fourth_line = ''

    first = first_line.lstrip('\n').rstrip()

    arranged_problem = f'{first_line.rstrip()}\n{second_line.rstrip()}\n{third_line.rstrip()}{fourth_line.rstrip()}'
    return arranged_problem


print(f'\n{arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True)}')
