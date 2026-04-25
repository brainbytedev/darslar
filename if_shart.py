#if shart operatori

# username = 'ikromjon'
# password = 'salom2026'
#
# login = input('Enter your login name: ')
# temp_password = input('Enter your password: ')
#
# if login == username and password == temp_password:
#     print('Login Successful\n foydalanuvchi sahifasiga xush kelibsiz')
#
# else:
#     print('Login failed')
#
#
#
#
# # match case
# # ball = 5,4,3,2,1,0
# ball = 10
# if ball == 5:
#     print("A'lo")
# elif ball == 4:
#     print("Yaxshi")
# elif ball == 3:
#     print("Qoniqarli")
# elif ball == 2:
#     print("Qoniqarsiz")
# elif ball == 1:
#     print("Dabdala")
# else:
#     print("Bunday baho bebaho")
#
# match ball:
#     case 5:
#         print("A'lo")
#     case 4:
#         print("Yaxshi")
#     case 3:
#         print("Qoniqarli")
#     case 2:
#         print("Qoniqarsiz")
#     case 1:
#         print("Dabdala")
#     case _:
#         print("Bunday baho bebaho")
#
# teacher = input("Enter your name: ").lower()
#
# match teacher:
#     case 'ikromjon':                      #'IkromjON' | 'ikromjon' | "IKROMJON":
#         print("Python Backend teacher!")
#     case _:
#         print("Notanish teacher!")



kun = int(input('Kun raqami: '))
qoldiq = kun % 7

if 1 <= kun <= 365:
    match qoldiq:
        case 1 :#| 8 | 15 | 22:
            print('Payshanba')
        case 2: #| 9:
            print('Juma')
        case  3:
            print('Shanba')
        case 4:
            print('Yakshanba')
        case 5:
            print('Dushanba')
        case 6:
            print('Seshanba')
        case 0:
            print('Chorshanba')
else:
    print('Bunday kun yoq')