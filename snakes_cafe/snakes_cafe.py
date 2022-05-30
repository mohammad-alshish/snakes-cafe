menu = {
  'Wings': 0,
  'Cookies': 0,
  'Spring Rolls': 0,
  'Salmon': 0,
  'Steak': 0,
  'Meat Tornado': 0,
  'A Literal Garden': 0,
  'Ice Cream': 0,
  'Cake': 0,
  'Pie': 0,
  'Coffee': 0,
  'Tea': 0,
  'Unicorn Tears': 0
}

welcome = """*************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
----------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts 
----------
Ice Cream
Cake
Pie

Drinks
----------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************
"""
print(welcome)

while 1:
  user_input = input('> ')
  if user_input == 'quit':
    break
  elif user_input in menu:
    menu[user_input] += 1
  else:
    print('\n** Please enter an item on the menu! ** \n')
  for key, val in menu.items():
    if val == 1:
      print('** 1 order of ' + key + ' has been added to your meal **')
    elif val > 1:
      print('** ' + str(val) + ' orders of ' + key + ' have been added to your meal **')
    else:
      continue