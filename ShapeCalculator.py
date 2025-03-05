print('=== Area of Calculation ===')
print('1. Square')
print('2. Rectangle')
print('3. Circle')
print('4. Triangle')

shape = input('\nEnter shape: ')

if shape == 'Square':
    side = float(input("Enter side length: "))
    area = side * side
    print('Output Area: ', area)
    
elif shape == 'Rectangle':
    length = float(input('Enter length: '))
    width = float(input('Enter width: '))
    area =  length * width
    print('Output Area: ', area)

elif shape == 'Circle':
    pi = 3.1416
    radius = float(input('Enter radius: '))
    area = pi * radius * radius
    print('Output Area: ', area)

elif shape == 'Triangle':
    base = float(input('Enter base: '))
    height = float(input('Enter height: '))
    area = 0.5 * base * height
    print('Output Area: ', area)

else:
    area = None
    print('Invalid shape.')