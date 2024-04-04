import itertools


def read_talks():
    with open('text.txt', 'r', encoding="utf-8") as file:
        arr = file.readlines()

    res = ''

    for i in arr:
        res = f'{res}{i}'

    result = ''

    for i in res:
        if i != '\n':
            result = f'{result}{i}'
        else:
            result = f'{result} '

    return result


def enumeration(n):
    n = str(n)
    x = f'\nВариант с числом "{n}":\n'

    global line

    while len(line) % 6 != 0:
        line = f'{line} '

    for i in range(0, len(line), 6):
        x = (f'{x}{line[i + int(n[0])]}{line[i + int(n[1])]}{line[i + int(n[2])]}'
             f'{line[i + int(n[3])]}{line[i + int(n[4])]}{line[i + int(n[5])]}')

    return f'{x}'


line = read_talks()
combination_options = []
number_of_capital_letters: int = 0

for i in range(6):
    if line[i] == line[i].upper():
        number_of_capital_letters += 1

if number_of_capital_letters == 1:
    key_0 = 0
    for i in range(6):
        if line[i] == line[i].upper():
            key_0 = i

    perms = itertools.permutations('12345', 5)
    perms = [''.join(p) for p in perms if p[0] != '0']

    for i in range(len(perms)):
        pr = f'{perms[i]}'
        print(pr)
        for j in range(len(pr)):
            if pr[j] == str(key_0):
                pr = f'{pr[:j]}0{pr[j+1:]}'
        perms[i] = f'{key_0}{pr}'
        print(perms[i], '\n')

else:
    perms = itertools.permutations(range(6), 6)
    perms = [''.join(map(str, p)) for p in perms]

perms = sorted(perms)
for i in range(len(perms)):
    print(f'{i+1}. {enumeration(perms[i])}\n')

x = input('\n\n\nВведите шестизначное число, в соответствии с которым нужно произвести сортировку\n'
          'Для проверки варианта 20 введите "034125": ')
print(f'\nИтоговое решение — в{enumeration(x)[2:]}')
