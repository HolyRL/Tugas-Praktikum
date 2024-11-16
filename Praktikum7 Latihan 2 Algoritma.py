print("======Ordinal======")
print("Ketik 0 untuk menghentikkan program")
def ordinal(n):
    if 10 <= n % 100 <= 20:
        tanda = 'th'
    else:
        if n % 10 == 1:
            tanda = 'st'
        elif n % 10 == 2:
            tanda = 'nd'
        elif n % 10 == 3:
            tanda = 'rd'
        else:
            tanda = 'th'
    
    return (n, tanda)

while True:
    isi = input("Masukkan angka: ")  
    
    if isi.isdigit():  
        isi = int(isi)  
        
        if isi == 0:  
            print("Terima kasih!")
            break
        
        print(f"{ordinal(isi)}") 

   



