import csv

isim = input("İsim Giriniz").lower()

results = []
with open('C:/sayisal/'+isim+'/veriler.txt') as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        results.append(row)

print(str(len(results)) + " Kolon Oynanmış. Toplamda "+ str(len(results)*6) + " tahminde Bulunacaksınız")

sonuclar = []
kolonsayisi = 0

for result in results:
    basarilisayac=0
    i = 0
    while i < 6:
        z = 0
        tahmin = input(str(kolonsayisi+1) +". Kolon için " + str(i+1) + ". Tahmininizi Girin")
        while z < 6:
            if int(tahmin) == int(results[kolonsayisi][z]):
                basarilisayac = basarilisayac + 1
            z = z + 1
        i = i + 1
    if basarilisayac >= 3:
        sonuclar.append((str(kolonsayisi+1)) + ". Kolonda " + str(basarilisayac) + " Tane Bildiniz!")
    kolonsayisi = kolonsayisi + 1




print(sonuclar)





