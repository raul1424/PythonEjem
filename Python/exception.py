import sys
#x = input ('x: ')
#y = input ('y: ')

#print(f'{x} / {y} = {x/y}')

try:
    x = int(input('x: '))
    y = int(input('y: '))
except ValueError:
     print('Error de tipo')

try:
    resultado = x/y
except ZeroDivisionError:
    print('error dividir por cero')
    sys.exit(1)

print(f'{x}/{y}={resultado}')
