friends = ['ali', 'valijon', 'salimjon','karimjon', 'bob', 'alice', 'xasanboy','xusanboy']

# print(friends, type(friends), len(friends))
# # friends.upper()
#
# # print(['Ali', 'Valijon', 'Salimjon', 'Karimjon'])
# katta_xarf = []
# for dost in friends:
#     katta_xarf.append(dost.title())
#
# print(katta_xarf)

# print(f"Do'stim {friends[0].title()}, Seni Qurbon Hayit bayrami bilan tabriklayman!")
# print(f"Do'stim {friends[1].title()}, Seni Qurbon Hayit bayrami bilan tabriklayman!")
# print(f"Do'stim {friends[3].title()}, Seni Qurbon Hayit bayrami bilan tabriklayman!")
# print(f"Do'stim {friends[4].title()}, Seni Qurbon Hayit bayrami bilan tabriklayman!")
# print(f"Do'stim {friends[5].title()}, Seni Qurbon Hayit bayrami bilan tabriklayman!")
# print(f"Do'stim {friends[2].title()}, Seni Qurbon Hayit bayrami bilan tabriklayman!")

# for i in friends:
#     print(f"Do'stim {i.title()}, Seni Qurbon Hayit bayrami bilan tabriklayman!")
#
# numbers = [45,68,9,41,4,2,4,7,6,1,5,4]
# juft = []
# toq = []
# for i in numbers:
#     if i % 2 == 0:
#         juft.append(i)
#     else:
#         toq.append(i)
# print(toq)
# print(juft)
#
# for i in numbers:
#     print(f"{i} ** 2 = {i**2}")
#
# for i in 'salom':
#     print(i*50)

# range(start, stop, step)
# sonlar = tuple(range(1,101,1))
sonlar = tuple(range(100))
print(sonlar)
sakkiz = list(range(104, 999, 8))
print(sakkiz)

for i in range(10):
    print(i*"*")