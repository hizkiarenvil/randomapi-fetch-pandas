
# Random Users Data Pipeline

Proyek ini adalah contoh sederhana pipeline data yang mengambil data pengguna acak dari [RandomUser.me API](https://randomuser.me/), memproses data tersebut menggunakan Python, dan menghasilkan output dalam format CSV dan file statistik teks. Proyek ini cocok untuk belajar dan menguji konsep ETL (Extract, Transform, Load) serta analisis data menggunakan Python.

## Fitur

- **Pengambilan Data Otomatis:** Mengambil data acak (default: 50 pengguna) dari API.
- **Pemrosesan Data:** Parsing dan pemrosesan data untuk mendapatkan informasi seperti nama depan, nama belakang, email, umur, gender, lokasi, dan nomor telepon.
- **Analisis Statistik Dasar:** Menampilkan informasi dataset, statistik usia, distribusi gender, dan jumlah pengguna per negara.
- **Ekspor Data:** Menyimpan data yang telah diproses ke dalam file CSV dan statistik ke dalam file teks.
- **Otomatisasi Folder Output:** Membuat folder `data` secara otomatis jika belum ada.

## Prasyarat

Pastikan Anda telah menginstal:
- **Python 3.x** (disarankan versi 3.9 atau lebih baru)
- Modul Python: `requests`, `pandas`

Untuk menginstal dependensi, jalankan perintah:
```bash
pip install requests pandas
```

## Cara Menggunakan

1. **Clone Repository:**
   ```bash
   git clone https://github.com/username/repo-name.git
   ```
2. **Masuk ke Direktori Proyek:**
   ```bash
   cd repo-name
   ```
3. **Jalankan Script:**
   ```bash
   python random_data.py
   ```

Script akan melakukan:
- Mengambil 50 data pengguna acak dari API.
- Mengonversi data menjadi DataFrame dan mencetak informasi serta statistik dasar.
- Menyimpan output ke dalam folder `data`:
  - CSV file dengan nama `random_users_<timestamp>.csv`
  - File teks `user_stats.txt` yang berisi statistik dasar dataset.

## Struktur Proyek

```
repo-name/
├── data/                   # Folder output untuk CSV dan file statistik (otomatis dibuat)
├── random_data.py          # Script Python utama
└── README.md               # Dokumentasi proyek ini
```

## Penjelasan Kode

- **get_random_users(num_users=10):**  
  Fungsi untuk mengambil data pengguna acak dari RandomUser.me API dan memprosesnya menjadi list of dictionaries dengan field seperti `first_name`, `last_name`, `email`, `age`, `gender`, `country`, `city`, `street`, `phone`, dan `nationality`.

- **main():**  
  Fungsi utama yang:
  - Mengambil 50 data pengguna acak.
  - Mengonversi data ke DataFrame menggunakan Pandas.
  - Menampilkan informasi dataset (info, statistik usia, distribusi gender, dan jumlah pengguna per negara).
  - Mengekspor data ke file CSV dan menyimpan statistik ke file teks di dalam folder `data`.

## Kontribusi

Jika Anda ingin berkontribusi pada proyek ini:
1. Fork repository ini.
2. Buat branch baru untuk fitur atau perbaikan bug.
3. Kirimkan pull request dengan deskripsi perubahan Anda.

