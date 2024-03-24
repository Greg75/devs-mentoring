import random


# ---------- Exercise number 1 ----------
# print('Exercise number 1')
# list_a = [1, 2, 'g', 5.7]
# list_b = ['k', 'True', 2, 3.4]
#
# is_common = False
#
# for element_a in list_a:
#     for element_b in list_b:
#         if element_a == element_b:
#             is_common = True
#
# if is_common:
#     print('At least one common element in both lists.')
# else:
#     print('No common elements in the lists.')


# ---------- Exercise number 2 ----------
# print('Exercise number 2')
# random_numbers = {random.randint(5, 120) for _ in range(15)}
# random_numbers_evens_removed = {num for num in random_numbers if num % 2 != 0}
#
# print(f'All random numbers: {random_numbers}.')
# print(f'Even numbers removed: {random_numbers_evens_removed}.')


# ---------- Exercise number 3 ----------
# print('Exercise number 3')
# basic = {'a': 3, 'b': 1, 'c': 10, 'd': 15, 'e': 20}
# basic_reversed = {}
#
# for k, v in basic.items():
#     basic_reversed.update({v: k})
#
# print(f'Reversed: {basic_reversed}.')


# ---------- Exercise number 4 ----------
# print('Exercise number 4')
# weather = {}
# while True:
#     city_rain = input('Type city and amount of rain: ')
#     if city_rain == '':
#         break
#     else:
#         city = city_rain.split(' ')[0]
#         rain = int(city_rain.split(' ')[1])
#         if city in weather.keys():
#             updated_rain = weather[city] + rain
#             weather[city] = updated_rain
#         else:
#             weather.update({city: rain})
#
# print()
# print('Final results:')
# for k, v in weather.items():
#     print(f'{k}: {v}')


# ---------- Exercise number 5 ----------
print('Exercise number 5')
final_bill = {}
meals = []
prices = 0

bill_items = [
    ['Tom', 'Calamari', 6.00],
    ['Tom', 'American Hot', 11.50],
    ['Tom', 'Chocolate Fudge Cake', 4.45],
    ['Clare', 'Bruschetta Originale', 5.35],
    ['Clare', 'Fiorentina', 10.65],
    ['Clare', 'Tiramisu', 4.90],
    ['Rich', 'Bruschetta Originale', 5.35],
    ['Rich', 'La Reine', 10.65],
    ['Rich', 'Honeycomb Cream Slice', 4.90],
    ['Rosie', 'Garlic Bread', 4.35],
    ['Rosie', 'Veneziana', 9.40],
    ['Rosie', 'Tiramisu', 4.90],
]

for bill_item in bill_items:
    name = bill_item[0]
    final_bill.update({name: {'meals': meals, 'price': prices}})

names = final_bill.keys()
for name in names:
    meals = []
    prices = 0
    for bill_item in bill_items:
        if bill_item[0] == name:
            meals.append(bill_item[1])
            prices += bill_item[2]

    final_bill[name] = {'meals': meals, 'price': prices}

print(final_bill)
