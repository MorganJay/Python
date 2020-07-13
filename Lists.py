# names = ['James', 'Elijah', 'Glory', 'Miracle', 'Lisa']
# names[3] = 'Egungun'
# print(names)
numbers = [21, 31, 342, 1, 3, 42, 23, 4]
# largestNumber = max(numbers)
# print(largestNumber)
maxNum = numbers[0]
for number in numbers:
    if number > maxNum:
        maxNum = number
print(maxNum)
