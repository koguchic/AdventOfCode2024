import itertools


RED = "\033[91m"
GREEN = "\033[92m"
BLUE = "\033[94m"
RESET = "\033[0m"


def color_symbols(s):
    colored_string = s.replace('+', f"{BLUE}+{RESET}")
    colored_string = colored_string.replace('*', f"{BLUE}*{RESET}")
    colored_string = colored_string.replace('|', f"{BLUE}|{RESET}")
    return colored_string


def get_inputs(filename='input.txt'):
# def get_inputs(filename='test.txt'):

    with open(filename, 'r') as f:
        x = f.readlines()

    x = [row.strip() for row in x]

    inputs = {}
    for row in x:
        target, terms = row.split(':')
        target = int(target)
        terms = terms.strip()
        terms = [int(t) for t in terms.split(' ')]
        inputs[target] = terms

    return inputs



def evaluate(format_string, verbose=True):
    if verbose:
        print(f'Evaluating {color_symbols(format_string)}')

    answer = 0
    left = 0
    right = 0
    next_operation = '+'

    while right < len(format_string):
        c = format_string[right]
        if c in ['+', '*', '|']:

            number = int(format_string[left:right])
            if next_operation == '+':
                answer += number
            elif next_operation == '*':
                answer *= number
            elif next_operation == '|':
                answer = eval(str(answer) + str(number))
            else:
                print(f'Unsupported operation {next_operation}')

            next_operation = c
            right += 1
            left = right

        right += 1

    number = int(format_string[left:])
    if next_operation == '+':
        answer += number
    elif next_operation == '*':
        answer *= number
    elif next_operation == '|':
        answer = eval(str(answer) + str(number))
    else:
        print(f'Unsupported operation {next_operation}')

    return answer


inputs = get_inputs()


answer = 0
callibrated = []

for target, terms in inputs.items():
    print(f'\n\n{target}: [{terms}]')
    options = ['+', '*', '|']
    cartesian_product = itertools.product(options, repeat=(len(terms)-1))
    for operators in cartesian_product:

        format_string = str(terms[0])

        for operator, term in zip(operators, terms[1:]):
            format_string += operator + str(term)

        y = evaluate(format_string, False)

        if y == target:
            print(f'{color_symbols(format_string)} = {y}')
            print(f'{GREEN}FOUND{RESET}')
            answer += target
            callibrated.append(target)
            break
    else:
        print(f'{RED}NO SOLUTION{RESET}')

print(f'Answer: {answer} - [{callibrated}]') # 95297119227552

