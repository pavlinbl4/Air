vk = {'driver.drv': 'system', 'bussiness_data.txt': 'confidential', 'gtaV_graphics.txt': 'settings', 'отчет.txt': 'ordinary', 'fight_club.torrent': 'ordinary'}

print(vk['driver.drv'])  # вывод значения по ключу
print(vk)
print("driver.drv" in vk)
print("system" in vk)


# """пробую создать словарь6где в качестве  значения используется список"""
# phonebook = {
#     "tom":[555555,6666666,7777777],
#     "jerry": [444444,333333,34343434]
# }
#
# phonebook["scrudj"] = 837598345238 # добавление ключ - значение в словарь
# phonebook["tom"].append(10101) # добавляю данные в список значения в словаре
# print(phonebook.get("bob"))
#
# print(phonebook)
# print(phonebook["tom"])
# print(*phonebook["tom"])
# print(333333 in phonebook)
vk = {v:k for k, v in vk.items()} # меняем местами ключи и значения в словер
print(vk)
print("driver.drv" in vk)
print("system" in vk)

