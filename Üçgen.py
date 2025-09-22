x = int(input("Açı 1 : "))
y = int(input("Açı 2 : "))
z = int(input("Açı 3 : "))
a = int(input("Açı 4 : "))
b = int(input("Açı 5 : "))
c = int(input("Açı 6 : "))
d = int(input("Açı 7 : "))
e = int(input("Açı 8 : "))
if x + y + z == 180:
    print("Bu Bir Üçgen") 
if x + y + z + a == 360:
    print("Bu Bir Kare")         
if x + y + z + a + b == 540:
    print("Bu Bir Beşgen")
if x + y + z + a + b + c == 720:
    print("Bu Bir Altıgen")
if x + y + z + a + b + c + d == 900:
    print("Bu Bir Yedigen")         
if x + y + z + a + b + c + d + e == 1080:
    print("Bu Bir Sekizgen")