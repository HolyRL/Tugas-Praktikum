class ManipulasiNilai:
    def __init__(self):
        self.nilai = 0

    def get_nilai(self):
        return self.nilai

    def set_nilai(self, nilai):
        if 0 <= nilai <= 100:
            self.nilai = nilai
            print(f"Nilai berhasil diperbarui menjadi: {nilai}")
        else:
            print("Nilai yang dimasukkan tidak valid! Harus antara 0 dan 100.")

def main():
    obj = ManipulasiNilai() 

    while True:
        print("\nProgram OOP:")
        print("1. Masukkan Nilai")
        print("2. Tampilkan Nilai")
        print("3. Ubah Nilai")
        print("4. Keluar")
        pilihan = input("Pilih menu (1-4): ")

        if pilihan == '1':
            nilai_masukkan = input("Masukkan nilai (0-100): ")
            if nilai_masukkan.isdigit(): 
                nilai_masukkan = int(nilai_masukkan)
                obj.set_nilai(nilai_masukkan)
            else:
                print("Input nilai tidak valid! Harap masukkan angka.")
        elif pilihan == '2':
            print(f"Nilai saat ini adalah: {obj.get_nilai()}")
        elif pilihan == '3':
            nilai_baru = input("Masukkan nilai baru (0-100): ")
            if nilai_baru.isdigit():  
                nilai_baru = int(nilai_baru)
                obj.set_nilai(nilai_baru)
            else:
                print("Input nilai tidak valid! Harap masukkan angka.")
        elif pilihan == '4':
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

if __name__ == "__main__":
    main()
