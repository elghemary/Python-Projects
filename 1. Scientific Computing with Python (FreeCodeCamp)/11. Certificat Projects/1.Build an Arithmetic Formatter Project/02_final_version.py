def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'

    first_line = ''
    second_line = ''
    third_line = ''
    fourth_line = ''
    column_spacing = '    '

    for problem in problems:
        number1, sign, number2 = problem.split()

        if sign not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        if not (number1.isdigit() and number2.isdigit()):
            return 'Error: Numbers must only contain digits.'
        if len(number1) > 4 or len(number2) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        width = max(len(number1), len(number2)) + 2
        top = number1.rjust(width)
        bottom = sign + number2.rjust(width - 1)
        line = '-' * width
        if show_answers:
            if sign == '+':
                result = str(int(number1) + int(number2)).rjust(width)
            else:
                result = str(int(number1) - int(number2)).rjust(width)
            fourth_line += result + column_spacing

        first_line += top + column_spacing
        second_line += bottom + column_spacing
        third_line += line + column_spacing

    if show_answers:
        arranged_problem = f'{first_line.rstrip()}\n{second_line.rstrip()}\n{third_line.rstrip()}\n{fourth_line.rstrip()}'
    else:
        arranged_problem = f'{first_line.rstrip()}\n{second_line.rstrip()}\n{third_line.rstrip()}'

    return arranged_problem


print(f'\n{arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True)}')
