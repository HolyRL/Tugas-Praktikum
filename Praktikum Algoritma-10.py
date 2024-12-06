def bubble_sort(angka):
    for i in range(len(angka)):
        for r in range(len(angka)-i-1):
            if angka[r] > angka[r+1]:
                angka[r], angka[r+1] = angka[r+1], angka[r]

def binary_search(angka, target):
    a, b = 0, len(angka)-1
    while a <= b:
        c = (a + b) // 2
        if angka[c] == target:
            return c
        elif angka[c] < target:
            a = c + 1
        else:
            b = c - 1
    return -1

def find_element(angka, target):
    bubble_sort(angka)
    print(f"List setelah diurutkan: {angka}")
    return binary_search(angka, target)

angka = [2, 5, 9, 11, 20, 23, 41, 99, 500]
target = int(input("Masukkan angka yang ingin dicari: "))
hasil = find_element(angka, target)

print(f"Elemen {target} {'ditemukan pada indeks ' + str(hasil) if hasil != -1 else 'tidak ditemukan.'}")