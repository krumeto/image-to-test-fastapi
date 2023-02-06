from keybert import KeyBERT
from sentence_transformers import SentenceTransformer


def extract_keywords(text: str):
    """a simple keybert based keywords extraction

    Args:
        text (list of strings): list of strings to get keywords for
    """
    sentence_model = SentenceTransformer("all-MiniLM-L6-v2")
    sentence_model.max_seq_length = 512
    
    kw_model = KeyBERT(model=sentence_model)
    
    keywords = kw_model.extract_keywords(text, 
                                         keyphrase_ngram_range=(2, 5), 
                                         stop_words='english',
                                         use_maxsum=True, 
                                         nr_candidates=20, 
                                         top_n=5)
    return keywords
