

# with open('test_1.txt', 'r') as f:
# with open('test.txt', 'r') as f:
with open('input.txt', 'r') as f:
    x = f.read()
    stones = [int(c) for c in x.split()]


def rule1(stone):
    return 1

def rule2(stone):
    str_stone = str(stone)
    k = len(str_stone) // 2
    return int(str_stone[:k]), int(str_stone[k:])

def rule3(stone):
    return 2024 * stone


num_iters = 25
# num_iters = 6
for iter in range(num_iters):
    print(f'{"*"*80}\n{iter+1} {stones}\n{"*"*80}')
    new_stones = []
    for stone in stones:
        print(f'\n{stone}')
        if stone == 0:
            print('0->1 Rule 1')
            new_stones.append(rule1(stone))
        elif len(str(stone)) % 2 == 0:
            print('Splitting... Rule 2')
            new_stones.extend(rule2(stone))
        else:
            print('Multiplying... Rule 3')
            new_stones.append(rule3(stone))
        # print(new_stones)

    stones = new_stones[:]

print(f'{"*"*80}\n{iter+1} {stones}\n{"*"*80}')
print(f'Answer: {len(stones)}') # Too low: 55312
