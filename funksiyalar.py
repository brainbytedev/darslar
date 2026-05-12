from wsgiref.util import request_uri


def salomlash():
    print("Assalomu aleykum")


def salomlash_pro(ism):
    text = f"Assalomu aleykum {ism} aka!"
    print(text)


def kattani_top(a, b):
    if a > b:
        return f"A son katta {a} > {b}"
    elif a < b:
        return f"B son katta {b} > {a}"
    else:
        return f"A va B sonlar teng {a} = {b}"

a = int(input("A son: "))
b = int(input("B son: "))

print(kattani_top(a, b))


# print(max(45,65,5,4))
# print(min(45,65,5,4))

# salomlash()
# salomlash()
# salomlash()
# salomlash()

# salomlash_pro('Humoyun')
# salomlash_pro('Muhammadaziz')
# salomlash_pro('Muhammadrizo')
# salomlash_pro('Fatxullox')
# salomlash_pro('Aziza')