from collections import Counter

# ---------- Exercise number 1 ----------
print('Exercise number 1')
albums = {
    'The Sensual World': 'Kate Bush',
    'Shaday': 'Ofra Haza',
    'Achtung Baby': 'U2',
    'Aion': 'Dead Can Dance',
    'Invisible Touch': 'Genesis'
}

print(f'All keys: {albums.keys()}')
title = input('Type title of the song: ')
if title in albums.keys():
    print(f'The singer of the "{title}" is "{albums[title]}".')
else:
    print('No data available.')


# ---------- Exercise number 2 ----------
print('Exercise number 2')

albums = {
    'The Sensual World': 'Kate Bush',
    'Shaday': 'Ofra Haza',
    'Achtung Baby': 'U2',
    'Aion': 'Dead Can Dance',
    'Invisible Touch': 'Genesis'
}

while True:
    print()
    print('Collection menu:')
    print('-' * 20)
    print('1. Add a song to the collection.')
    print('2. Delete a song from the collection.')
    print('3. Display all songs from the collection.')
    print('4. Exit the collection.')
    print('-' * 20)
    user_choice = int(input('Type your choice: '))
    if user_choice == 1:
        title = input('Type title of the song to be added: ')
        artist = input('Type artist of the song to be added: ')
        albums.update({title: artist})
    elif user_choice == 2:
        title = input('Type a song title to be deleted: ')
        albums.pop(title)
    elif user_choice == 3:
        print('Your collection: ')
        for title, song in albums.items():
            print(f'Title: {title} - artist: {song}.')
    elif user_choice == 4:
        print('Bye, bye!')
        break
    else:
        print('Incorrect choice. Try again.')
        break


# ---------- Exercise number 3 ----------
print('Exercise number 3')
text = "Once upon a midnight dreary, while I pondered, weak and weary, Over many a quaint and curious volume of " \
       "forgotten lore, While I nodded, nearly napping, suddenly there came a tapping, As of someone gently rapping, " \
       "rapping at my chamber door. This visitor, I muttered, tapping at my chamber door - Only this, and nothing more."

chars = [',', '-', '.']
for char in chars:
    text = text.replace(char, ' ').strip()

text_to_list = text.split(' ')

text_to_dict = {}

for word in text_to_list:
    value = text_to_list.count(word)
    text_to_dict.update({word: value})

print(text_to_dict)


# ---------- Exercise number 4 ----------
print('Exercise number 4')
birds_dict = {
    'kos': 'Turdus merula',
    'wilga': 'Oriolus oriolus',
    'rudzik': 'Erithacus rubecula',
    'kukulka': 'Cuculus canorus',
    'pleszka': 'Phoenicurus phoenicurus',
    'bogatka': 'Parus major',
    'drozd': 'Turdus philomelos',
    'zieba': 'Fringilla coelebs',
    'dzwoniec': 'Chloris chloris',
    'szczygiel': 'Carduelis carduelis',
    'szpak': 'Sturnus vulgaris',
    'kopciuszek': 'Phoenicurus ochruros'
}

text = 'W polowie maja, juz przed wschodem slonca, o trzeciej zaczyna spiewac drozd, po nim rudzik, a chwile pozniej ' \
       'kos. Pol godziny pozniej odzywa sie kukulka. Zaraz po niej budzi sie bogatka. Wraz ze wschodem slonca, ' \
       'o czwartej godzinie, swoj koncert rozpoczynaja pleszka i zieba. Dwadziescia minut pozniej i wilga akcentuje ' \
       'swoja obecnosc wysoko w koronach drzew. Jeszcze pozniej swoje trzy grosze dodaje szpak, a tuz po nim ' \
       'kopciuszek. Najwiekszymi spiochami w tej ferajnie okazuja sie byc dzwoniec i szczygiel.'

text_to_list = text.split(' ')
text_with_latin_names = []
alphanumeric_character = ''

for word in text_to_list:
    if word in birds_dict.keys():
        word += f' ({birds_dict[word]})'
        text_with_latin_names.append(word)

    elif word[:-1] in birds_dict.keys():
        no_alphanumeric_character_word = word[:-1]

        if word[-1] == ',':
            alphanumeric_character = ','
        elif word[-1] == '.':
            alphanumeric_character = '.'

        no_alphanumeric_character_word += f' ({birds_dict[no_alphanumeric_character_word]}){alphanumeric_character}'
        text_with_latin_names.append(no_alphanumeric_character_word)

    else:
        text_with_latin_names.append(word)

print(' '.join(text_with_latin_names).strip())


# ---------- Exercise number 5 ----------
print('Exercise number 5')
numbers_dict = {}
number = int(input('Type any integer number n: '))
for n in range(1, number + 1):
    numbers_dict.update({n: n * n})

print(numbers_dict)


# ---------- Exercise number 6 ----------
print('Exercise number 6')
answer = 'Kluczami w słownikach mogą być tylko i wyłącznie elementy niemutowalne, czyli takich typów jak: ' \
         'string, integer, float, boolean, tuple. Natomiast elementy, które są mutowalne, czyli typu: słownik, lista ' \
         'NIE MOGĄ BYĆ kluczami w słowniku. Kolejnym ograniczeniem jest to, że klucze nie mogą być powtarzalne.'


# ---------- Exercise number 7 ----------
print('Exercise number 7')
lovers = {1: 'Rahima', 2: 'Alishba', 3: 'Fizza'}
friends = {4: 'Bilal', 5: 'Arbab', 6: 'Shahzor'}

first_dict = {}
second_dict = {}

print()
print('Add inputs to the first dictionary: ')
while True:
    key = input('Type key: ')
    value = input('Type value: ')
    first_dict.update({key: value})
    is_continue = input('Do you want to add next key - value pair? (y/n): ')
    if is_continue == 'y':
        continue
    elif is_continue == 'n':
        break
    else:
        print('Incorrect choice.')

print()
print('Add inputs to the second dictionary: ')
while True:
    key = input('Type key: ')
    value = input('Type value: ')
    second_dict.update({key: value})
    is_continue = input('Do you want to add next key - value pair? (y/n): ')
    if is_continue == 'y':
        continue
    elif is_continue == 'n':
        break
    else:
        print('Incorrect choice.')

print()
print('Concatenated dictionaries:')
first_dict.update(second_dict)
print(first_dict)


# ---------- Exercise number 8 ----------
print('Exercise number 8')
data_dict = {
    "V": "S001",
    "VI": "S002",
    "VII": "S001",
    "VIII": "S005",
    "IX": "S005",
    "X": "S009",
    "XI": "S007"
}

c = Counter(data_dict.values())
unique_items = [k for k, v in c.items() if v == 1]
print(f'Unique values in the dictionary: {unique_items}')
