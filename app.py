import streamlit as st
import pandas as pd

from modules.preprocessing import preprocess_text
from modules.tfidf_processor import extract_tfidf_scores
from modules.faq_generator import generate_faq


st.set_page_config(
    page_title="Automatic FAQ Generator",
    layout="wide"
)

st.title("Automatic FAQ Generator untuk Review Desa Wisata")

st.markdown("""
Sistem menghasilkan FAQ secara otomatis menggunakan:

- Rule-Based
- TF-IDF
""")

uploaded_file = st.file_uploader(
    "Upload CSV Review",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    if "review" not in df.columns:
        st.error("CSV harus memiliki kolom 'review'")
        st.stop()

    df = df.dropna()

    st.subheader("Data Review")
    st.dataframe(df.head())

    # Input jumlah FAQ dari user
    faq_count = st.number_input(
        "Jumlah FAQ yang ingin dihasilkan",
        min_value=1,
        max_value=50,
        value=10,
        step=1
    )

    # cek jumlah FAQ yang diminta user
    # st.write("FAQ yang diminta:", faq_count)

    # Preprocessing
    df["processed_review"] = df["review"].apply(
        preprocess_text
    )

    keyword_df = extract_tfidf_scores(
    df["processed_review"]
    )

    # cek 20 keyword teratas buat ditampilin di dashboard
    # st.subheader("20 Keyword TF-IDF Teratas")

    # st.dataframe(
    #     keyword_df.head(20)
    # )

    # Generate FAQ
    faq_df = generate_faq(
        keyword_df,
        df["review"].tolist(),
        faq_count
    )

    # Batasi sesuai jumlah FAQ yang diminta user
    faq_df = faq_df.head(faq_count)

    st.subheader("Dashboard")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Jumlah Review",
            len(df)
        )

    with col2:
        st.metric(
    "Jumlah FAQ Dihasilkan",
    len(faq_df)
    )

    st.subheader("Top Keyword TF-IDF")
    st.dataframe(keyword_df)

    st.subheader("FAQ Hasil Generasi")

    faq_df.index = range(1, len(faq_df) + 1)
    st.dataframe(
        faq_df,
        use_container_width=True
    )

    csv = faq_df.to_csv(
        index=False
    ).encode("utf-8-sig")

    st.download_button(
        label="Download FAQ CSV",
        data=csv,
        file_name="faq_wisata.csv",
        mime="text/csv"
    )