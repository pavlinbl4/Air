models = [{'make': 'Nokia', 'model': 216, 'color': 'Black'},
          {'make': 'Mi Max', 'model': 2, 'color': 'Gold'},
          {'make': 'Samsung', 'model': 7, 'color': 'Blue'},
          {'make': 'Apple', 'model': 10, 'color': 'Silver'},
          {'make': 'Oppo', 'model': 9, 'color': 'Red'},
          {'make': 'Huawei', 'model': 4, 'color': 'Grey'},
          {'make': 'Honor', 'model': 3, 'color': 'Black'}]
for i in sorted(models,key = lambda x:x['color']):
    # print("Производитель:", i['make'],", модель:", i['model'],"цвет:",i['color'])
    print(f"Производитель: { i['make'] }, модель: {i['model']}, цвет: {i['color']}")