

# items = input().split(", ") # список предметов
# buyrs = input().split(", ") # список покупателей
buyrs = ['Michael', 'Jake', 'John', 'Alex', 'Jane', 'Steve']
# price = int(input())
items = ['Apple II', 'компьютерная мышь Lisa', 'Sony PS1', 'YIS-805', 'IBM 5150', 'Macintosh LC520', 'Эльбрус 801-PC']
price = 1500
st = { a : price for a in items} # создаю словарь предмет - стартовая цена

# bid = input().split() # проблема в вводе ставок^ что есть проелы и в названии лота
bid = ['Lisa', 'компьютерная', 'мышь', 'Lisa', '2000']
print(bid[0]) # имя покупателя
print(bid[-1]) # величина ставки
print(bid)
print(" ".join(bid[1:-1])) # название лота

