def greet_user(name, last):
    print(f'Hi {name} {last}!')
    print('Welcome aboard\n')


print('Start')
greet_user(last="John", name='Smith')
# keyword arguments
greet_user(name='Mary', last='Magdalene')
print('Finish')
