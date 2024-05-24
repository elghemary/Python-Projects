def arithmetic_arranger(problems, show_answers=True):
    problem2 = []

    if len(problems) > 5:
            return 'Error: Too many problems.'

    for problem in problems:
        number1 = problem.split(' ')[0]
        sign = problem.split(' ')[1]
        number2 = problem.split(' ')[2]
        problem2.append([number1,sign,number2])

        if sign == '/' or sign == '*':
            return "Error: Operator must be '+' or '-'."
        elif not (number1.isnumeric() and number2.isnumeric()):
            return 'Error: Numbers must only contain digits.'
        elif len(number1) > 4 or len(number2) > 4:
            return 'Error: Numbers cannot be more than four digits.'
    return problems

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')

# TO CONTINUUUUUUE
