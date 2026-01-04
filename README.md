# Time Series Classification - Chinatown Melbourne

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=flat&logo=scikit-learn&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=flat&logo=python&logoColor=white)

Aplikasi web interaktif untuk mengklasifikasikan pola volume pejalan kaki per jam di Chinatown, Melbourne. Sistem ini menggunakan machine learning untuk mengidentifikasi apakah data yang diinput menunjukkan karakteristik hari kerja (weekday) atau akhir pekan (weekend).

## Deskripsi Proyek

Proyek ini memanfaatkan data time series volume pejalan kaki dalam periode 24 jam untuk menentukan tipe hari. Dengan memanfaatkan algoritma Random Forest dan model machine learning lainnya, aplikasi mampu mengenali pola aktivitas yang khas antara hari kerja dan akhir pekan berdasarkan distribusi keramaian sepanjang hari.

Aplikasi dilengkapi dengan interface yang user-friendly, memungkinkan pengguna untuk memasukkan data secara manual atau menggunakan template preset untuk eksplorasi cepat.

## Fitur Utama

- **Input Interaktif**: Masukkan data volume pejalan kaki untuk setiap jam (00:00 - 23:00) menggunakan number input yang mudah digunakan
- **Template Preset**: Tombol cepat untuk mencoba pola weekday dan weekend yang umum
- **Visualisasi Real-time**: Grafik dinamis yang menampilkan pola input dengan highlight pada rush hour pagi dan sore
- **Prediksi Instan**: Klasifikasi menggunakan model Random Forest dengan confidence score
- **Multiple Models**: Tersedia 4 model machine learning (Random Forest, SVM, Logistic Regression, ROCKET)
- **Interface Responsif**: Tampilan yang rapi dengan layout berbasis kolom dan tab

## Teknologi yang Digunakan

- **Frontend/UI**: Streamlit 1.52.1
- **Machine Learning**: Scikit-learn 1.7.2
- **Data Processing**: NumPy 2.3.5, Pandas 2.3.3
- **Visualization**: Matplotlib 3.10.7
- **Model Persistence**: Joblib 1.5.2

## Instalasi

1. Clone repository ini:

```bash
git clone https://github.com/edi-mj/time-series-classification.git
cd time-series-classification
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Pastikan folder `models/` berisi file model yang diperlukan:
   - `random_forest_model.pkl`
   - `logistic_regression_model.pkl`
   - `svm_model.pkl`
   - `rocket_model.pkl`

## Cara Menggunakan

1. Jalankan aplikasi Streamlit:

```bash
streamlit run app.py
```

2. Buka browser dan akses `http://localhost:8501`

3. Pilih salah satu opsi:

   - **Coba Pola Weekday**: Memuat template data hari kerja
   - **Coba Pola Weekend**: Memuat template data akhir pekan
   - **Manual Input**: Masukkan nilai sendiri untuk setiap jam

4. Klik tombol **Prediksi Hari** untuk melihat hasil klasifikasi

## Struktur Proyek

```
time-series-classification/
│
├── app.py                              # Aplikasi utama Streamlit
├── requirements.txt                    # Daftar dependencies
├── models/                             # Folder berisi trained models
│   ├── random_forest_model.pkl
│   ├── logistic_regression_model.pkl
│   ├── svm_model.pkl
│   └── rocket_model.pkl
└── README.md                           # Dokumentasi proyek
```

## Detail Implementasi

### Input Data

Aplikasi menerima 24 nilai numerik yang merepresentasikan volume pejalan kaki per jam (00:00 - 23:00). Input dibagi menjadi 4 tab berdasarkan periode waktu:

- Dini Hari (00:00 - 05:00)
- Pagi (06:00 - 11:00)
- Siang (12:00 - 17:00)
- Malam (18:00 - 23:00)

### Klasifikasi

Model machine learning menghasilkan dua kemungkinan output:

- **Class 1**: Weekend (Akhir Pekan)
- **Class 2**: Weekday (Hari Kerja)

Setiap prediksi dilengkapi dengan confidence score yang menunjukkan tingkat keyakinan model.

## Kontribusi

Kontribusi sangat terbuka untuk pengembangan fitur baru, perbaikan bug, atau peningkatan dokumentasi. Silakan buat pull request atau laporkan issue di repository ini.

## Lisensi

Proyek ini bersifat open source dan tersedia untuk keperluan edukasi dan penelitian.

## Catatan Teknis

- Model utama yang digunakan adalah Random Forest Classifier
- Aplikasi menggunakan session state untuk persistensi input
- Visualisasi menggunakan matplotlib dengan highlight area rush hour
- Model di-cache menggunakan `@st.cache_resource` untuk performa optimal

---

Dikembangkan dengan Python dan Streamlit untuk analisis time series classification.
