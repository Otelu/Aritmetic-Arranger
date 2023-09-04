def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    arranged_problems = ""
    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""

    for problem in problems:
        parts = problem.split()
        num1 = parts[0]
        operator = parts[1]
        num2 = parts[2]

        if operator not in ('+', '-'):
            return "Error: Operator must be '+' or '-'."

        if not (num1.isdigit() and num2.isdigit()):
            return "Error: Numbers must only contain digits."

        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."

        width = max(len(num1), len(num2)) + 2
        line1 += num1.rjust(width)
        line2 += operator + num2.rjust(width - 1)
        line3 += '-' * width
        line4 += str(eval(problem)).rjust(width) if show_answers else ' ' * width

        if problem != problems[-1]:
            line1 += '    '
            line2 += '    '
            line3 += '    '
            line4 += '    '

    arranged_problems = "\n".join([line1, line2, line3, line4])

    return arranged_problems
