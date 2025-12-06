
import math
from collections import Counter

def tokenize(text):

#    Découpe un texte en mots simples (tokenisation basique).
    #Tout en minuscule + on garde seulement les lettres.

    import re
    return re.findall(r"[a-zàâçéèêëîïôûùüÿñæœ]+", text.lower())


def term_freq(text):
    
    #Retourne un Counter des mots du document.
    
    tokens = tokenize(text)
    return Counter(tokens), len(tokens)


def build_df(corpus):

    #Calcule la Document Frequency :
   # combien de documents contiennent chaque mot.
    
    df = Counter()
    N = corpus.taille()

    for _, doc in corpus.id2doc.items():
        terms = set(tokenize(doc.texte))  # un mot compte 1 fois par document
        df.update(terms)

    return df, N


def compute_tfidf(corpus):

    #Calcule TF-IDF pour chaque document du corpus.
    #Retourne un dict : doc_id -> Counter(term -> TF-IDF)
    
    df, N = build_df(corpus)
    tfidf_all = {}

    # Calcul IDF
    idf = {t: math.log((N + 1) / (dfi + 1)) for t, dfi in df.items()}

    for doc_id, doc in corpus.id2doc.items():
        tf, total = term_freq(doc.texte)

        tfidf_doc = {}
        for t, count in tf.items():
            tfidf_doc[t] = (count / total) * idf.get(t, 0)

        tfidf_all[doc_id] = Counter(tfidf_doc)

    return tfidf_all


def top_terms(corpus, k=20):
    
    #Retourne les k termes les plus importants du corpus.
    #On additionne le TF-IDF de tous les documents.
    tfidf_dict = compute_tfidf(corpus)
    agg = Counter()

    for _, scores in tfidf_dict.items():
        agg.update(scores)

    return agg.most_common(k)

