
class Document:
    def __init__(self, titre, auteur, date, url, texte, source="local"):
        self.titre = titre
        self.auteur = auteur
        self.date = date
        self.url = url
        self.texte = texte
        self.type = source

    def __str__(self):
        return f"{self.titre} — {self.auteur}"

#classes specialisees
class RedditDocument(Document):
    def __init__(self, titre, auteur, date, url, texte, comments=0):
        super().__init__(titre, auteur, date, url, texte, source="reddit")
        self.comments = comments

class ArxivDocument(Document):
    def __init__(self, titre, auteurs, date, url, texte):
        super().__init__(titre, ", ".join(auteurs), date, url, texte, source="arxiv")
        self.coauthors = auteurs

