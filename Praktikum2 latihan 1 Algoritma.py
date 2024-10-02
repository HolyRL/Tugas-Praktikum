import math
a1 = float(input("Lintang kota 1: "))
a2 = float(input("Bujur kota 1: "))
b1 = float(input("Lintang kota 2: "))
b2 = float(input("Bujur kota 2: "))

a1 = math.radians(a1)
a2 = math.radians(a2)
b1 = math.radians(b1)
b2 = math.radians(b2)

R = 6371.0

Aa = b1 - a1
Bb = b2 - a2

a = math.sin(Aa / 2)**2 + math.cos(a1) * math.cos(b1) * math.sin(Bb / 2)**2
c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

jarak = R * c

print(f"Jarak antara kedua titik tersebut adalah {jarak: .2f} kilometer.")