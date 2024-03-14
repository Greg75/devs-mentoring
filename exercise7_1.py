colors_list = ['green', 'red', 'blue', 'black', 'purple', 'navy blue', 'blue', 'black', 'black', 'green',
               'lemon yellow', 'navy blue', 'blue', 'indigo', 'green', 'red']

colors_set = set(colors_list)

print(f'Number of the elements in the colors_list: {len(colors_list)}')
print(f'Number of different colors used: {len(colors_set)}')

for color in colors_set:
    print(color)

colors_set.update({'grey'})
print(f'Set with extra color: {colors_set}')

colors_set.discard('indigo')
print(f'Set with deleted color: {colors_set}')
