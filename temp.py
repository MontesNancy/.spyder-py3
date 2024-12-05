import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk import pos_tag, ne_chunk

# Descargar recursos adicionales de NLTK (si aún no lo has hecho)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('wordnet')

# Oración de ejemplo
sentence = "If you wish to make an apple pie from scratch, you must first invent the universe."

# Tokenización
words = word_tokenize(sentence)

# Stemming
porter_stemmer = PorterStemmer()
stemmed_words = [porter_stemmer.stem(word) for word in words]

# Etiquetado de partes del discurso (POS)
pos_tags = pos_tag(words)

# Lemmatización
lemmatizer = WordNetLemmatizer()
lemmatized_words = [lemmatizer.lemmatize(word) for word in words]

# Chunking
chunked_tree = ne_chunk(pos_tags)

# Imprimir resultados
print("Original Sentence:", sentence)
print("\nTokenization:", words)
print("\nStemming:", stemmed_words)
print("\nPOS Tagging:", pos_tags)
print("\nLemmatization:", lemmatized_words)
print("\nChunking Tree:")
chunked_tree.draw()


