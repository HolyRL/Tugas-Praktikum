import math

print("=======Selamat Datang di Program Mencari Akar Persamaan Kuadrat dan Determinan=======")

Ank1 = int(input("Masukan Nilai A = "))
Ank2 = int(input("Masukan Nilai B = "))
Ank3 = int(input("Masukan Nilai C = "))


if Ank1 == 0:
    print("Bukan merupakan Persamaan Kuadrat")
else:
    
    D = (Ank2 ** 2) - (4 * Ank1 * Ank3)
    
    print("Persamaan kuadrat:", Ank1, "x^2 +", Ank2, "x +", Ank3)

    if D > 0:
        x1 = (-Ank2 + math.sqrt(D)) / (2 * Ank1)
        x2 = (-Ank2 - math.sqrt(D)) / (2 * Ank1)
        print("Determinan =", D)
        print("Akar x1 =", x1)
        print("Akar x2 =", x2)
        print("Akar berbeda")
    elif D == 0:
        x1 = x2 = -Ank2 / (2 * Ank1)  
        print("Determinan =", D)
        print("Akar =", x1)
        print("Akar kembar")
    else:
        print("Determinan =", D)
        print("Akar x1 = -", Ank2, "+ √(", D, ")/ 2*", Ank1)
        print("Akar x2 = -", Ank2, "- √(", D, ")/ 2*", Ank1)
        print("Tidak punya akar")

print("Terima Kasih")

