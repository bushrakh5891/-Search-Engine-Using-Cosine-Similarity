
# Search Engine Using Cosine Similarity

A Python-based search engine that ranks documents by **relevance** using **Cosine Similarity**. Queries and documents are converted into **TF-IDF vectors**, and similarity scores determine the most relevant results, demonstrating how **NLP** and vector-based methods enable effective document retrieval.

---

## Project Members

| Name          | Roll Number |
| ------------- | ----------- |
| Bushra Khalid | 22SP-060-CS |
| Layba Asif    | 22SP-062-CS |

---

## Project Description

This system implements a **“Retrieve-and-Compare” architecture** using Python and open-source libraries. It fetches content from web URLs, preprocesses it, converts it into **TF-IDF vectors**, and ranks documents by similarity to user queries using **Cosine Similarity**.

---

## Key Features

* **Document Fetching:** Fetch text from blog posts, articles, or any webpage using URLs.
* **Preprocessing:** Converts text to lowercase, removes punctuation, tokenizes, removes stopwords, and keeps only meaningful words.
* **Vectorization:** Transforms text into **TF-IDF vectors** for numerical representation.
* **Similarity Calculation:** Computes **Cosine Similarity** between query and documents to rank relevance.
* **Interactive Web UI:** Streamlit-based interface for easy comparison of documents.
* **Similarity Interpretation:** Provides intuitive similarity labels:

  * 🟢 Very Similar (≥ 0.7)
  * 🟡 Moderately Similar (≥ 0.4)
  * 🟠 Somewhat Similar (≥ 0.2)
  * 🔴 Not Similar (< 0.2)

---

## Prerequisites

* Python 3.8+
* Required libraries (install via `pip install -r requirements.txt`):

  * `streamlit`
  * `requests`
  * `beautifulsoup4`
  * `nltk`
  * `scikit-learn`

---

## Demo / Reproducibility Steps

Follow these steps to run the project and verify its functionality:

1. **Open a terminal** in the project directory.

2. **Run the application:**

```bash
streamlit run app.py
```

3. **Enter URLs:**

* Enter the first and second document/blog URLs in the input fields.
* Click **“Calculate Similarity”**.

4. **View Results:**

* The similarity score between the two documents will be displayed.
* The app provides a visual interpretation:

  * 🟢 Very Similar (≥ 0.7)
  * 🟡 Moderately Similar (≥ 0.4)
  * 🟠 Somewhat Similar (≥ 0.2)
  * 🔴 Not Similar (< 0.2)

5. **Example Output:**

```
Similarity Score: 0.7823
🟢 Very Similar
```

---

## How it Works

1. **Text Extraction:** Uses `requests` and `BeautifulSoup` to fetch web page content.
2. **Cleaning & Preprocessing:** Lowercase, punctuation removal, tokenization, stopword removal.
3. **TF-IDF Vectorization:** Converts preprocessed text into numerical vectors.
4. **Cosine Similarity:** Calculates similarity score between vectors to rank relevance.
5. **Interactive Display:** Shows results on a Streamlit web interface.

---

<img width="1360" height="678" alt="image" src="https://github.com/user-attachments/assets/d6a27797-5364-4919-8a3b-b22f9a6fd019" />

<img width="1353" height="688" alt="image" src="https://github.com/user-attachments/assets/ce221af9-eb28-4ee6-b5ab-05d08b1572fe" />

