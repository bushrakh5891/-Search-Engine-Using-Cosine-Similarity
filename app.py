import streamlit as st
import requests
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download NLTK data (only first time)
@st.cache_resource
def download_nltk_data():
    nltk.download('punkt')
    nltk.download('stopwords')

download_nltk_data()

# Function to fetch and extract text from URL
def get_text_from_url(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Remove unwanted parts
        for script in soup(["script", "style", "header", "footer", "nav", "aside"]):
            script.extract()
        
        text = soup.get_text(separator=' ')
        
        # Clean text
        text = text.lower()
        text = text.translate(str.maketrans('', '', string.punctuation))
        tokens = word_tokenize(text)
        stop_words = set(stopwords.words('english'))
        filtered_tokens = [word for word in tokens if word not in stop_words and word.isalpha() and len(word) > 2]
        
        return ' '.join(filtered_tokens)
    
    except Exception as e:
        return f"Error: Could not fetch {url} → {str(e)}"

# Web App UI
st.set_page_config(page_title="Blog Similarity Checker", page_icon="🔍", layout="centered")
st.title("🔍 Blog Similarity Checker")
st.markdown("### Compare how similar two blog posts or articles are")

col1, col2 = st.columns(2)
with col1:
    url1 = st.text_input("First URL", placeholder="https://example.com/blog1")
with col2:
    url2 = st.text_input("Second URL", placeholder="https://example.com/blog2")

if st.button("Calculate Similarity", type="primary", use_container_width=True):
    if not url1 or not url2:
        st.error("Please enter both URLs!")
    else:
        with st.spinner("Fetching and comparing content..."):
            text1 = get_text_from_url(url1)
            text2 = get_text_from_url(url2)
            
            if "Error" in text1 or "Error" in text2:
                st.error(text1 if "Error" in text1 else text2)
            else:
                vectorizer = TfidfVectorizer()
                tfidf_matrix = vectorizer.fit_transform([text1, text2])
                similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
                
                st.success(f"**Similarity Score: {similarity:.4f}**")
                if similarity >= 0.7:
                    st.balloons()
                    st.markdown("🟢 **Very Similar**")
                elif similarity >= 0.4:
                    st.markdown("🟡 **Moderately Similar**")
                elif similarity >= 0.2:
                    st.markdown("🟠 **Somewhat Similar**")
                else:
                    st.markdown("🔴 **Not Similar**")

st.markdown("---")
st.caption("NLP End-Term Project | TF-IDF + Cosine Similarity")