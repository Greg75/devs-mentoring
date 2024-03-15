# ---------- Exercise number 1 ----------
print('Exercise number 1')
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


# ---------- Exercise number 2 ----------
print('Exercise number 2')
marks = [',', '.', ':', ';', '!', '?']
text = input('Type any statement: ')
stripped_text = ''
for character in text:
    if character not in marks:
        stripped_text += character

print()
print('Tuple part:')
stripped_text_to_tuple = tuple(stripped_text.split(' '))
print(stripped_text_to_tuple)
print(f'Number of words in text: {len(stripped_text_to_tuple)}.')
for word in stripped_text_to_tuple:
    print(word, end=' ')
print()
print(f'First word in the tuple: "{stripped_text_to_tuple[0]}", '
      f'fourth word in the tuple: "{stripped_text_to_tuple[3]}".')

print()
print('Set part:')
stripped_text_to_set = set(stripped_text_to_tuple)
print(f'Number of unique words: {len(stripped_text_to_set)}.')
for word in stripped_text_to_set:
    print(word, end=' ')
print()
print(f'First word in the set: "{list(stripped_text_to_set)[0]}", '
      f'fourth word in the set: "{list(stripped_text_to_set)[3]}".')

print()
if stripped_text_to_tuple[0] == list(stripped_text_to_set)[0] and \
        stripped_text_to_tuple[3] == list(stripped_text_to_set)[3]:
    print('The first and fourth words in tuple and set are the same.')
else:
    print('The first and fourth words in tuple and set are different.')


# ---------- Exercise number 3 ----------
print('Exercise number 3')
author_colors = {'blue', 'green', 'white', 'brown'}
user_colors = set(input('Type any number of your favourite colors separated by space: ').split(' '))

if author_colors == user_colors:
    print('Both colors sets are the same.')
else:
    print(f'Same colors in both sets: {author_colors.intersection(user_colors)}.')
    print(f'Colors chosen only by the user: {user_colors.difference(author_colors)}.')
    print(f'Colors chosen only by the author: {author_colors.difference(user_colors)}.')


# ---------- Exercise number 4 ----------
print('Exercise number 4')
set_limit = int(input('Type any integer number: '))

set_A = {element for element in range(set_limit) if element % 2 == 0}
print(f'Set A: {set_A}.')

set_B = {element for element in range(set_limit) if element % 3 == 2}
print(f'Set B: {set_B}.')

print(f'Sum of sets A and B: {set_A.union(set_B)}.')
print(f'Intersection of sets A and B: {set_A.intersection(set_B)}.')
print(f'Difference between set A and set B: {set_A.difference(set_B)}.')
print(f'Symmetric difference between set A and set B: {set_A.symmetric_difference(set_B)}.')
