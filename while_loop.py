# while shartga ko'ra takrorlash

qadam = 0
while qadam < 5:
    print(qadam)
    # qadam += 1 # qadam = qadam + 1
print('Takrorlanish yakunlandi!')

belgi = True
while belgi:
    number = int(input("Enter a number: "))
    if number == 0:
        belgi = False
        print("takrorlanish yakunlandi")
    else:
        print(f"{number} * {number} = {number*number}")

while True:
    number = input("Enter a number: ")
    if number.isdigit():
        number = int(number)
        if number == 0:
            print("takrorlanish yakunlandi")
            break
        else:
            print(f"{number} * {number} = {number*number}")
    else:
        print("Faqat son kiriting")