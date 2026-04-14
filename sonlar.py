# 1. BMI (Tana Massa Indeksi)
vazn = 55      # kg
bo_y = 1.65    # metr
bmi = vazn / (bo_y ** 2)
print(f"BMI: {bmi:.2f}")   # BMI: 22.9
print(f"BMI: {round(bmi, 2)}")   # BMI: 22.9


# 2. Kredit hisoblash
kredit = 10_000_000   # 10 mln so'm (Python'da _ ishlating)
foiz = 0.18           # 18% yillik
muddat = 24           # oy
oylik_foiz = foiz / 12
oylik_tolov = kredit * (oylik_foiz * (1+oylik_foiz)**muddat) / ((1+oylik_foiz)**muddat - 1)

print(f"Oylik to'lov: {oylik_tolov:,.0f} so'm")

# 3. Pifagor teoremasi
a = 3
b = 4
import math
c = math.sqrt(a**2 + b**2)
print(f"Gipotenuza: {c}")  # 5.0


a = float(input("Birinchi son: "))
b = float(input("Ikkinchi son: "))

print(f"\n{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
# if b != 0:
print(f"{a} / {b} = {a / b:.4f}")
print(f"{a} // {b} = {a // b}")
print(f"{a} % {b} = {a % b}")
print(f"{a} ** 2 = {a ** 2}")


# misol = '(5+9)*2**3'
# print(eval(misol))

print('salom dunyo')