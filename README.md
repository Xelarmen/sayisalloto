# Python ile Sayısal Loto Programı

### Detaylar
>Kullanıcı ismi aldıktan sonra kaç kolon oynamak istediği ile ilgili veriyi "C:\" dizini içerisinde "sayisal" >isimli klasöre "C:\kullaniciadi" adlı dizinine kaydediyor. 
>Devamında ise programa Kullanıcı ismini verdikten sonra kaydedilen dosyadan gerekli dosyaları çekerek kaç >tahminde bulunmanız gerektiğini hesaplıyor. Tahminleri bulunduktan sonra 1 kolon içinde 3 veya daha fazla >doğru tahmininiz varsa bunu size belirtiyor.

### Kullanımı
>Main.py çalıştırıldıktan sonra Kullanıcı adı ve Kaç Kolon sayı üretilmesi gerektiği bilgisi girilir. Run.py >kodunda ise önceki kodda girdiğiniz kullanıcı adınızı sonrasında tahminlerinizi giriyorsunuz.
  
### Olası Hatalar
```sh
Traceback (most recent call last):
  File "C:/Users/Username/PycharmProjects/$projectname/Code.py", line 21, in <module>
    olustur()
  File "C:/Users/Username/PycharmProjects/$projectname/Code.py", line 9, in olustur
    os.mkdir(dirName)
FileExistsError: [WinError 183] Halen varolan bir dosya oluşturulamaz: 'C:\\sayisal/'
```
**Çözümü:**
>"C:\" dizinindeki "sayisal" isimli klasörü silmeniz durumunda ortada sorun kalmayacaktır.


```sh
Traceback (most recent call last):
  File "C:/Users/Username/PycharmProjects/$projectname/pis.py", line 6, in <module>
    with open('C:/sayisal/'+isim+'/veriler.txt') as csvfile:
FileNotFoundError: [Errno 2] No such file or directory: 'C:/sayisal/username/veriler.txt'
```
**Çözümü:**
>"Code.py" çalıştırıldığında girdiğiniz ismin "Run.py" ile aynı olduğundan emin olun.



