import random

# print(random.randint(100000,999999))

comp_number = random.randint(1, 10)
print(f"🤖: men 1-10 oraliqda bir son tanladim, topoliysizmi?")
while True:
    user_number = int(input('🤖: Taxminingiz: '))
    if comp_number > user_number:
        print('🤖: Men tanlagan son kattaroq')
    elif comp_number < user_number:
        print('🤖: Men tanlagan son kichikroq')
    else:
        print('🎉🎊 Tabriklaymiz topdingiz! 🎊🎉')
        break


