def rekursif(angka, pangkat):
    if pangkat == 0:
        return 1
    else:
        return angka * rekursif(angka, pangkat - 1)

def perhitungan():
    angka_input = input("Masukkan angka (Enter untuk berhenti): ")

    if angka_input == "":
        print("Terima kasih!")
        return  
    pangkat_input = input("Masukkan pangkat: ")
    angka = int(angka_input)
    pangkat = int(pangkat_input)

    hasil = rekursif(angka, pangkat)
    print(f"Hasil dari {angka} pangkat {pangkat} adalah {hasil}")

    perhitungan()    

perhitungan()






   



