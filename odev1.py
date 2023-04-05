baslik="Haberiniz olsun"
print(baslik)
print(type(baslik))
vade=6
faizOrani1=1.47
faizOrani2=1.43
print(vade)
print(faizOrani1)
print(faizOrani2)
print(type(vade))
print(type(faizOrani1))
print(type(faizOrani2))

mesaj="Hosgeldiniz"
musteriAdi="Duygu"
musteriSoyadi="Yilmaz"

print(mesaj+" "+musteriAdi+" "+musteriSoyadi)
son_mesaj=mesaj +" "+musteriAdi+" "+musteriSoyadi
print(son_mesaj)

sayi1=10
sayi2=20
toplam=sayi1 + sayi2
print(toplam)
print(sayi1+sayi2)
#kosullar#

dolarDun= 5.50
dolarBugun=5.40


if dolarDun < dolarBugun :
    print("Artis oku")
if dolarDun > dolarBugun:
    print("Azalis oku")
if dolarDun ==dolarBugun :
    print("Esittir oku")

#şartları okuyarak yukarıdan aşağı dogru calısır.

#else ve elif komutları
dolarDun= 5.50
dolarBugun=5.40


if dolarDun < dolarBugun :
    print("Artis oku")
    print("Bitti")
elif dolarDun > dolarBugun:
    print("Artis oku")
else:
    print("Esittir oku")

print("Bitti")

#if e bakar ,yanlışssa else kodunu döndürür.
#eger en bastaki if blogu calısırsa döngü oradan sonra biter.
#if blogu kodları dogru değilse asagı iner.

# Dizi(Array)#
#liste tanımlama
krediler= ["Hızlı Kredi","Maaşını halkbanktan alanlara özel","mutlu emeklilik ihtiyac kredisi"]
print(krediler)

print(krediler[0])
#diziler 0 dan başlar.İndex kodu olarak 0 dersek listedeki 1.elemanımızı verir.

print(len(krediler)) #kaç eleman var?
krediler[0]="Çabuk Kredi"
print(krediler) #1.elemanı değiştirdik.

#Döngüler
for kredi in krediler :
    print(kredi)

for i in range(10): #10kere calısacak döngü
    print(i)

for i in range(len(krediler)):
    print(i)

for i in range(len(krediler)):
    print(krediler[i])

for i in range(10):
    print(i)

for i in range(3,10):
    print(i)

for i in range(0,10,2):
    print(i)

#Fonksiyonlar

def kredileriListele():
    kredilere=["Hızlı Kredi","Maasını halkbanktan alanlara özel","Mutlu emekli ihtiyac kredisi"]
    for kredi in krediler:
        print("<option>"+kredi+"<option>")

        kredileriListele()



























