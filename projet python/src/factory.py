from src.Document import RedditDocument, ArxivDocument, Document 
  
   # cree et retourne un document Reddit avec le nombre de commentaires
class DocumentFactory: 
    def create_reddit(self, titre, auteur, date, url, texte, comments=0):
      
           return RedditDocument(titre, auteur, date, url, texte, comments)
         

    def create_arxiv(self, titre, auteurs, date, url, texte): 
        return ArxivDocument(titre, auteurs, date, url, texte) 
    # cree et retourne un document generique
    def create_basic(self, titre, auteur, date, url, texte): 
        return Document(titre, auteur, date, url, texte)

