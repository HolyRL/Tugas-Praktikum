print("======SELAMAT DATANG DI KEBUN BINATANG=====")

total_harga = 0.0

while True:
    umur = int(input("Masukkan umur pengunjung: "))
    if umur == -1 :
        break

    if umur <= 2:
        harga = 0.0
    elif 3 <= umur <= 12:
        harga = 14.0
    elif umur >= 65:
        harga = 18.0
    else:
        harga = 23.0

    total_harga += harga

    print(f"Harga tiket: ${harga:.2f}")
    print(f"Running total: ${total_harga:.2f}")

if total_harga > 0:
    uang_dibayar = float(input("Masukkan jumlah uang : "))
    if uang_dibayar < total_harga:
        print("Uang tidak cukup.")
    else:
        kembalian = uang_dibayar - total_harga
        print(f"Running kembalian: ${kembalian:.2f}")

print("======Terima Kasih======")
