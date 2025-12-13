#Classe pour repreesenter un auteur et sa production
class Author:
    def __init__(self, name):
        self.name = name
        self.production = {}
        self.ndoc = 0

    def add(self, doc_id, doc):
        self.production[doc_id] = doc

        self.ndoc += 1

    def __str__(self):
        return f"{self.name} — {self.ndoc} docs"





