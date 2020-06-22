import os
from random import randint

def olustur():
    isim= input("İsminizi Giriniz").lower() #isimi kücük harflerle input yapıyoruz
    kolonsayisi=input("Kaç Kolon Oynayacaksınız")

    dirName = "C:\sayisal/" #Dizin Oluşturulur
    os.mkdir(dirName)
    dirName = "C:\sayisal/" + isim + "/" # Kisisel Dizin Oluşturulur
    os.mkdir(dirName)

    f = open(dirName +"veriler.txt", "w+") #Metin belgesi Oluşturulr

    for i in range(int(kolonsayisi)):
        for z in range(0, 6):
            f.write(str(randint(1, 49)) + ",")  # Random Sayı yazar
        f.write("\n")


olustur()
