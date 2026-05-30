# Automatic FAQ Generator untuk Review Wisata Indonesia

## Deskripsi

Aplikasi web untuk mengubah kumpulan review wisata menjadi FAQ secara otomatis menggunakan:

- Rule-Based
- TF-IDF

Tanpa menggunakan:

- Machine Learning Classification
- Clustering
- LDA
- Word Embedding
- Deep Learning
- LLM

---

## Struktur Folder

```text
automatic-faq-generator/

app.py

modules/
├── preprocessing.py
├── tfidf_processor.py
└── faq_generator.py

requirements.txt
README.md
```

---

## Format CSV

Contoh:

```csv
review
Parkir luas dan nyaman
Toilet bersih dan terawat
Harga tiket cukup murah
Jalan menuju lokasi bagus
```

---

## Instalasi

Buat virtual environment (opsional):

```bash
python -m venv venv
```

Aktifkan:

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

Install dependency:

```bash
pip install -r requirements.txt
```

---

## Menjalankan Aplikasi

```bash
streamlit run app.py
```

---

## Alur Sistem

1. Upload CSV review
2. Preprocessing
   - lowercase
   - remove punctuation
   - remove angka
   - stopword removal (Sastrawi)
   - stemming (Sastrawi)
3. TF-IDF Analysis
4. Ambil keyword dengan skor tertinggi
5. Rule-Based FAQ Generation
6. Generate Answer dari review terkait
7. Download FAQ CSV

---

## Metode

### TF-IDF

Menggunakan:

```python
from sklearn.feature_extraction.text import TfidfVectorizer
```

untuk menemukan keyword dominan dari kumpulan review.

### Rule-Based

Keyword dipetakan ke template pertanyaan FAQ.

Contoh:

- parkir → Apakah tersedia area parkir?
- toilet → Bagaimana kondisi toilet?
- harga → Berapa kisaran harga tiket masuk?

Jika keyword tidak ditemukan:

- Apa yang perlu diketahui pengunjung mengenai tempat wisata ini?s