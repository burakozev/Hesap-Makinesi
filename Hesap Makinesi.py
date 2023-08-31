def topla(x, y):
    return x + y


def cikar(x, y):
    return x - y


def carp(x, y):
    return x * y


def bol(x, y):
    if y != 0:
        return x / y
    else:
        return "Bölme işlemi için payda 0 olmamalıdır."


print("İşlem Seçiniz")
print("1. Toplama")
print("2. Çıkarma")
print("3. Çarpma")
print("4. Bölme")

secim = input("(1/2/3/4): ")

if secim in ["1", "2", "3", "4"]:
    sayi1 = float(input("1. Sayıyı Giriniz: "))
    sayi2 = float(input("2. Sayıyı Giriniz: "))


    if secim == "1":
        sonuc = topla(sayi1, sayi2)
    elif secim == "2":
        sonuc = cikar(sayi1, sayi2)
    elif secim == "3":
        sonuc = carp(sayi1, sayi2)
    elif secim == "4":
        sonuc = bol(sayi1, sayi2)

    if sonuc.is_integer():
        sonuc = int(sonuc)
        print("Sonuç:", sonuc)
    else:
        print("Sonuç:", sonuc)
else:
    print("Geçersiz Seçim")