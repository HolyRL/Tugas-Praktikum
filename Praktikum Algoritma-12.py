import pandas as pd

file_path = "Negara.csv"

df = pd.read_csv(file_path)

if len(df) < 10:
    print("Data dalam file CSV kurang dari 10 negara.")
else:
    print("Data Negara:")
    print(df.head(10))

    if 'Benua' in df.columns:
        grouped = df.groupby('Benua').mean(numeric_only=True)
        std_dev_grouped = df.groupby('Benua').std(numeric_only=True)

        print("\nMean (Rata-rata) per Benua:")
        print(grouped)
        print("\nStandar Deviasi per Benua:")
        print(std_dev_grouped)
    else:
        print("Kolom 'Benua' tidak ditemukan dalam data.")


