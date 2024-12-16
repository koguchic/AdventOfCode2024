

with open('input.txt', 'r') as f:
# with open('test.txt', 'r') as f:
    disk_map = f.read().strip()

# print(disk_map)

FREE_SPACE = '.'

def dict_to_string(output):
    out_string = ''
    for d in output:
        k, v = next(iter(d.items()))
        out_string = out_string + (str(k)*v)
    return out_string


def merge_spaces(output):
    # Merge consecutive free space blocks
    i = 0
    while i < len(output) - 1:
        block_type1, size1 = next(iter(output[i].items()))
        block_type2, size2 = next(iter(output[i + 1].items()))
        if block_type1 == FREE_SPACE and block_type2 == FREE_SPACE:
            output[i][FREE_SPACE] = size1 + size2
            del output[i + 1]
        else:
            i += 1

    output[:] = [block for block in output if next(iter(block.values())) > 0]


id_number = 0
output = []

# First number is a block-file
is_block = True
for x in disk_map:
    x = int(x)
    if is_block:
        if x > 0:
            output.append({id_number: x})
        id_number += 1
        is_block = False
    else:
        if x > 0:
            output.append({FREE_SPACE: x})
        is_block = True


# print(output)
# print(dict_to_string(output))

# Find the first file ID(right)
for right in reversed(range(len(output))):
    # print(right)
    block_type, size = next(iter(output[right].items()))
    if block_type != FREE_SPACE:
        break

seen = set()
while right >= 0:
    # print(f'\n{"*"*80}\n{right} {output[right]} -- SEEN {seen}\n{"*"*80}')

    block_type2, size2 = next(iter(output[right].items()))
    if block_type2 in seen:
        # print(f'Already seen {block_type2}! Skipping...')
        right -= 1
        block_type2, size2 = next(iter(output[right].items()))
        # Shift one extra if we hit a 0 space
        if block_type2 == FREE_SPACE:
            right -= 1
        continue
    else:
        print(block_type2)

    # Find first left
    for left in range(right):
        block_type1, size1 = next(iter(output[left].items()))
        if block_type1 != FREE_SPACE:
            continue

        # Left OK, Right OK
        block_type1, size1 = next(iter(output[left].items()))
        block_type2, size2 = next(iter(output[right].items()))

        # print(f'\nBlock: {block_type2} - Size: {size2}')
        # print(f'{left}/{right} -> Block: {block_type1} - Size: {size1}')

        if size2 == size1:
            # print(dict_to_string(output))
            output[left], output[right] = output[right], output[left]
            seen.add(block_type2)

            right -= 1
            block_type2, size2 = next(iter(output[right].items()))

            # Shift one extra if we hit a 0 space
            if block_type2 == FREE_SPACE:
                right -= 1

            merge_spaces(output)
            # print('Fit perfectly!')
            break

        elif size2 < size1:
            # print(dict_to_string(output))
            remaining_memory = size1 - size2
            output[left], output[right] = output[right], output[left]
            output[right][FREE_SPACE] -= remaining_memory
            output = output[:left+1] + [{FREE_SPACE: remaining_memory}] + output[left+1:]
            seen.add(block_type2)

            # Extra insertion of a new element causes right to be in the next pos
            block_type2, size2 = next(iter(output[right].items()))
            # Shift one extra if we hit a 0 space
            if block_type2 == FREE_SPACE:
                right -= 1
                # print(f'Need to shift again. Now at {output[right]} at pos {right}')

            # print('Fit with slack!')
            merge_spaces(output)
            break
        # input()

    else:
        # print(f"Did not move {output[right]}")
        seen.add(block_type2)

        right -= 1
        block_type2, size2 = next(iter(output[right].items()))

        # Shift one extra if we hit a 0 space
        if block_type2 == FREE_SPACE:
            right -= 1
 
    # print(dict_to_string(output))
    # print(output)

# print(output)
# print(dict_to_string(output))

answer = 0
out_string = dict_to_string(output)
idx = 0
for x in output:
    id, size = next(iter(x.items()))
    for i in range(size):
        if id != FREE_SPACE:
            answer += id * idx
        idx += 1

print(f'Answer: {answer}') # Too low: 86,617,297,309 -> 6,448,168,620,520

