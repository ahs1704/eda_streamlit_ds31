# eda_streamlit_ds31
# 📊 Superstore EDA Dashboard

Aplikasi visualisasi interaktif berbasis Streamlit untuk menganalisis data penjualan Superstore.

## 🚀 Fitur Utama

- 📂 Upload file dalam format CSV, XLSX, atau JSON
- 📅 Filter data berdasarkan rentang tanggal
- 🌍 Filter berdasarkan Region, State, dan City
- 📈 Visualisasi:
  - Bar chart penjualan per kategori
  - Pie chart penjualan per region dan segment
  - Line chart penjualan bulanan (time series)
  - Tree map kombinasi Region, Category, Sub-Category
  - Tabel ringkasan penjualan

## 🛠️ Teknologi

- Python
- Streamlit
- Plotly
- Pandas

## 📦 Instalasi

1. Clone repo:
   ```bash
   git clone https://github.com/ahs1704/eda_streamlit_ds31.git
   cd superstore-eda-dashboard

### Buat dan aktifkan virtual environment:
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

### Install dependencies:
pip install -r requirements.txt

### Menjalankan Aplikasi
streamlit run app.py


## Struktur Proyek
.
├── app.py                   # Aplikasi utama Streamlit
├── Sample - Superstore.csv  # Contoh dataset
├── requirements.txt         # Daftar library
├── README.md                # Dokumentasi proyek

File `Sample - Superstore.csv` sudah tersedia di repo.  
Jalankan aplikasi dengan:
streamlit run dashboard_eda.py

