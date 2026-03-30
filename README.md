# Sistem Fuzzy untuk Menentukan Kecepatan Kipas Angin

Sistem ini menggunakan **logika fuzzy** untuk menentukan kecepatan kipas angin secara otomatis berdasarkan **suhu** dan **kelembapan** lingkungan. Sistem ini dibangun menggunakan **Python** dengan library **SciKit-Fuzzy** dan **Matplotlib** untuk visualisasi.

---

## Fitur

- Menentukan kecepatan kipas (Mati, Lambat, Sedang, Cepat) secara otomatis  
- Input berupa **suhu (0–40°C)** dan **kelembapan (0–100%)**  
- Visualisasi fungsi keanggotaan untuk setiap variabel  
- Simulasi output kecepatan kipas berdasarkan kondisi input tertentu  

---

## Variabel dan Fungsi Keanggotaan

**Input (Antecedent):**  
- **Suhu:** Dingin, Sejuk, Hangat, Panas  
- **Kelembapan:** Kering, Normal, Lembap  

**Output (Consequent):**  
- **Kecepatan Kipas:** Mati, Lambat, Sedang, Cepat  

Setiap kategori didefinisikan dengan **fungsi segitiga (triangular membership function)** untuk memetakan nilai input ke derajat keanggotaan fuzzy.

---

## Aturan Fuzzy (IF–THEN)

Contoh beberapa aturan dalam sistem:  

- Jika **suhu dingin**, maka **kipas mati**  
- Jika **suhu sejuk** dan **kelembapan kering**, maka **kipas lambat**  
- Jika **suhu sejuk** dan **kelembapan lembap**, maka **kipas sedang**  
- Jika **suhu hangat** dan **kelembapan lembap**, maka **kipas cepat**  
- Jika **suhu panas**, maka **kipas cepat**  

Secara total, terdapat **8 aturan fuzzy** yang menyesuaikan kecepatan kipas dengan kondisi lingkungan.

---

## Cara Menjalankan Program

1. Pastikan Python sudah terinstal  
2. Install library yang dibutuhkan:
```bash
pip install scikit-fuzzy scipy numpy packaging networkx matplotlib
```

---


## Nama : Zahratul Askia
## NIM : H1D024016
## Shift Awal : G
## Shift Akhir : F
