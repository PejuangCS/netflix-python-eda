# 🎬 Netflix Data Analysis & Movie Recommender

Repositori ini berisi proyek *Exploratory Data Analysis* (EDA) dan pembuatan prototipe Mesin Pencari Rekomendasi Film menggunakan dataset dunia nyata dari Netflix. Fokus utama proyek ini adalah membersihkan data mentah (*data wrangling*) dan menarik wawasan bisnis mengenai tren strategis konten platform *streaming*.

## 🛠️ Tech Stack
- **Bahasa:** Python
- **Library Utama:** Pandas (Data Profiling & Cleaning), Matplotlib (Data Visualization)
- **Environment:** Jupyter Notebook

---

## 📊 Fase 1: Data Profiling & Cleaning
Dataset asli memiliki ~7.787 baris dengan berbagai anomali (*Missing Values*). Keputusan strategis yang dilakukan:
* **Imputasi (Fill):** Mengisi nilai yang hilang pada kolom `director`, `cast`, dan `country` (tingkat kekosongan hingga 30%) dengan label `'Unknown'` untuk menyelamatkan dan mempertahankan struktur data.
* **Penghapusan (Drop):** Membuang anomali sangat kecil (< 1%) pada kolom `date_added` dan `rating` untuk menjaga integritas analisis waktu tanpa mengurangi validitas statistik.

## 📈 Fase 2: Exploratory Data Analysis (EDA) & Business Insights
Proyek ini menjawab 3 pertanyaan bisnis utama melalui visualisasi data:
1. **Ledakan Konten:** Ditemukan lonjakan penambahan konten raksasa pada rentang 2015-2019 (menandakan era ekspansi global Netflix), yang kemudian terhenti drastis di tahun 2020 akibat berhentinya produksi karena pandemi global.
2. **Proporsi Movie vs TV Show:** Kategori *Movie* mendominasi platform. Secara bisnis, hal ini menekan *budget* lisensi sekaligus berfungsi sebagai alat akuisisi pengguna baru melalui variasi katalog yang masif.
3. **Peta Produsen Konten:** Amerika Serikat menduduki peringkat pertama, namun secara mengejutkan **India berada di peringkat kedua**, menunjukkan keberhasilan strategi akuisisi film Bollywood oleh Netflix untuk mendominasi pasar Asia.

---

## 🔍 Fase 3: Feature Engineering (Mesin Pencari Film)
Membangun purwarupa sistem rekomendasi film sederhana berbasis filter multi-kondisi (`multiple conditions filtering`) menggunakan Pandas.
* **Fitur:** Pengguna dapat memasukkan kata kunci "Kategori/Genre" dan "Tahun Rilis Minimal".
* **Logika:** Menggunakan metode ekstraksi *string* (`str.contains()`) untuk mencari irisan teks genre secara dinamis dan menampilkan 5 rekomendasi teratas berdasarkan urutan perilisan paling baru.

## 🚀 Cara Menjalankan Proyek Ini
1. *Clone* repositori ini ke komputer lokal Anda.
2. Pastikan file `NetFlix.csv` dan file `.ipynb` (Jupyter Notebook) berada di dalam folder yang sama.
3. Instal dependensi dengan menjalankan perintah: `pip install pandas matplotlib`
4. Buka file Jupyter Notebook dan jalankan setiap *cell* secara berurutan untuk melihat proses pembersihan, kemunculan grafik, dan hasil mesin rekomendasi.