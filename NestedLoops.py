# for x in range(4):
#     for y in range(4):
#         print(f'({x},{y})')
numbers = [1, 1, 1, 1, 7]
for xNumber in numbers:
    output = ""
    # print('x' * xNumber)
    for count in range(xNumber):
        output += 'x'
    print(output)
