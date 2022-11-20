def coz():
    try:
        a1 = int(input("a köşesinin x koordinatı:"))
        a2  =int(input("a köşesinin y koordinatı:"))
        b1 = int(input("b köşesinin x koordinatı:"))
        b2 = int(input("b köşesiNin y koordinatı:"))
        c1 = int(input("c köşesinin x koordinatı:"))
        c2 = int(input("c köşesinin y koordinatı:"))
        i1 = int(input("istenilen koordinatın x değerini giriniz:"))
        i2 = int(input("istenilen koordinatın y değerini giriniz."))
    except ValueError:
        print("Lutfen tam sayı giriniz.")
    

    
coz() 