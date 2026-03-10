
# Laporan Smart Farming - Data Lifecycle Management
## Studi Kasus 1: Sensor IoT Pertanian

### 1. Deskripsi Project
Project ini bertujuan untuk mengelola data sensor IoT (Soil Moisture, pH, Temp) guna memprediksi Yield (hasil panen).

### 2. Implementasi 6 Tahapan DLM (Halaman 4)
* **Acquisition**: Mengambil data dari Kaggle via API.
* **Storage**: Data mentah disimpan di `data/raw/`.
* **Processing**: Pembersihan data null (Completeness) disimpan di `outputs/cleaned_data.csv`.
* **Analysis**: Korelasi heatmap menunjukkan hubungan antar sensor.
* **Visualization**: Dashboard tren sensor untuk monitoring real-time.
* **Governance**: Penerapan standar kualitas data (Akurasi & Kelengkapan).

### 3. Metrik Kualitas Data (Halaman 25)
* **Completeness**: 100% (Baris kosong telah dihapus).
* **Accuracy**: Data sensor tervalidasi dalam rentang normal (pH 5.5 - 7.5).
* **Timeliness**: Dataset mencakup data tahun 2024.
