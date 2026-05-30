import pandas as pd


FAQ_RULES = {
    "parkir": "Apakah tersedia area parkir?",
    "toilet": "Bagaimana kondisi toilet?",
    "harga": "Berapa kisaran harga tiket masuk?",
    "tiket": "Berapa kisaran harga tiket masuk?",
    "akses": "Bagaimana akses menuju lokasi wisata?",
    "jalan": "Bagaimana akses menuju lokasi wisata?",
    "foto": "Apakah tersedia spot foto menarik?",
    "spot": "Apakah tersedia spot foto menarik?",
    "kuliner": "Apakah tersedia kuliner di lokasi?",
    "makanan": "Apakah tersedia kuliner di lokasi?",
    "restoran": "Apakah tersedia kuliner di lokasi?",
    "bersih": "Bagaimana tingkat kebersihan lokasi wisata?",
    "kebersihan": "Bagaimana tingkat kebersihan lokasi wisata?",
    "pantai": "Apa daya tarik utama pantai ini?",
    "air": "Bagaimana kondisi area perairan di lokasi wisata?",
    "wahana": "Apa saja wahana yang tersedia?",
    "anak": "Apakah lokasi cocok untuk anak-anak?",
    "keluarga": "Apakah lokasi cocok untuk keluarga?",
    "view": "Bagaimana kualitas pemandangan di lokasi?",
    "pemandangan": "Bagaimana kualitas pemandangan di lokasi?",
    "sunset": "Apakah lokasi memiliki pemandangan sunset yang menarik?",
    "camping": "Apakah tersedia area camping?",
    "hotel": "Apakah tersedia penginapan di sekitar lokasi?",
    "penginapan": "Apakah tersedia penginapan di sekitar lokasi?"
}


def generate_answer(keyword, reviews):

    matched_reviews = []

    for review in reviews:

        if keyword.lower() in review.lower():
            matched_reviews.append(review)

    if len(matched_reviews) == 0:
        return (
            f"Beberapa pengunjung memberikan ulasan terkait "
            f"aspek '{keyword}'."
        )

    unique_reviews = list(dict.fromkeys(matched_reviews))

    summary = "; ".join(unique_reviews[:5])

    return (
        "Berdasarkan review pengunjung: "
        + summary
    )


def generate_faq(tfidf_df, reviews, faq_count):

    faq_data = []

    for keyword, question in FAQ_RULES.items():

        matched = tfidf_df[
            tfidf_df["keyword"].str.contains(
                keyword,
                case=False,
                na=False
            )
        ]

        if matched.empty:
            continue

        score = matched["score"].max()

        answer = generate_answer(
            keyword,
            reviews
        )

        faq_data.append({
            "Score": score,
            "Pertanyaan": question,
            "Jawaban": answer
        })

    faq_df = pd.DataFrame(faq_data)

    if faq_df.empty:
        return pd.DataFrame(
            columns=[
                "Pertanyaan",
                "Jawaban"
            ]
        )

    faq_df = faq_df.sort_values(
        by="Score",
        ascending=False
    )

    faq_df = faq_df.drop_duplicates(
        subset=["Pertanyaan"]
    )

    faq_df = faq_df.head(faq_count)

    faq_df = faq_df[
        ["Pertanyaan", "Jawaban"]
    ]

    return faq_df