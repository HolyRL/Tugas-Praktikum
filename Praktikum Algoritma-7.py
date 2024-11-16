def prima(bil):
    if bil <= 1: 
        return False
    for i in range(2, int(bil**0.5) + 1):  
        if bil % i == 0:  
            return False
    return True

def hasil(bil): 
    if prima(bil):
        print(f"{bil} adalah bilangan Prima.")
    else:
        print(f"{bil} bukanlah bilangan Prima.")

bilangan = int(input("Masukkan angka: "))
hasil(bilangan)


   



