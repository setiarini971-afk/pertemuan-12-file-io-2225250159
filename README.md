# Pertemuan 12 - File I/O dan Error Handling

Nama: Ririn Setiarini
NIM: 2225250159
Kelas: F

## Tujuan
Mempelajari cara membaca, menulis, memproses,
dan memvalidasi data menggunakan file Python.

## Materi
- File Input-Output
- Mode r, w, dan a
- read(), readline(), readlines()
- strip() dan split()
- try-except
- FileNotFoundError
- ValueError
- Fungsi baca dan tulis file

## Struktur Folder
- data/
- latihan/
- tugas/
- README.md

## Format File Input
NIM,nilai

Contoh:
A001,85
A002,78
A003,92

## Cara Menjalankan
python latihan/01_tulis_file.py
python latihan/02_baca_file.py
python latihan/03_append_file.py
python latihan/04_proses_baris.py
python latihan/05_file_not_found.py
python latihan/06_value_error.py
python tugas/rekap_nilai_file.py

## Error yang Ditangani
- FileNotFoundError
- ValueError

## Test Case
1. Semua data valid.
2. File tidak ditemukan.
3. Nilai tidak valid.
4. Terdapat baris kosong.
5. Nilai tepat 60 dihitung lulus.

## Refleksi
Saya memahami bahwa file dapat digunakan
untuk menyimpan data agar tetap tersedia
setelah program selesai. Saya juga mempelajari
cara menangani kesalahan menggunakan
try-except agar program tetap memberikan
pesan yang jelas ketika terjadi kesalahan.