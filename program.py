print("Merhaba ! Bugün sana hangi işletim sistemini kullanman gerektiği hakkında bir test yapıcaz")

gizlilik = input("Gizliliğe önem verir misin? (Evet veya Hayır): ").strip().lower()

if gizlilik == "evet":
    windows = False
    macos = False
    linux = True
    print("Linux kullanmalısın")

elif gizlilik == "hayır" or gizlilik == "hayir":
    windows = True
    macos = True
    linux = False
    oyun = input("Oyun oynar mısın? (Evet veya Hayır): ").strip().lower()
    if oyun == "evet":
        print("Windows kullanmalısın")
    else:
        print("Macos kullanmalısın ")