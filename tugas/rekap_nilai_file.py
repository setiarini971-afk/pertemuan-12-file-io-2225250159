# Fungsi membaca dan memvalidasi data
def baca_data(nama_file):
    data = []

    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for nomor, baris in enumerate(file, start=1):
                baris = baris.strip()

                if not baris:
                    continue

                try:
                    nim, teks_nilai = baris.split(",")
                    nilai = float(teks_nilai)

                    data.append((nim.strip(), nilai))

                except ValueError:
                    print(f"Baris {nomor} dilewati: {baris}")

    except FileNotFoundError:
        print(f"File tidak ditemukan: {nama_file}")

    return data


# Fungsi menulis hasil rekap
def tulis_rekap(nama_file, data):
    if not data:
        print("Tidak ada data valid untuk direkap.")
        return

    nilai = [item[1] for item in data]

    jumlah_data = len(nilai)
    rata_rata = sum(nilai) / jumlah_data
    minimum = min(nilai)
    maksimum = max(nilai)

    jumlah_lulus = sum(1 for x in nilai if x >= 60)

    with open(nama_file, "w", encoding="utf-8") as file:
        file.write(f"Jumlah data valid: {jumlah_data}\n")
        file.write(f"Rata-rata: {rata_rata:.2f}\n")
        file.write(f"Minimum: {minimum:.2f}\n")
        file.write(f"Maksimum: {maksimum:.2f}\n")
        file.write(f"Jumlah lulus: {jumlah_lulus}\n")


# Program utama
input_file = "data/nilai.txt"
output_file = "data/hasil_rekap.txt"

data = baca_data(input_file)

if data:
    tulis_rekap(output_file, data)

    print("\nRekap nilai berhasil dibuat.")
    print("Jumlah data valid:", len(data))
    print(f"Rata-rata: {sum(item[1] for item in data) / len(data):.2f}")
    print("Hasil disimpan di:", output_file)