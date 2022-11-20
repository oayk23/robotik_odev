a = str(input("metin:"))

b = str(input("aranacak kelime:"))

kelimeler = a.split(" ")
for i in range(len(kelimeler)):
    if kelimeler[i] == b:
        print("kelime bulundu")
        exit()
print("kelime bulunamadı")