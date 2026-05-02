# set - takrorlanmaydigan to'plam

numbers = {5,9,4,7,3,3,5,7}
# print(numbers, type(numbers), len(numbers))

py_back = {'Humoyun', 'Alijon', 'Karimjon', 'Doniyor','Bob','Valijon'}
front_end = {'Alijon', 'Karimjon','Muhammadaziz',"O'ktam"}


front_end.add('Ilyos')
# front_end.add('Ilyos')
# front_end.add('Ilyos')
# front_end.add('Ilyos')

# print(front_end)


# barcha = py_back | front_end  #py_back.union(front_end)
#
# print(barcha, len(barcha))
# both = py_back & front_end # py_back.intersection(front_end)
# print(both)
# only_py = py_back - front_end # py_back.difference(front_end)
# print(only_py)
# only_front = front_end.difference(py_back)
# print(only_front)

# print(py_back)
#
# py_back.remove('Bob')
# print(py_back)
#
# py_back.clear()
# print(py_back)


# dictionary - lug'at

user = {
    # 'key' : "value"
    'username': 'legion001',
    'name': 'Alijon',
    'by': 2005,
    'is_married' : False,
    'address':"Namangan viloyati Uchqo'rg'on tumani"
}
# print(user['name'])
# print(user['username'])
# print(user['fullname'])

# print(user.get('username'))
# print(user.get('fullname'))
# print(user.get('name'))
# print(user.get('age'))

user['fullname'] = 'Alijon Karimov'


# print(user)
#
# print(user['fullname'])
user.update({"by":2000})
# user_age = 2026 - user['by']
#
# print(user_age)

# print(user.keys())
# print(user.values())


user.pop('address')

print(user)

