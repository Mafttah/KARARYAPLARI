yas = input("Lütfen yaşınızı giriniz: ")


if not yas.strip().isdigit(): 
    print("Yaş bilgisi için sayı girmelisiniz.")
# if (yas.strip())== "":
#print ("Yas bilgisini bos gecemezsiniz !")
    print("Programı tekrar çalıştırıp doğru bir yaş değeri girmelisiniz.")
elif int(yas) < 18:
    print("Yaşınız:" , yas, "\nReşit değilsiniz.")
elif int(yas) >= 18 and int(yas) < 24:
    print("Yaşınız:" , yas, "\nPub'a giremezsiniz. Yaşınız uygun değil.")
elif int(yas) == 24:
    print("Yaşınız:" , yas, "\nLütfen kimlik gösteriniz.")
elif int(yas) >= 25:
    print("Yaşınız:" , yas, "\nPub'a girebilirsiniz.")   
