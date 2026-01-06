Search Engine Using Cosine Similarity

A Python-based search engine that ranks documents by relevance using Cosine Similarity. Queries and documents are converted into TF-IDF vectors, and similarity scores determine the most relevant results, demonstrating how NLP and vector-based methods enable effective document retrieval.

Project Members
Name              	Roll Number
BUSHRA KHALID      22SP-060-CS
LAYBA ASIF         22SP-060-CS


(Replace with your actual team members)

Project Description

This system implements a “Retrieve-and-Compare” architecture using Python and open-source libraries. It fetches content from web URLs, preprocesses it, converts it into TF-IDF vectors, and ranks documents by similarity to user queries using Cosine Similarity.

Key Features

Document Fetching: Fetch text from blog posts, articles, or any webpage using URLs.

Preprocessing: Converts text to lowercase, removes punctuation, tokenizes, removes stopwords, and keeps only meaningful words.

Vectorization: Transforms text into TF-IDF vectors for numerical representation.

Similarity Calculation: Computes Cosine Similarity between query and documents to rank relevance.

Interactive Web UI: Streamlit-based interface for easy comparison of documents.

Similarity Interpretation: Provides intuitive similarity labels:

🟢 Very Similar

🟡 Moderately Similar

🟠 Somewhat Similar

🔴 Not Similar

Prerequisites

Python 3.8+

Required libraries (install via pip install -r requirements.txt):

streamlit

requests

beautifulsoup4

nltk

scikit-learn

Demo / Reproducibility Steps

Follow these steps to run the project and verify its functionality:

Open a terminal in the project directory.

Run the application:

streamlit run app.py


Enter URLs:

Enter the first and second document/blog URLs in the input fields.

Click “Calculate Similarity”.

View Results:

The similarity score between the two documents will be displayed.

The app provides a visual interpretation:

Very Similar (≥ 0.7)

Moderately Similar (≥ 0.4)

Somewhat Similar (≥ 0.2)

Not Similar (< 0.2)

Example:

Similarity Score: 0.7823
🟢 Very Similar

How it Works

Text Extraction: Uses requests and BeautifulSoup to fetch web page content.

Cleaning & Preprocessing: Lowercase, punctuation removal, tokenization, stopword removal.

TF-IDF Vectorization: Converts preprocessed text into vectors.

Cosine Similarity: Calculates similarity score between vectors to rank relevance.

Interactive Display: Shows results on a Streamlit web interface.
