# 3 xil usul
ism1 = "Ali"                    # ikkita tirnoq
ism2 = 'Vali'                   # bitta tirnoq
bio = """
Mening ismim Ali.
Men Toshkentda yashayman.
"""                             # uch tirnoq — ko'p qatorli

# Aralash tirnoq
#        012345
xabar = "O'zbek tili"           # ichida apostrof bor
xabar2 = 'U "dasturchi"'        # ichida qo'shtirnoq bor

# print("Salom", ism1)
# print(ism2, len(ism2))
# print(xabar, len(xabar), type(xabar))
# print(xabar[0])
# print(xabar[2])
# print(xabar[11])
# print(xabar[-1])
# print(xabar[0:6])
# print(bio[23:31])

name = input("Ismingiz: ")
print("Assalomu aleykum " + name.capitalize() + ' aka') # capitalize()
print("Assalomu aleykum " + name.title() + ' aka')      # title()
print("Assalomu aleykum " + name.lower() + ' aka')      # lower()
print("Assalomu aleykum " + name.upper() + ' aka')      # upper()
print("Assalomu aleykum " + name.swapcase() + ' aka')   # swapcase()
print(f"Assalomu aleykum {name.capitalize()} aka")