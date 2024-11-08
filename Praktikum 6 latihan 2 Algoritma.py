print("Menentukan jumlah hari dalam bulan dan tahun tertentu!")

def kabisat(tahun):
    if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
        return True
    else:
        return False

def jumlah_hari(bulan, tahun):
    if bulan in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif bulan in [4, 6, 9, 11]:
        return 30
    elif bulan == 2:
        if kabisat(tahun):
            return 29
        else:
            return 28
    else:
        return None

def mulai():
    while True:
        print("0 untuk menghentikan program")
        bulan = int(input("Masukkan bulan : "))
        if bulan == 0:
            print("Terima kasih!")
            break

        tahun = int(input("Masukkan tahun : "))
        hari = jumlah_hari(bulan, tahun)

        if hari:
            print(f"Ada {hari} hari pada bulan {bulan} tahun {tahun}.\n")
        else:
            print("Masukkan bulan antara 1 dan 12.\n")

mulai()



