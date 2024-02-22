inputData = input()

row = int(inputData[1])
column = int(ord(inputData[0]) - ord('a')) + 1
result = 0

move = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, -2), (-1, 2)]

for i in move:
    next_row = row + i[0]
    next_column = column + i[1]
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1
        
print(result)