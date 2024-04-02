Icecream = int(input("Скільки коштує 1 порція морозива в грн"))
water = int(input("Скільки коштує 1 пляшка газованої води в грн"))
Stephania = (3*Icecream)+(2*water)
Misha = (2*Icecream)+(3*water)
if Stephania > Misha:
    print("Стефанія витратила більше грошей")
elif Stephania < Misha:
    print("Михайло витратила більше грошей")
else:
    print("Вони витратили однаково грошей")