# Automatic FAQ Generator untuk Review Wisata Indonesia

## Deskripsi

Automatic FAQ Generator merupakan aplikasi web berbasis Streamlit yang digunakan untuk menghasilkan Frequently Asked Questions (FAQ) secara otomatis dari kumpulan review wisata Indonesia.

Aplikasi ini memanfaatkan metode:

* TF-IDF (Term Frequency-Inverse Document Frequency)
* Rule-Based FAQ Generation

Sistem dirancang untuk membantu pengelola destinasi wisata maupun peneliti dalam mengubah review pengunjung menjadi informasi FAQ yang lebih terstruktur dan mudah dipahami.

---

## Metode yang Digunakan

### 1. Preprocessing Teks

Setiap review akan melalui tahapan:

* Lowercase
* Remove punctuation
* Remove angka
* Stopword removal menggunakan Sastrawi
* Custom stopword removal
* Stemming menggunakan Sastrawi

### 2. TF-IDF

Menggunakan:

```python
from sklearn.feature_extraction.text import TfidfVectorizer
```

untuk mengidentifikasi kata-kata penting yang sering muncul pada review wisata.

### 3. Aspect-Based Filtering

Keyword hasil TF-IDF difilter menggunakan daftar aspek wisata yang telah ditentukan, seperti:

* Parkir
* Toilet
* Harga
* Tiket
* Kuliner
* Kebersihan
* Pantai
* Wahana
* Pemandangan
* Penginapan
* Akses

Tujuannya untuk menghilangkan keyword yang tidak relevan seperti:

* sangat
* bagus
* mantap
* lumayan
* rekomendasi

### 4. Rule-Based FAQ Generation

Setiap aspek wisata dipetakan ke template pertanyaan tertentu.

Contoh:

| Keyword     | FAQ                                       |
| ----------- | ----------------------------------------- |
| parkir      | Apakah tersedia area parkir?              |
| toilet      | Bagaimana kondisi toilet?                 |
| harga       | Berapa kisaran harga tiket masuk?         |
| kuliner     | Apakah tersedia kuliner di lokasi?        |
| pemandangan | Bagaimana kualitas pemandangan di lokasi? |

### 5. Answer Generation

Jawaban FAQ dibentuk dari kumpulan review yang mengandung keyword terkait.

Contoh:

Review:

* Parkir luas dan nyaman
* Area parkir cukup besar
* Parkir tersedia di dekat pintu masuk

FAQ:

Pertanyaan:

Apakah tersedia area parkir?

Jawaban:

Berdasarkan review pengunjung: Parkir luas dan nyaman; Area parkir cukup besar; Parkir tersedia di dekat pintu masuk.

---

## Batasan Penelitian

Penelitian ini hanya menggunakan:

* Rule-Based
* TF-IDF

Tidak menggunakan:

* Machine Learning Classification
* K-Means
* DBSCAN
* LDA
* Word2Vec
* FastText
* BERT
* Sentence Transformer
* Deep Learning
* OpenAI API
* Large Language Model (LLM)
* LangChain

---

## Teknologi yang Digunakan

* Python
* Streamlit
* Pandas
* Scikit-learn
* Sastrawi

---

## Struktur Folder

```text
automatic-faq-generator/

├── app.py
│
├── modules/
│   ├── preprocessing.py
│   ├── tfidf_processor.py
│   └── faq_generator.py
│
├── requirements.txt
└── README.md
```

---

## Format Dataset

File CSV harus memiliki kolom:

```csv
review
```

Contoh:

```csv
review
Parkir luas dan nyaman
Toilet bersih dan terawat
Harga tiket cukup murah
Spot foto menarik
Jalan menuju lokasi bagus
```

---

## Fitur Aplikasi

### Upload Dataset Review

User dapat mengunggah file CSV berisi review wisata.

### Preprocessing Otomatis

Review akan dibersihkan dan dinormalisasi secara otomatis.

### Analisis TF-IDF

Mengidentifikasi keyword penting dari kumpulan review.

### Generate FAQ Otomatis

Menghasilkan FAQ berdasarkan aspek wisata yang ditemukan.

### Pengaturan Jumlah FAQ

User dapat menentukan jumlah FAQ yang ingin dihasilkan.

### Dashboard Statistik

Menampilkan:

* Jumlah Review
* Jumlah FAQ Dihasilkan

### Download FAQ

Hasil FAQ dapat diunduh dalam format CSV.

---

## Instalasi

Clone repository:

```bash
git clone https://github.com/username/automatic-faq-generator.git
```

Masuk ke folder project:

```bash
cd automatic-faq-generator
```

Install dependency:

```bash
pip install -r requirements.txt
```

---

## Menjalankan Aplikasi

```bash
python -m streamlit run app.py
```

Aplikasi akan berjalan pada:

```text
http://localhost:8501
```

---

## Contoh Output FAQ

| No | Pertanyaan                                | Jawaban                                                                           |
| -- | ----------------------------------------- | --------------------------------------------------------------------------------- |
| 1  | Apakah tersedia area parkir?              | Berdasarkan review pengunjung: Parkir luas dan nyaman; Area parkir cukup besar    |
| 2  | Bagaimana kondisi toilet?                 | Berdasarkan review pengunjung: Toilet bersih dan terawat                          |
| 3  | Berapa kisaran harga tiket masuk?         | Berdasarkan review pengunjung: Harga tiket cukup murah                            |
| 4  | Apakah tersedia kuliner di lokasi?        | Berdasarkan review pengunjung: Banyak pilihan makanan dan minuman                 |
| 5  | Bagaimana kualitas pemandangan di lokasi? | Berdasarkan review pengunjung: Pemandangan sangat indah dan cocok untuk fotografi |

---

## Pengembangan Selanjutnya

Beberapa pengembangan yang dapat dilakukan:

* Ekspansi daftar aspek wisata
* Visualisasi keyword TF-IDF
* Analisis sentimen berbasis Rule-Based
* Integrasi database
* Deployment ke Streamlit Community Cloud

---

## Lisensi

Project ini dikembangkan untuk kebutuhan penelitian dan pembelajaran Text Mining menggunakan metode TF-IDF dan Rule-Based.
