from pyexcel_xlsx import get_data

data = get_data('book1.xlsx')

for key,value in data.items():
    print(key)
    print(value)