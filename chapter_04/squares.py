squares = []

for value in range(1,11):
    square = value ** 2
    squares.append(square)

print(squares)

print('Alternatively for a more concise code')

squares_2 = [] # first set an empty list
for values in range(2, 12): # values is the temp var
    squares_2.append(values **2)

print(squares_2)

print('For List Comprehensions way')
#inclusive of 3, exclusive of 13
squares_3 = [value3 ** 2 for value3 in range(3,13)]
print(squares_3)
