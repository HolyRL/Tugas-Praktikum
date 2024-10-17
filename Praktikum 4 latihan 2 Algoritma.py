while True:
    Bulan = int(input("Masukkan bulan (1-12), -1 berhenti: "))
    
    if Bulan == -1:
        print("Terima kasih!")
        break

    Tahun = int(input("Masukkan tahun: "))
    
    if Bulan < 1 or Bulan > 12:
        print("Tidak valid! Masukan antara 1-12.")
    else:
        jumlah_hari = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if Bulan == 2:
            if (Tahun % 4 == 0 and Tahun % 100 != 0) or (Tahun % 400 == 0):
                print(f"Bulan {Bulan} pada tahun {Tahun} memiliki 29 hari (tahun kabisat).")
            else:
                print(f"Bulan {Bulan} pada tahun {Tahun} memiliki 28 hari.")
        else:
            print(f"Bulan {Bulan} pada tahun {Tahun} memiliki {jumlah_hari[Bulan - 1]} hari.")