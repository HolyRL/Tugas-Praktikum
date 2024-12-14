class Mahasiswa:
    def __init__(self, nama, nim, tahun_angkatan):
        self.nama = nama
        self.nim = nim
        self.tahun_angkatan = tahun_angkatan

    def tampilkan_biodata(self):
        print(f"Nama: {self.nama}")
        print(f"NIM: {self.nim}")
        print(f"Tahun Angkatan: {self.tahun_angkatan}")

# Input biodata mahasiswa
nama = input("Masukkan namamu: ")
nim = input("Masukkan NIM mu: ")
tahun_angkatan = input("Masukkan tahun angkatanmu: ")

mahasiswa = Mahasiswa(nama, nim, tahun_angkatan)

mahasiswa.tampilkan_biodata()
