from math import prod


# def get_inputs(filename='input.txt'):
def get_inputs(filename='test.txt'):

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


inputs = get_inputs()


answer = 0
for target, sequence in inputs.items():
    print(f"{'*' * 20}\n \033[93m{target:,}\033[0m {sequence} \n{'*' * 20}")

    
    upper_triangular = sequence[0] + sequence[1]
    lower_triangular = sequence[0] * sequence[1]

    if len(sequence) == 2:
        if target in [upper_triangular, lower_triangular]:
            print(f'\033[92m{"FOUND!"}\033[0m {target:,}: {sequence}\n\n')
            answer += target
        else:
            print(f'\033[91m{"NOPE"}!\033[0m\n\n')
        continue

    print(f'\nStarting at: {upper_triangular:,} & {lower_triangular:,}')
    for start in range(2, len(sequence)):

        s = sum(sequence[start:]) + upper_triangular
        p = prod(sequence[start:]) * lower_triangular

        # if target > p and start == 2:
        #     # Early exit if target is just too large because full product is the upper bound
        #     print(f'Breaking early, maximum product is {p:,}')
        #     print(f'\033[91m{"NOPE"}!\033[0m\n\n')
        #     break

        print(f'Rest sum {s:,}, Rest prod {p:,}')

        if target in [s, p]:
            print(f'\033[92m{"FOUND!"}\033[0m {target:,}: {sequence}\n\n')
            answer += target
            break

        else:
            val = sequence[start]
            # print(f'\nNext Term is {val:,}')
            print(f'\nNext Term is \033[94m{val:,}\033[0m')
            print(f'Curr iter {upper_triangular:,} {lower_triangular:,}')
            upper_triangular, lower_triangular = lower_triangular + val, upper_triangular * val
            print(f'Next iter {upper_triangular:,} {lower_triangular:,}')
    else:
        if target in [upper_triangular, lower_triangular]:
            print(f'\033[92m{"FOUND!"}\033[0m {target:,}: {sequence}\n\n')
            answer += target

        else:
            print(f'\033[91m{"NOPE"}!\033[0m\n\n')


print(f'Answer: {answer:,}') # 8,401,132,154,762
