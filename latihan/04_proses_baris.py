nilai = []

with open("data/nilai.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()

        if baris == "":
            continue

        nim, teks_nilai = baris.split(",")
        angka = float(teks_nilai)
        nilai.append(angka)

print("Daftar nilai:", nilai)
print(f"Rata-rata = {sum(nilai) / len(nilai):.2f}")