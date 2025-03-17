while True:
    print('\nMenu:')
    print('======Snacks======')
    print('1. Cheesy Burger Meal | Php 50.00')
    print('2. Crunchy Chicken Sandwich | Php 60.00')
    print('3. Jolly Hotdog Meal | Php 40.00')
    print('4. Exit')
    
    print('\n======Meals======')
    print('1. Burger Steak | Php 80.00')
    print('2. Chickenjoy Rice Meal | Php 100.00')
    print('3. Cornedbeef Breakfast Meal | Php 70.00')
    print('4. Exit')
    
    menu = input('\nEnter menu choice (Snacks or Meals or Exit): ')
    
    if menu.lower() == 'exit':
        print('Thank you for ordering! Have a great day! ^^')
        break
    
    choice = int(input('Choose from the options above (1-3): '))
    
    if menu.lower() == 'snacks':
        if choice == 1:
            print('Your order is Cheesy Burger Meal that costs Php 50.00. ^^')
            print('Thank you for ordering! Have a great day! ^^')
        elif choice == 2:
            print('Your order is Crunchy Chicken Sandwich that costs Php 60.00. ^^')
            print('Thank you for ordering! Have a great day! ^^')
        elif choice == 3:
            print('Your order is Jolly Hotdog Meal that costs Php 40.00. ^^')
            print('Thank you for ordering! Have a great day! ^^')
        else:
            print('Invalid Choice. Try again. :<')
    
    elif menu.lower() == 'meals':
        if choice == 1:
            print('Your order is Burger Steak that costs Php 80.00. ^^')
            print('Thank you for ordering! Have a great day! ^^')
        elif choice == 2:
            print('Your order is Chickenjoy Rice Meal that costs Php 100.00. ^^')
            print('Thank you for ordering! Have a great day! ^^')
        elif choice == 3:
            print('Your order is Cornedbeef Breakfast Meal that costs Php 70.00. ^^')
            print('Thank you for ordering! Have a great day! ^^')
        else:
            print('Invalid Choice. Try again. :<')
    
    else:
        print('Invalid menu choice. Please enter Snacks, Meals, or Exit.')
