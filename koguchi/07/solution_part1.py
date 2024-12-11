

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


inputs = get_inputs()
answer = 0

for target, terms in inputs.items():
    n = len(terms) - 1 # for n numbers, you do n-1 operations
    num_combinations = 2 ** n

    print(f'\nEnumerating over {num_combinations} choices!')

    for i in range(num_combinations):

        choices = [str(terms[0])]
        x = int(terms[0])

        binary_repr = format(i, f'0{n}b')
        for i, (bit, term) in enumerate(zip(binary_repr, terms[1:])):
            if int(bit) == 0:
                x += term
                choices.append(f'+{term}')
            elif int(bit) == 1:
                x *= term
                choices.append(f'*{term}')
            else:
                print('Wtf, shoulda only been binary')

        if x == target:
            print(f'TARGET: {target} = {"".join(choices)}')
            answer += target
            break


# MENACING TEST CASE THAT SHOULD PASS: 84669705: 851 449 5 801 81
print(f'Answer: {answer}') # 8401132154762

