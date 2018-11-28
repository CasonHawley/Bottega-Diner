reply = input('Welcome to Kona Bar and Grill')

seating = input('Would you like the bar or booth?')
if seating == 'bar':
  print('ok great, just a heads up its by one get one 50% off')
elif seating == 'booth':
  print('Ok right this way!')

bar_menu = input('Would you like to see a menu?')
if bar_menu == 'yes':
  print('perfect, take your time and read through out options')
elif bar_menu == 'drinks':
  print('Ahh, something a little stronger i see.')

booth_menu = input('What can i get for you today?')
if booth_menu == 'Dinner':
  print('Great, our specials for today is the Cheeseburger')
elif booth_menu == 'other':
  print('We have a great assortment of drinks and appetizers for the taking.')

ready = input('Are you ready? Or do you need a few minutes?')
if ready == 'yes':
  print('ok, what can i get ya?')
elif ready == 'no':
  print('ok, ill come back and check on you')


entree_menu = {
  'Cheeseburger': '7.00',
  'Tacos': '2.00',
  'Chicken Salad': '7.00'
}

side_menu = {
  'Beer': '2.00',
  'Rum': '4.00',
  'Whiskey': '4.00'
}
print('Entrees:')
for item, price in entree_menu.item():
  print(f'{item}: ${price}0')
print("___________")
print('Side Menu:')
for item, price in side_menu.item():
  print(f'{items}: ${price}0')

print("-----------------")
print('TOTAL:')
print(f'${order_total}0')
