def biodata():
    nama = input("Namamu: ")
    umur = input("Umurmu: ")
    alamat = input("Alamatmu: ")
    email = input("Emailmu: ")
    dosen_wali = input("Dosen Walimu: ")
    
    file = open("Biodata.txt", "w")
    file.write(f"Nama: {nama}\n")
    file.write(f"Umur: {umur}\n")
    file.write(f"Alamat: {alamat}\n")
    file.write(f"Email: {email}\n")
    file.write(f"Dosen Wali: {dosen_wali}\n")
    file.close()  
    
def baca_biodata():
    file = open("Biodata.txt", "r") 
    isi_file = file.read()  
    file.close()  

    print("\nBerikut ini biodata kamu:\n")
    print(isi_file)

def main():
    biodata()  
    baca_biodata()  

main() 













   



