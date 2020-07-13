weight = int(input('Weight: '))
unit_weight = input('Enter lbs for pounds or kg for Kilograms: ')
if unit_weight == "lbs":
    converted = weight * 0.45
    print(f'{converted} kg')
else:
    converted = weight // 0.45
    print(f'{converted} lbs')
