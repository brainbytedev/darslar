# str    = belgilar (matn)
# int    = butun sonlar
# float  = o'nli kasr
# bool   = True / False


# list = o'zgaruvchan, tabtiblangan, takrorlanuvchi ro'yxat
# tuple = o'zgarmas, tabtiblangan, takrorlanuvchi ro'yxat
# set = {1,1,1,1,1}
# dict = {key:value}



# pupil1 = 'Humoyun'
# pupil2 = 'Muhammadrizo'
# pupil3 = 'Fathullo'
# pupil4 = 'Muhammadaziz'
#             0            1              2             3
pupils = ['Humoyun', 'Muhammadrizo', 'Fathullo', 'Muhammadaziz']
# print(pupils[2])
# print(pupils[-1])
# print(pupils[-3])
# print(pupils[-4])
# print(pupils[0])

# =========== add elements ====================
pupils.append('Sherzodbek')
# print(pupils)
# print(len(pupils), type(pupils) )
pupils.insert(2, 'Ilyosbek')
# print(pupils)
pupils.extend(['Alijon', 'Valijon', 'Karimjon'])
# print(pupils)


# ========== delete elements ==========
pupils.pop()
# print(pupils)
pupils.remove('Ilyosbek')
# print(pupils)
pupils.pop(-1)
print(pupils)

pupils.reverse()
print(pupils)
pupils.sort()
print(pupils)

# print(pupils.count('Alijon'))
# print(pupils.index('Muhammadrizo'))
# print(pupils.pop())


pupil = ['Alijon', 15, 'Namanagan', False]
numbers_list = [1, 2, 3, 4, 5]
numbers_tuple= (1, 2, 3, 4, 5)
# print(numbers_list)
# print(max(numbers_list))
# print(min(numbers_list))
# print(sum(numbers_list))
print(type(numbers_list), len(numbers_list), numbers_list)
print(type(numbers_tuple), len(numbers_tuple), numbers_tuple)
