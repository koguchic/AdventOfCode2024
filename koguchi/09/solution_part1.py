


with open('input.txt', 'r') as f:
# with open('test.txt', 'r') as f:
    disk_maps = f.readlines()

FREE_SPACE = '.'


disk_maps = [disk_map.strip() for disk_map in disk_maps]

for disk_map in disk_maps:

    id_number = 0
    output = []

    # First number is a block-file
    is_block = True
    # print(f'\n{disk_map}')

    for x in disk_map:
        x = int(x)
        if is_block:
            for i in range(x):
                output.append(id_number)
            id_number += 1
            is_block = False
        else:
            for i in range(x):
                output.append(FREE_SPACE)
            is_block = True

    # print(''.join([str(o) for o in output]))

    # Reorder
    left = 0
    right = len(output) - 1

    while left < right:
        # print(''.join(output))
        if output[left] != FREE_SPACE:
            left += 1
        elif output[right] == FREE_SPACE:
            right -= 1
        else:
            output[left], output[right] = output[right], output[left]
            left += 1
            right -= 1


    # print(''.join([str(o) for o in output]))
    answer = 0
    for i, c in enumerate(output):
        if c != FREE_SPACE:
            answer += (i * c)

    print(answer) # 6421128769094

