from nltk_utils import tokenize
import nltk
from nltk.corpus import stopwords
from documents import JavaScript_scrape
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel       
from nltk.stem import WordNetLemmatizer

# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('wordnet')
stop_words = set(stopwords.words('english')) 
class LemmaTokenizer:
    ignore_tokens = [',', '.', ';', ':', '"', '``', "''", '`']
    def __init__(self):
        self.wnl = WordNetLemmatizer()
    def __call__(self, doc):
        return [self.wnl.lemmatize(t) for t in tokenize(doc) if t not in self.ignore_tokens]

def rank_docs(query, documents):
    stop_words = set(stopwords.words('english')) 
    tokenizer=LemmaTokenizer()
    token_stop = tokenizer(' '.join(stop_words))
    vectorizer = TfidfVectorizer(stop_words=token_stop, 
                              tokenizer=tokenizer)
    doc_vectors = vectorizer.fit_transform([query] + documents)

    # Calculate similarity
    cosine_similarities = linear_kernel(doc_vectors[0:1], doc_vectors).flatten()
    document_ranks = [item.item() for item in cosine_similarities[1:]]
    return document_ranks
def get_most_relevant_idx(document_ranks):
    max_value = max(document_ranks)
    max_index = document_ranks.index(max_value)
    return max_index


if __name__ == '__main__':
    counter = 0
    documents, links = JavaScript_scrape().scrape_websites()
    query = "research opportunities"
    document_ranks = rank_docs(query, documents)
    max_idx = get_most_relevant_idx(document_ranks)
    print(document_ranks)
    print(max_idx)
    print(links[max_idx])
    '''
    items = JavaScript_scrape().scrape_medscape(limit=-1,output='elasticsearch')
    counter+= len(items)
    items = JavaScript_scrape().scrape_aapNews(limit=-1,output='elasticsearch')
    counter+= len(items)
    items = JavaScript_scrape().scrape_medicalNewsToday(limit=-1,output='elasticsearch')
    counter+= len(items)'''
