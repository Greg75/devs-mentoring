import random


# ---------- Exercise number 1 ---------- # Needs clarification!
print('Exercise number 1')
punctuation_marks = [',', '.', ':', ';', '!', '?']
text = input('Type any text: ')
for character in text:
    if character in punctuation_marks:
        text = text.replace(character, '')

text_to_list = text.split(' ')
list_of_indexes = [i for i in range(len(text_to_list))]

text_to_list_reversed = [item for i, item in sorted(zip(list_of_indexes, text_to_list),
                                                    key=lambda x: x[0], reverse=True)]  # Lambda function - how it works?
print(' '.join(text_to_list_reversed))


# ---------- Exercise number 2 ----------
print('Exercise number 2')
results = [12, 1, 45, 76, 50, 23]
correct_results = []
for result in results:
    if result not in range(1, 50):
        correct_results.append(random.randint(1, 49))
        print('I found wrong value. Value successfully replaced.')
    else:
        correct_results.append(result)

print(f'Corrected results: {correct_results}.')


# ---------- Exercise number 3 ----------
print('Exercise number 3')
list1 = ["abc", "def", "ghi", "jkl"]
list2 = [1, 2, 3, 4, 5]
list3 = ["xyz", 1, '2']

lists = [list1, list2, list3]
for i, lst in enumerate(lists):
    print(f'List{i + 1}: {lst}')

print(f'First and fourth element from List1, respectively: {list1[0]}, {list1[3]}.')

list2[1] = list3[1]
print(f'Assigning the element number 2 in list2, value of the element number 2 from list3: {list2}.')

list3_3rd_element_new_value = input('Type new value for 3rd element of list3: ')
list3[2] = list3_3rd_element_new_value
print(f'List3 with new value of 3rd element: {list3}.')

list1.append('word')
print(f'List1 with new element added: {list1}.')

list1.pop(2)
print(f'List1 with removed element with index 2: {list1}.')

print(f'Number of elements in list3: {len(list3)}.')

list1.extend(list3)
print(f'List1 extended of elements from list3: {list1}.')


# ---------- Exercise number 4 ----------
print('Exercise number 4')
friends = []
greetings = ['Hello', 'Good morning', 'Cheers', 'Hi']
while True:
    friend = input('Type name of your friend: ')
    friends.append(friend)
    is_continue = input('Do you want to add another name? (y/n): ')
    if is_continue == 'y':
        continue
    elif is_continue == 'n':
        break
    else:
        print('Invalid choice. Try again later.')

for friend in friends:
    greeting = random.choice(greetings)
    print(f'{greeting} {friend}!')


# ---------- Exercise number 5 ---------- # Needs clarification
print('Exercise number 5')
words = ['and', 'in', 'at', 'under', 'for']
punctuation_marks = [',', '.', ':', ';', '!', '?']
text = input('Type any text: ')
for character in text:
    if character in punctuation_marks:
        text.replace(character, '')

text_to_list = text.split(' ')
text_to_list_with_no_punctuation_marks = []
for word in text_to_list:
    if word.isalpha():
        text_to_list_with_no_punctuation_marks.append(word.lower())
    else:
        text_to_list_with_no_punctuation_marks.append(word[:-1].lower())

print(f'Number of words in text: {len(text_to_list)}.')
if not text.islower():
    print('Words starting with capital letter: ', end='')
    for word in text_to_list:
        if word[0].isupper():
            if word.isalpha():
                print(word, end=' ')
            else:
                print(word[:-1], end=' ')
else:
    print('There is no words starting with the capital letter.')

print()
counter = 0
for word in text_to_list:
    if word.lower() in words:
        print(f'"{word.lower()}" is in the text with index: {text_to_list.index(word)}.')
        counter += 1
if counter == 0:
    print(f'There is no words: {words} in text.')

text_to_list_with_no_punctuation_marks.sort()
print(f'List of all words in the text sorted alphabetically: {text_to_list_with_no_punctuation_marks}.')

unique_words_set = set(text_to_list_with_no_punctuation_marks)
unique_words_list = list(unique_words_set)
unique_words_list.sort()
print(f'List of unique words sorted alphabetically: {unique_words_list}.')
