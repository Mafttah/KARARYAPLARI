import colorama
from colorama import Fore
while True: 
    print(Fore.BLUE)
    Ad = input("Lütfen adınızı giriniz: ")
    if Ad == "":    
        print(Fore.RED, "Ad bilgisini bos gecemezsiniz !")
        print(Fore.WHITE, "Başa dön")
        print("")
        continue
    if not Ad.strip().isalpha():
        print(Fore.RED, "Adınızı girmek için kelime girmelisiniz.") 
        print(Fore.WHITE, "Başa dön")
        print("") 
        continue  
    break 

while True:
    print(Fore.BLUE)
    Soyad = input("Lütfen Soyadınızı giriniz: ")
    if Soyad == "":
         print(Fore.RED, "Soyadı bilgisini boş geçemezsiniz.")
         print(Fore.WHITE, "Başa dön")
         print("") 
         continue
    if not Soyad.isalpha():
        print(Fore.RED, "Soyadınızı girmek için kelime girmelisiniz.")
        print(Fore.WHITE,"Başa dön")
        print("") 
        continue
    break

while True:
    print(Fore.WHITE)
    yas = input("Lütfen yaşınızı giriniz: ")
    if yas == "" :
        print(Fore.RED, "Yas bilgisini bos gecemezsiniz !")
        print(Fore.WHITE, "Başa Dön")
        print("")
        continue
    if not yas.strip().isdigit():
        print(Fore.RED,"Yaş bilgisi için sayı girmelisiniz.")
        print(Fore.WHITE,"Başa dön")
        print("")
        continue
    break
if int(yas) >=0 and int(yas)<= 12:
    print(Fore.YELLOW, "\n -> Çocuk Kategorisindesiniz.")
if int(yas) >= 13 and int(yas) < 17:
        print(Fore.YELLOW, "\n -> Genç Kategorisindesiniz.")
if int(yas) >= 18 and int(yas) <= 24:
        print(Fore.YELLOW, "\n -> Genç Yetişkin Kategorisindesiniz.")
if int(yas) >= 25:
        print(Fore.YELLOW, "\n -> Yetişkin Kategorisindesiniz.") 

print("")
print(Fore.BLUE, "Hoşgeldiniz:", Fore.WHITE, Ad, Soyad)      
print(Fore.BLUE, "Yaşiniz:", Fore.WHITE, yas)
