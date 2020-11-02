numbers = [8, 9, 10, 11]
numbers[1] = 17
# print(numbers) #Заменил второй элемент списка на 17
numbers.append(4)
numbers.append(5)
numbers.append(6)
# print(numbers)#Добавил числа 4, 5 и 6 в конец списка;
numbers.pop(0)
# print(numbers)#Удалил первый элемент списка;
numbers = numbers * 2
# print("Удвоил список ",numbers)
numbers.insert(3,25)
# print("Вставил число 25 по индексу 3 -",numbers)
print(numbers)



