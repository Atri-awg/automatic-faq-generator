import pandas as pd

FAQ_RULES = {
    "parkir": "Apakah tersedia area parkir?",
    "toilet": "Bagaimana kondisi toilet?",
    "harga": "Berapa kisaran harga tiket masuk?",
    "tiket": "Berapa kisaran harga tiket masuk?",
    "jalan": "Bagaimana akses menuju lokasi wisata?",
    "akses": "Bagaimana akses menuju lokasi wisata?",
    "foto": "Apakah tersedia spot foto menarik?",
    "makanan": "Apakah tersedia makanan atau kuliner di lokasi?",
    "kuliner": "Apakah tersedia makanan atau kuliner di lokasi?",
    "bersih": "Bagaimana tingkat kebersihan lokasi wisata?",
    "kebersihan": "Bagaimana tingkat kebersihan lokasi wisata?"
}


def generate_question(keyword):

    for rule_keyword, question in FAQ_RULES.items():

        if rule_keyword in keyword.lower():
            return question

    return f"Apa informasi mengenai '{keyword}' yang perlu diketahui pengunjung?"


def generate_answer(keyword, reviews):

    matched_reviews = []

    for review in reviews:

        if keyword.lower() in review.lower():
            matched_reviews.append(review)

    if not matched_reviews:
        return (
            f"Beberapa pengunjung menyebutkan '{keyword}' "
            f"sebagai aspek yang menarik untuk diperhatikan."
        )

    unique_reviews = list(dict.fromkeys(matched_reviews))

    summary = "; ".join(unique_reviews[:5])

    return (
        "Berdasarkan review pengunjung: "
        + summary
    )


def generate_faq(tfidf_df, reviews, faq_count):

    faq_data = []

    used_questions = set()

    top_keywords = tfidf_df.head(faq_count * 5)

    for _, row in top_keywords.iterrows():

        keyword = row["keyword"]

        question = generate_question(keyword)

        if question in used_questions:
            continue

        answer = generate_answer(
            keyword,
            reviews
        )

        faq_data.append({
            "Pertanyaan": question,
            "Jawaban": answer
        })

        used_questions.add(question)

        if len(faq_data) >= faq_count:
            break

    return pd.DataFrame(faq_data)