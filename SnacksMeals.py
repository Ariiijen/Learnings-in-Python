print('Menu:')
print('=====Snacks=====')
print('1. Cheesy Burger Meal')
print('2. Crunchy Chicken Sandwich')
print('3. Jolly Hotdog Meal')

print('\n=====Meals=====')
print('1. Burger Steak')
print('2. Chickenjoy Rice Meal')
print('3. Cornedbeef Breakfast Meal')

menu = input ('\nEnter menu choice (Snacks or Meals): ')
choice = int(input('Choose from the options above (1-3): '))

if menu == 'Snacks':
    if choice == 1:
        print('Your order is Chessy Burger Meal. ^^')
    elif choice == 2:
        print('Your order is Crunchy Chicken Sandwich. ^^')
    elif choice == 3:
        print('Your order is Jolly Hotdog Meal. ^^')
    else:
        print('Invalid Choice. Try again. :<')

if menu == 'Meals':
    if choice == 1:
        print('Your order is Burger Steak. ^^')
    elif choice == 2:
        print('Your order is Chickenjoy Rice Meal. ^^')
    elif choice == 3:
        print('Your order is Cornedbeef Breakfast Meal. ^^')
    else:
        print('Invalid Choice. Try again. :<')
