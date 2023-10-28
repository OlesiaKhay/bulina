numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
position = numbers.index(None)
f = sum(numbers[:position])
s = sum(numbers[position+1:])
srednee = (f+s)/len(numbers)
new_Numbers = numbers.copy()
new_Numbers[position] = srednee

print("Измененный список:", new_Numbers)