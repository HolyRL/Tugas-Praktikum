def nilai(huruf):
    if huruf == 'A':
        return 4.00
    elif huruf == 'A-':
        return 3.75
    elif huruf == 'B+':
        return 3.50
    elif huruf == 'B':
        return 3.00
    elif huruf == 'B-':
        return 2.75
    elif huruf == 'C+':
        return 2.50
    elif huruf == 'C':
        return 2.00
    elif huruf == 'C-':
        return 1.75
    elif huruf == 'D':
        return 1.50
    elif huruf == 'E':
        return 1.25
    else:
        return None 

def rata_rata():
    total_nilai = 0
    jumlah_nilai = 0

    while True:
        data = input("Input nilai: ")
        
        if data == "":
            break
        
        nilai1 = nilai(data)
        
        if nilai1 is not None:
            total_nilai += nilai1
            jumlah_nilai += 1
            print(f'Nilai = {nilai1:.2f}')
        else:
            print("Nilai invalid!")

    if jumlah_nilai > 0:
        avg = total_nilai / jumlah_nilai
        print(f'Rata-rata nilai: {avg:.2f}')
    else:
        print("Invalid.")

rata_rata()

