
import pandas as pd
import re
from src.Author import Author
from src.Document import Document

class Corpus:
    def __init__(self, nom="Corpus"):
        self.nom = nom
        self.id2doc = {}   # {id: Document}
        self.authors = {}  # {author_name: Author}
        self.ndoc = 0
        self.full_text = None

    def add_doc(self, doc):
        doc_id = self.ndoc
        self.id2doc[doc_id] = doc
        self.ndoc += 1
        # auteurs
        if doc.auteur not in self.authors:
            self.authors[doc.auteur] = Author(doc.auteur)
        self.authors[doc.auteur].add(doc_id, doc)
        # invalidate full_text cache
        self.full_text = None
        return doc_id

    def taille(self):
        return self.ndoc

    def build_full_text(self):
        if self.full_text is None:
            texts = [d.texte for d in self.id2doc.values()]
            self.full_text = " ".join(texts)
        return self.full_text

    def search(self, query):
        
        #Retourne liste de tuples (doc_id, Document) si query substring dans texte .
        if not query:
            return []
        q = query.lower()
        results = []
        for doc_id, doc in self.id2doc.items():
            if q in doc.texte.lower():
                results.append((doc_id, doc))
        return results

    def concorde(self, motif, k=40):
        txt = self.build_full_text()
        res = []
        for m in re.finditer(re.escape(motif), txt, flags=re.IGNORECASE):
            left = txt[max(0, m.start()-k):m.start()]
            right = txt[m.end():m.end()+k]
            res.append((left, m.group(), right))
        return res

    def save(self, path):
        rows = []
        for i, d in self.id2doc.items():
            rows.append([i, d.titre, d.auteur, d.date, d.url, d.texte, d.type])
        df = pd.DataFrame(rows, columns=["id","titre","auteur","date","url","texte","type"])
        df.to_csv(path, sep="\t", index=False)

    def load_from_dataframe(self, df):
    
        #df attendu : colonnes speaker,text,date,descr,link 
       # découpe chaque 'text' en phrases et ajoute au corpus.
       
        for _, row in df.iterrows():
            speaker = row.get("speaker", "Unknown")
            date = row.get("date", "")
            url = row.get("link", "")
            full_text = str(row.get("text", ""))
            # split naïf en phrases
            phrases = full_text.split(".")
            for p in phrases:
                p = p.strip()
                if len(p) > 10:
                    doc = Document(
                        titre="Phrase de discours",
                        auteur=speaker,
                        date=date,
                        url=url,
                        texte=p
                    )
                    self.add_doc(doc)
