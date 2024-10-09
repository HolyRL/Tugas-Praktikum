print("=======Selamat Datang di Segitiga Detector=======")

a = int(input("Masukkan panjang sisi a: "))
b = int(input("Masukkan panjang sisi b: "))
c = int(input("Masukkan panjang sisi c: "))

if a + b > c and a + c > b and b + c > a:
    
    if a == b == c:
        print("Segitiga sisi.")
        print("=======Terimakasih=======")
    elif a == b or a == c or b == c:
        print("Segitiga ini adalah segitiga sama kaki.")
        print("=======Terimakasih=======")
    elif round(a**2, 5) == round(b**2 + c**2, 5) or round(b**2, 5) == round(a**2 + c**2, 5) or round(c**2, 5) == round(a**2 + b**2, 5):
        print("Segitiga siku-siku")
        print("=======Terimakasih=======")
    else:
        print("Segitiga sembarang")
        print("=======Terimakasih=======")
else:
    print("Bukan seigitiga")
    print("=======Terimakasih=======")

