from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')


def get_similarity(d1,d2):   
    r'''
    Returns the Cosine similarity score between 2 documents 
    Args:
    d1 (String): Document 1
    d2 (String): Document 2   
    ''' 
    sw = set(stopwords.words('english'))
    d1 = ' '.join([word for word in d1.split() if word not in sw])
    d2 = ' '.join([word for word in d2.split() if word not in sw])

    corpus = [d1,d2]
    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform(corpus)    # Learn vocabulary and idf. Returns the document-term matrix.
    sim_matrix = cosine_similarity(tfidf)       # Computes cosine similarity between samples in X and Y
    score = sim_matrix[0,1]  # or [1,0]
    score = round(score*100,2)

    return score

