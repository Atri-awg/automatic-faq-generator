import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer


def extract_tfidf_scores(texts):

    vectorizer = TfidfVectorizer()

    tfidf_matrix = vectorizer.fit_transform(texts)

    feature_names = vectorizer.get_feature_names_out()

    scores = tfidf_matrix.sum(axis=0)

    scores_df = pd.DataFrame({
        "keyword": feature_names,
        "score": scores.A1
    })

    scores_df = scores_df.sort_values(
        by="score",
        ascending=False
    )

    return scores_df