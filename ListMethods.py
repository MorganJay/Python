numbers = [3, 4, 5, 1, 5, 4, 5, 3, 1, 6]
# numbers.append(30)
# numbers.insert(0, 2)
# numbers.remove()
# numbers.clear()
# numbers.pop()
# print(numbers.index(4))
# print(42 in numbers)
# print(numbers.count(5))
# numbers.sort()
# numbers.reverse()
numbers2 = numbers.copy()
unique = []
for i in numbers:
    if i not in unique:
        unique.append(i)
numbers.sort()
unique.sort()
print(numbers)
print(unique)


