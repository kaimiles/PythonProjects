Max_len_of_input = 5
Max_len_of_digits = 6

num1 = []
operator = []
num2 = []
results = []

def Arithmetic_arranger(problems, exit = True):
    problem_input(problems)
    return process_output(exit)

def problem_input(problems):
    assert len(problems) <= Max_len_of_input, 'ERROR: Too many inputs'

    for problem in problems:
        parts = problem.split()

        assert len(parts) == 3, 'ERROR: Too many digits'

        t1 = parts[0]
        op = parts[1]
        t2 = parts[2]

        assert t1.isnumeric() and t2.isnumeric(), 'ERROR: Please input numbers'
        assert len(t1) < Max_len_of_digits and len(t2) < Max_len_of_digits, 'ERROR: Too many digits'
        assert op == '+' or op =='-', 'ERROR: invalid operators'

        num1.append(t1)
        num2.append(t2)
        operator.append(op)
        result = ''
        if op == '+':
            result = int(t1) + int(t2)
        else:
            result = int(t1) - int(t2)

        results.append(result)

def process_output(exit):
    spacer = '  ' * 3
    line1 = ''
    line2 = ''
    dashes = ''
    line3 = ''
    result = ''

    for index in range(len(num1)):
        t1 = num1[index]
        op = operator[index]
        t2 = num2[index]
        result = results[index]
        width = max(len(t1), len(t2))

        line1 += spacer + ' ' + ' ' + t1.rjust(width)
        line2 += spacer + op + ' ' + t2.rjust(width)
        dashes += spacer + '-' * (width + 2)
        line3 += spacer + ' ' + str(result).rjust(width + 1)

    output = line1 + '\n' + line2 + '\n' + dashes + '\n'
    if exit == True:
        output += line3 + '\n'
    print(output)
    return output


Arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", '123 + 456'],True)
