import pandas as pd

data = {
    "Negara": ["Indonesia", "Jepang", "India", "China", "Amerika Serikat", "Brazil", "Rusia", "Nigeria", "Aljazair", "Inggris"],
    "Ibu Kota": ["Jakarta", "Tokyo", "New Delhi", "Beijing", "Washington DC", "Brasilia", "Moskow", "Abuja", "Aljazair", "London"],
    "Benua": ["Asia", "Asia", "Asia", "Asia", "Amerika", "Amerika", "Asia", "Afrika", "Afrika", "Eropa"],
    "Luas": [1905, 377, 3287, 9597, 9834, 8515, 17098, 923, 2381, 242],
    "Populasi": [264, 143, 1252, 1357, 329, 210, 146, 200, 43, 66]
}

df = pd.DataFrame(data)

mean_df = df.groupby("Benua")[["Luas", "Populasi"]].mean().reset_index()
std_df = df.groupby("Benua")[["Luas", "Populasi"]].std().reset_index()

mean_df.rename(columns={"Luas": "Mean Luas", "Populasi": "Mean Populasi"}, inplace=True)
std_df.rename(columns={"Luas": "Std Luas", "Populasi": "Std Populasi"}, inplace=True)

mean_df.to_csv("NegaraMean.csv", index=False)
std_df.to_csv("NegaraStandarDeviasi.csv", index=False)

print("Berikut Data Frame-nya:\n")
print(df)
print("\nBerikut Data Mean:\n")
print(mean_df)
print("\nBerikut Data Standard Deviation:\n")
print(std_df)

print("\nFile berhasil dibuat:\n1. NegaraMean.csv\n2. NegaraStandarDeviasi.csv")

