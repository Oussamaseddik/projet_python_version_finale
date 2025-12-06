from Corpus import Corpus
from Document import Document
from factory import DocumentFactory
from SearchEngine import SearchEngine

# créer corpus
corpus = Corpus("TestCorpus")
factory = DocumentFactory()

# ajouter des documents
doc1 = factory.create(
    source="reddit",
    titre="Hello World",
    auteur="Alice",
    date="2024",
    url="http://reddit.com",
    texte="Ceci est un test reddit avec un moteur de recherche.",
    comments=12
)

doc2 = factory.create(
    source="arxiv",
    titre="Deep Learning",
    auteurs=["Bob", "Charlie"],
    date="2023",
    url="http://arxiv.org",
    texte="Cet article parle de deep learning et intelligence artificielle."
)

corpus.add_doc(doc1)
corpus.add_doc(doc2)

# moteur de recherche relié
engine = SearchEngine(corpus)

print("Recherche 'test' :", engine.search("test"))
print("Concordancier ('deep') :\n", corpus.concorde("deep"))
