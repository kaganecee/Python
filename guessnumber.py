import random
denemeSayısı = 0
number = random.randint(1, 100)
number1 = int(input("Lütfen seçilen sayıyı tahmin ediniz...:"))
if(number==number1):
    print("Doğru tahmin ettiniz. Deneme sayınız", denemeSayısı)
else:
    while(number1 != number):
        denemeSayısı = denemeSayısı + 1
        if(number<number1):
            number1 = int(input("Tahmininizi alçaltarak tekrar tahmin ediniz:"))
        elif(number>number1):
            number1 = int(input("Tahmininizi yükselterek tekrar tahmin ediniz:"))
    if (number == number1):
        print("Doğru tahmin ettiniz. Deneme sayınız", denemeSayısı)