from collections import defaultdict
from pprint import pprint


# with open('test.txt', 'r') as f:
with open('input.txt', 'r') as f:
    x = f.readlines()

r = []
u = []
for token in x:
    token = token.strip()
    if not token:
        continue

    if '|' in token:
        r.append(token)
    else:
        u.append(token)

rule_book = defaultdict(list)
for rule in r:
    a, b = rule.split('|')
    rule_book[int(a)].append(int(b))


pprint(rule_book)

# {29: [13],
#  47: [53, 13, 61, 29],
#  53: [29, 13],
#  61: [13, 53, 29],
#  75: [29, 53, 47, 61, 13],
#  97: [13, 61, 47, 29, 53, 75]})

# 75,47,61,53,29
# 97,61,53,29,13
# 75,29,13
# 75,97,47,61,53
# 61,13,29
# 97,13,75,29,47

updates = []
for update in u:
    updates.append([int(c) for c in update.split(',')])


correctly_ordered_updates = []
for update in updates:
    children = set()
    print(f'\n\nUpdate: {update}')
    for i, page in enumerate(update):

        if i == 0:
            children = {child for child in rule_book[page]}
            continue

        if page in children:
            children = set()
            children = {child for child in rule_book[page]}
            print(f'page {page} - {children}')

        else:
            break
    else:
        print(update)
        correctly_ordered_updates.append(update)

total = 0
for update in correctly_ordered_updates:
    middle_page = update[len(update)//2]
    total += middle_page

print(total)
