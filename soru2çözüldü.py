a = int(input("istenilen sayı:"))
sayac = 1
liste = list()
if a <=1:
    print("siktirlan ordan 0 dan büyük bişey yaz.")
while (sayac <= a):
    if a%sayac == 0:
        liste.append(sayac)
    sayac +=1

print(liste)
