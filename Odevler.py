import keyboard
Ad = input("Lütfen adınızı giriniz: ")

if not Ad.strip().isalpha():
    print("Adınızı girmek için kelime girmelisiniz.")
    print("Ad bilgisini bos gecemezsiniz !")
    print("Programı tekrar çalıştırıp doğru bir yaş değeri girmelisiniz.")
print(":ıkmak için esc'ye basın")
keyboard.wait("esc")

Soyad = input("Lütfen Soyadınızı giriniz: ")

if not Soyad.strip().isalpha():
    print("Soyadınızı girmek için kelime girmelisiniz.")
    print("Soyad bilgisini bos gecemezsiniz !")
    print("Programı tekrar çalıştırıp doğru bir yaş değeri girmelisiniz.")
yas = input("Lütfen yaşınızı giriniz: ")
if not yas.strip().isdigit():
    print("Yaş bilgisi için sayı girmelisiniz.") 
    print("Yas bilgisini bos gecemezsiniz !")

#if (yas.strip())== "":
    #print("Programı tekrar çalıştırıp doğru bir yaş değeri girmelisiniz."


elif int(yas) >=0 and int(yas)<= 12:
    print("Yaşınız:" , yas, "\n -> Çocuk Kategorisinidesiniz.")
elif int(yas) >= 13 and int(yas) < 17:
    print("Yaşınız:" , yas, "\n -> Genç Kategorisindesiniz.")
elif int(yas) >= 18 and int(yas) <= 24:
    print("Yaşınız:" , yas, "\n -> Genç Yetişkin Kategorisindesiniz.")
elif int(yas) >= 25:
    print("Yaşınız:" , yas, "\n -> Yetişkin Kategorisindesiniz.")  

kategori = input(" 0-12 yaş -> Çocuk kategorisi\n, 13-17 yaş -> Genç Kategorisi\n, 18-24 yaş Genç Yetişkin\n, =>25 -> Yetişkin Kategorisi")   

print("Hoşgeldiniz", Ad, Soyad, yas, kategori)