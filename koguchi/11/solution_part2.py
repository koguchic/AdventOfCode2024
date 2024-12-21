import functools



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


def push(stone):
    if stone == 0:
        out = rule1(stone)
    elif len(str(stone)) % 2 == 0:
        out = rule2(stone)
    else:
        out = rule3(stone)
    return out


# DIY Cache
# memo = {}
# def count_stones_after(stone, steps_left):
#     if (stone, steps_left) in memo:
#         return memo[(stone, steps_left)]
#
#     if steps_left == 0:
#         return 1
#
#     after_blink = push(stone)
#     if isinstance(after_blink, int):
#         count = count_stones_after(after_blink, steps_left-1)
#         # memo[(stone, steps_left)] = count
#         return count
#     else:
#         count = count_stones_after(after_blink[0], steps_left-1) + count_stones_after(after_blink[1], steps_left-1)
#         # memo[(stone, steps_left)] = count
#         return count
#
#     return count

@functools.cache
def count_stones_after(stone, steps_left):
    if steps_left == 0:
        return 1

    after_blink = push(stone)
    if isinstance(after_blink, int):
        count = count_stones_after(after_blink, steps_left-1)
        return count
    else:
        count = count_stones_after(after_blink[0], steps_left-1) + count_stones_after(after_blink[1], steps_left-1)
        return count

    return count


print(sum([count_stones_after(stone, 75) for stone in stones]))
