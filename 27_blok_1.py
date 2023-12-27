print('\t', end='')
for i in range(1, 11):
    print(i, '\t', end='')
print()

for i in range(1, 11):
    print(i, '\t', end='')
    for j in range(1, 11):
        print(i * j, '\t', end='')
    print()