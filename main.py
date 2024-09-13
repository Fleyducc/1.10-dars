import random

son = random.randint(1, 10)

tahminlar = 0

print("1 dan 10 gacha bo'lgan raqamni taxmin qiling! Sizda 3 marta urinish bor.")

for urinish in range(3):
    tahmin = int(input("Raqam kiriting: "))  
    tahminlar += 1  

    
    if tahmin == son:
        print(f"Tabriklaymiz! Siz {tahminlar} urinishda raqamni topdingiz!")
        break
    elif tahmin > son:
        print("raqam katta.")
    else:
        print("raqam kichik.")

print("O'yin tugadi!")

