while True: 
    Ad = input("Lütfen adınızı giriniz: ")
    if Ad == "":    
        print("Ad bilgisini bos gecemezsiniz !")
        print("Başa dön")
        print("")
        continue
    if not Ad.strip().isalpha():
        print("Adınızı girmek için kelime girmelisiniz.") 
        print("Başa dön")
        print("") 
        continue  
    break 

while True:
    Soyad = input("Lütfen Soyadınızı giriniz: ")
    if Soyad == "":
         print("Soyadı bilgisini boş geçemezsiniz.")
         print("Başa dön")
         print("") 
         continue
    if not Soyad.isalpha():
        print("Soyadınızı girmek için kelime girmelisiniz.")
        print("Başa dön")
        print("") 
        continue
    break

while True:
    yas = input("Lütfen yaşınızı giriniz: ")
    if yas == "":
        print("Yas bilgisini bos gecemezsiniz !")
        continue
    if not yas.strip().isdigit():
        print("Yaş bilgisi için sayı girmelisiniz.") 
        print("Yas bilgisini bos gecemezsiniz !")
        continue
    break

if int(yas) >=0 and int(yas)<= 12:
    print("Yaşınız:" , yas, "\n\n -> Çocuk Kategorisindesiniz.")
if int(yas) >= 13 and int(yas) < 17:
        print("Yaşınız:" , yas, "\n\n -> Genç Kategorisindesiniz.")
if int(yas) >= 18 and int(yas) <= 24:
        print("Yaşınız:" , yas, "\n\n -> Genç Yetişkin Kategorisindesiniz.")
if int(yas) >= 25:
        print("Yaşınız:" , yas, "\n\n -> Yetişkin Kategorisindesiniz.") 

print("")
print("Hoşgeldiniz", Ad, Soyad, "\nYaşınız: ", yas)
print("")