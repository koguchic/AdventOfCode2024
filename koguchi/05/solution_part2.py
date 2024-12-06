from collections import defaultdict


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


updates = []
for update in u:
    updates.append([int(c) for c in update.split(',')])


incorrectly_ordered_updates = []
for update in updates:
    children = set()
    for i, page in enumerate(update):

        if i == 0:
            children = {child for child in rule_book[page]}
            continue

        if page in children:
            children = set()
            children = {child for child in rule_book[page]}
            # print(f'page {page} - {children}')

        else:
            incorrectly_ordered_updates.append(update)
            break

corrected_updates = []
for update in incorrectly_ordered_updates:
    order = []
    for i, current_page in enumerate(update):
        if i == 0:
            order.append(current_page)
            continue

        for j, p in enumerate(reversed(order)):
            if current_page in rule_book[p]:
                order = order[:len(order)-j] + [current_page] + order[len(order)-j:]
                break
        else:
            order = [current_page] + order

    corrected_updates.append(order)

total = 0
for update in corrected_updates:
    middle_page = update[len(update)//2]
    total += middle_page

print(total)

