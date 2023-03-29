import random

# kullanıcının gireceği 5 sayı 
print("lütfen 5 tane sayı giriniz:")
sayilar = []
for i in range(5):
    sayi= int(input())
    sayilar.append(sayi)


# rastgele üretilen 5 sayı 
rastgele_sayilar = []
for i in range (5):
    sayi= random.randint(1, 100)
    rastgele_sayilar.append(sayi)
print("rastgele üretilen sayılar:", rastgele_sayilar)

# sayıların sırasıyla toplamı 
toplam = []
for i in range (len(sayilar)):
    toplam.append(sayilar[i] + rastgele_sayilar[i])



# sonucu ekran yazma 
print ("toplam:", toplam)


# sonuçları .txt dosyasına kaydetme 
with open ("sonuc.txt", "w") as dosya:
    for eleman in toplam:
        dosya.write(str(eleman) + "\n")






