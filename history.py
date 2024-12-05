clear
sorted([w for w in set(sent7) if not w.islower()])
sorted([t for t in set(text2) if 'cie' in t or 'cei' in t])
clear
[len(w) for w in text1]
[w.upper() for w in text1]
clear
len(text1)
len(set(text1))
len(set([word.lower() for word in text1]))
len(set([word.lower() for word in text1 if word.isalpha()]))
clear
[w for w in sent7 if len(w) < 4]
word = 'cat'
if len(word) < 5: print 'word length is less than 5'
if len(word) < 5:
    clear
    
clear
[w for w in sent7 if len(w) < 4]
word = 'cat'
if len(word) < 5:
    print 'word length is less than 5'
clear
if len(word) >= 5:
    print 'word length is greater than or equal to 5'
for word in ['Call', 'me', 'Ishmael', '.']:
    print word
clear
if len(word) >= 5:
    print 'word length is greater than or equal to 5'
for word in ['Call', 'me', 'Ishmael', '.']:
    print word
clear
sent1 = ['Call', 'me', 'Ishmael', '.']
for xyzzy in sent1:
    if xyzzy.endswith('l'):
        print xyzzy
clear
for token in sent1:
    if token.islower():
        print token, 'is a lowercase word'
clear
for token in sent1:
    ... if token.islower():
... print token, 'is a lowercase word'
... elif token.istitle():
... print token, 'is a titlecase word'
... else:
... print token, 'is punctuation'
clear
for token in sent1:
    if token.islower():print token, 'is a lowercase word'
clear
tricky = sorted([w for w in set(text2) if 'cie' in w or 'cei' in w])
for word in tricky:
    print word,
ancient ceiling conceit conceited conceive conscience
conscientious conscientiously deceitful deceive ...
clear
>>> babelize_shell()
clear
babelize_shell()
clear
from nltk.book
import *
from nltk.book import *
babelize_shell()
clear
nlk from nltk.book import *
from nltk.book import *
babelize_shell()
clear
babelize_shell()
NLTK Babelizer: type 'help' for a list of commands.
clear
babelize_shell()
clea
clear
nltk.book import *
import nltk.book import *
import modulo
import modulo
from nltk.book import *
babelize_shell()

## ---(Mon Nov 20 10:11:34 2023)---
import nltk
nltk.corpus.gutenberg.fileids()
emma = nltk.corpus.gutenberg.words('austen-emma.txt')
len(emma)
emma = nltk.Text(nltk.corpus.gutenberg.words('austen-emma.txt'))
emma.concordance("surprize")
>>> from nltk.corpus import gutenberg
clear
from nltk.corpus import gutenberg
gutenberg.fileids()
for fileid in gutenberg.fileids():
 num_chars = len(gutenberg.raw(fileid))   
 num_words = len(gutenberg.words(fileid))
 num_sents = len(gutenberg.sents(fileid))
 num_vocab = len(set([w.lower() for w in gutenberg.words(fileid)]))
 print int(num_chars/num_words), int(num_words/num_sents), int(num_words/num_vocab), 
 fileid
for fileid in gutenberg.fileids():
 num_chars = len(gutenberg.raw(fileid))   
 num_words = len(gutenberg.words(fileid))
 num_sents = len(gutenberg.sents(fileid))
 num_vocab = len(set([w.lower() for w in gutenberg.words(fileid)]))
 print int(num_chars/num_words), int(num_words/num_sents), int(num_words/num_vocab), fileid
print
print int(num_chars/num_words), int(num_words/num_sents), int(num_words/num_vocab), 
 fileid
clear
for fileid in gutenberg.fileids():
 num_chars = len(gutenberg.raw(fileid))   
 num_words = len(gutenberg.words(fileid))
 num_sents = len(gutenberg.sents(fileid))
 num_vocab = len(set([w.lower() for w in gutenberg.words(fileid)]))
 print int(num_chars/num_words), int(num_words/num_sents), int(num_words/num_vocab), fileid
clear
for fileid in gutenberg.fileids():
 num_chars = len(gutenberg.raw(fileid))   
 num_words = len(gutenberg.words(fileid))
 num_sents = len(gutenberg.sents(fileid))
 num_vocab = len(set([w.lower() for w in gutenberg.words(fileid)]))
 print int(num_chars/num_words), int(num_words/num_sents), int(num_words/num_vocab), filei
clear
macbeth_sentences = gutenberg.sents('shakespeare-macbeth.txt')
macbeth_sentences
macbeth_sentences[1037]
longest_len = max([len(s) for s in macbeth_sentences])
[s for s in macbeth_sentences if len(s) == longest_len]
from nltk.corpus import webtext
for fileid in webtext.fileids():
    print fileid, webtext.raw(fileid)[:65], '...'
for fileid in webtext.fileids():
    print (fileid, webtext.raw(fileid)[:65], '...')
    
clear
for fileid in webtext.fileids():
    print (fileid, webtext.raw(fileid)[:65], '...')
    
clear
for fileid in gutenberg.fileids():
 num_chars = len(gutenberg.raw(fileid))   
 num_words = len(gutenberg.words(fileid))
 num_sents = len(gutenberg.sents(fileid))
 num_vocab = len(set([w.lower() for w in gutenberg.words(fileid)]))
 print (int(num_chars/num_words), int(num_words/num_sents), int(num_words/num_vocab), fileid)
 
from nltk.corpus import nps_chat
chatroom = nps_chat.posts('10-19-20s_706posts.xml')
chatroom[123]
from nltk.corpus import brown
brown.categories()
brown.words(categories='news')
brown.words(fileids=['cg22'])
brown.sents(categories=['news', 'editorial', 'reviews'])
from nltk.corpus import brown
news_text = brown.words(categories='news')
fdist = nltk.FreqDist([w.lower() for w in news_text])
modals = ['can', 'could', 'may', 'might', 'must', 'will']
for m in modals:
    print (m + ':', fdist[m],)
    
>>> cfd = nltk.ConditionalFreqDist(
(genre, word)
for genre in brown.categories()
for word in brown.words(categories=genre))
genres = ['news', 'religion', 'hobbies', 'science_fiction', 'romance', 'humor']
modals = ['can', 'could', 'may', 'might', 'must', 'will']
cfd.tabulate(conditions=genres, samples=modals)
from nltk.corpus import reuters
reuters.fileids()
from nltk.corpus import reuters
reuters.fileids()
from nltk.corpus import reuters
reuters.fileids()
from nltk.corpus import reuters
reuters.categories()
reuters.categories('training/9865')
reuters.categories(['training/9865', 'training/9880'])
reuters.fileids('barley')
reuters.fileids(['barley', 'corn'])
reuters.words('training/9865')[:14]
reuters.words(['training/9865', 'training/9880'])
reuters.words(categories='barley')
reuters.words(categories=['barley', 'corn'])
from nltk.corpus import inaugural
clear
from nltk.corpus import inaugural
inaugural.fileids()
[fileid[:4] for fileid in inaugural.fileids()]
cfd = nltk.ConditionalFreqDist(
(target, file[:4])
for fileid in inaugural.fileids()
for w in inaugural.words(fileid)
for target in ['america', 'citizen']
if w.lower().startswith(target))
cfd = nltk.ConditionalFreqDist(
(target, file[:4])
for fileid in inaugural.fileids()
for w in inaugural.words(fileid)
for target in ['america', 'citizen']
if (w.lower().startswith(target)))
cfd.plot()
import nltk
nltk.download('punkt')
cfd = nltk.ConditionalFreqDist(
(target, file[:4])
for fileid in inaugural.fileids()
for w in inaugural.words(fileid)
for target in ['america', 'citizen']
if w.lower().startswith(target))
[fileid[:4] for fileid in inaugural.fileids()]
from nltk.corpus import inaugural
inaugural.fileids()
[fileid[:4] for fileid in inaugural.fileids()]
cfd = nltk.ConditionalFreqDist(
(target, file[:4])
for fileid in inaugural.fileids()
for w in inaugural.words(fileid)
for target in ['america', 'citizen']
if w.lower().startswith(target))
nltk.download('punkt')
cfd = nltk.ConditionalFreqDist(
(target, file[:4])
for fileid in inaugural.fileids()
for w in inaugural.words(fileid)
for target in ['america', 'citizen']
if (w.lower().startswith(target)))
cfd = nltk.ConditionalFreqDist(
(target, file[:4])
for fileid in inaugural.fileids()
for w in inaugural.words(fileid)
for target in ['america', 'citizen']
if w.lower().startswith(target))
from nltk.corpus import inaugural
nltk.download('inaugural')
cfd = nltk.ConditionalFreqDist(
    (target, fileid[:4])  # Cambiado file[:4] a fileid[:4]
    for fileid in inaugural.fileids()
    for w in inaugural.words(fileid)
    for target in ['america', 'citizen']
    if w.lower().startswith(target)
)
cfd.plot()
nltk.corpus.cess_esp.words()
nltk.corpus.floresta.words()
nltk.corpus.indian.words('hindi.pos')
nltk.corpus.udhr.fileids()
nltk.corpus.udhr.words('Javanese-Latin1')[11:]
from nltk.corpus import udhr
clear
nltk.corpus.udhr.words('Javanese-Latin1')[11:]
from nltk.corpus import udhr
languages = ['Chickasaw', 'English', 'German_Deutsch',
'Greenlandic_Inuktikut', 'Hungarian_Magyar', 'Ibibio_Efik']
cfd = nltk.ConditionalFreqDist(
(lang, len(word))
for lang in languages
for word in udhr.words(lang + '-Latin1'))
cfd.plot(cumulative=True)
nltk.FreqDist(raw_text).plot().
nltk.FreqDist(raw_text).plot()
udhr.fileids()
raw_text = udhr.raw(Language-Latin1)
nltk.FreqDist(raw_text).plot()
udhr.fileids()
raw_text = udhr.raw(Language-Latin1)

## ---(Mon Nov 20 19:42:17 2023)---
raw = gutenberg.raw("burgess-busterbrown.txt")
help(nltk.corpus.reader)
clear 
import nltk
nltk.corpus.gutenberg.fileids()
raw = gutenberg.raw("burgess-busterbrown.txt")
emma = nltk.corpus.gutenberg.words('austen-emma.txt')
len(emma)
from nltk.corpus import brown
clear
raw = gutenberg.raw("burgess-busterbrown.txt")
import nltk
nltk.download('gutenberg')
raw = gutenberg.raw("burgess-busterbrown.txt")
import nltk
nltk.download('gutenberg')
raw = gutenberg.raw("burgess-busterbrown.txt")
!pip install nltk
import nltk
nltk.download('gutenberg')
from nltk.corpus import gutenberg
raw = gutenberg.raw("burgess-busterbrown.txt")
raw[1:20]
words = gutenberg.words("burgess-busterbrown.txt")
words[1:20]
sents = gutenberg.sents("burgess-busterbrown.txt")
sents[1:20]
from nltk.corpus import PlaintextCorpusReader
corpus_root = '/usr/share/dict
clear
from nltk.corpus import PlaintextCorpusReader
corpus_root = '/usr/share/dict'
wordlists = PlaintextCorpusReader(corpus_root, '.*')
from nltk.corpus import PlaintextCorpusReader
wordlists = PlaintextCorpusReader(corpus_root, '.*')
nltk.corpus.gutenberg.fileids()
from nltk.corpus import webtext
from nltk.corpus import nps_chat
from nltk.corpus import brown
from nltk.corpus import reuters
from nltk.corpus import inaugural
nltk.corpus.cess_esp.words()
nltk.corpus.floresta.words()
nltk.corpus.indian.words('hindi.pos')
>>> nltk.corpus.udhr.fileids()
nltk.corpus.udhr.words('Javanese-Latin1')[11:]
from nltk.corpus import udhr
from nltk.corpus import PlaintextCorpusReader
corpus_root = '/usr/share/dict'
wordlists = PlaintextCorpusReader(corpus_root, '.*')
corpus_root = '/usr/share/dict'
wordlists.fileids()
from nltk.corpus import PlaintextCorpusReader
corpus_root = '/usr/share/dict'
wordlists = PlaintextCorpusReader(corpus_root, '.*')
corpus_root = r'C:\ruta\a\tu\corpus'
corpus_root = r'C:\Users\NANCY\Desktop\Corpus'
wordlists = PlaintextCorpusReader(corpus_root, '.*')
wordlists.fileids()
from nltk.corpus import PlaintextCorpusReader
corpus_root = r'C:\Users\NANCY\Desktop\Corpus'
clear
from nltk.corpus import PlaintextCorpusReader
corpus_root = '/usr/share/dict'
wordlists = PlaintextCorpusReader(corpus_root, '.*')
textCorpusReader
from nltk.corpus import PlaintextCorpusReader
corpus_root = r'C:\Users\NANCY\Desktop\Corpus'
wordlists = PlaintextCorpusReader(corpus_root, '.*')
wordlists.fileids()
wordlists.words('connectives')
from nltk.corpus import PlaintextCorpusReader
corpus_root = '/usr/share/dict'
wordlists = PlaintextCorpusReader(corpus_root, '.*')
import os
corpus_root = r'C:\MiCorpus'
if not os.path.exists(corpus_root): os.makedirs(corpus_root)
from nltk.corpus import PlaintextCorpusReader
corpus_root = r'C:\MiCorpus'
wordlists = PlaintextCorpusReader(corpus_root, '.*')
wordlists.fileids()
wordlists.words('connectives')

## ---(Thu Nov 30 14:46:18 2023)---
from nltk.tokenize import sent_tokenize, word_tokenize
example_tring = """
Muad'Dib learned rapidly because his first training was in how to learn. And the first lesson of all was the basic trust that he could learn. It's shocking to find how many people do not believe they can learn, and how many more believe learning to be difficult."""
sent_tokenize(example_string)
sent_tokenize(example_tring)
clear
from nltk.tokenize import sent_tokenize, word_tokenize
example_string = """
Muad'Dib learned rapidly because his first training was in how to learn. And the first lesson of all was the basic trust that he could learn. It's shocking to find how many people do not believe they can learn, and how many more believe learning to be difficult."""
sent_tokenize(example_string)
word_tokenize(example_string)

## ---(Fri Dec  1 11:20:12 2023)---
nltk.download("stopwords")
clear
pip install nltk
import nltk
nltk.download("stopwords")
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
clear
worf_quote = "Sir, I protest. I am not a merry man!"
words_in_quote = word_tokenize(worf_quote)
words_in_quote
stop_words = set(stopwords.words("english"))
filtered_list = []
clear
stop_words = set(stopwords.words("english"))
filtered_list = []
for word in words_in_quote:
    if word.casefold() not in stop_words:
        filtered_list.append(word)
        
filtered_list = [
word for word in words_in_quote if word.casefold() not in stop words
]
filtered_list = [
word for word in words_in_quote if word.casefold() not in stop words]
filtered_list = 
[word for word in words_in_quote if word.casefold() not in stop words]
filtered_list = [word for word in words_in_quote if word.casefold() not in stop_words]
clear
filtered_list = [word for word in words_in_quote if word.casefold() not in stop_words]
filtered_list
clear
for nltk.stem import PorterStemmer
clear
for nltk.stem import PorterStemmer
clear
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
stemmer = PorterStemmer()
clear
string_for_stemming = """
The crew of the USS Discovery discovered many discoveries.
Discovering is what explorers do."""
words = word_tokenize(string_for_stemming)
words
clear
stemmed_words = [stemmer.stem(word) for word in words]
stemmed_words
clear
from nltk.tokenize import word_tokenize
clear
import nltk
from nltk.tokenize import word_tokenize
text = word_tokenize("Hello welcome to the world of to learn Categorizing and POS Tagging with NLTK and Python")
nltk.pos_tag(text)
clear
sagan_quote = """
If you wish to make an apple pie from scratch,
you must first invent the universe. """"
sagan_quote = """
If you wish to make an apple pie from scratch,
you must first invent the universe.""""
clear
sagan_quote = """ If you wish to make an apple pie from scratch, you must first invent the universe.""""
clear
sagan_quote = """If you wish to make an apple pie from scratch, you must first invent the universe."""
words_in_sagan_quote = word_tokenize(sagan_quote)
nltk.pos_tag()
clear
sagan_quote = """If you wish to make an apple pie from scratch, you must first invent the universe."""
words_in_sagan_quote = word_tokenize(sagan_quote)
import nltk
nltk.pos_tag(words_in_sagan_quote)
clear
nltk.help.upenn_tagset()
clear
jabberwocky_excerpt = """'Twas brillig, and the slithy toves did gyre and gimble in the wabe: all mimsy were the borogoves, and the mome raths outgrabe."""
words_in_excerpt = word_tokenize(jabberwocky_excerpt)
nltk.pos_tag(words_in_excerpt)
clear
from nltk.stem import WordNetLemmatizer
lemmatizer.lematize("scarves")
clear
from nltk.stem import WordNetLemmatizer
lemmatizer.lemmatize("scarves")
clear
from nltk.stem import WordNetLemmatizer
lemmatizer.lemmatize("scarver")
lemmatizer.lemmatize("scarves")
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
lemmatizer.lemmatize("scarves")
string_for_lemmatizing = "The friends of DeSoto love scarves"
clear
words = word_tokenize(string_for_lemmatizing)
words
lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
clear
lemmatized_words
lemmatizer lemmatize("worst")
clear
lemmatized_words
lemmatizer.lemmatize("worst")
lemmatizer.lemmatize("worst", pos="a")

## ---(Tue Dec  5 19:12:56 2023)---
import nltk
from nltk.tokenize import word_tokenize
sagan_quote = """
If you wish to make an apple pie from scratch, 
you must first invent the universe. """
from nltk.tokenize import sent_tokenize, word_tokenize
sent_tokenize(sagan_quote)
word_tokenine(sagan_quote)
word_tokenize(sagan_quote)
import nltk
nltk.download("stopwords")
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
worf_qute = "If you wish to make an apple pie from scratch, you must first invent the universe."
worf_quote = "If you wish to make an apple pie from scratch, you must first invent the universe."
words_in_quote = word_tokenize(worf_quote)
words_in_quote
stop_words = set(stopwords.words("english"))
filtered_list = []
for word in words_in_quote:
… if word.casefold() not in stop_words:
… filtered_list.append(word)
for word in words_in_quote:
if word.casefold() not in stop_words:
    filtered_list.append(word)
for word in words_in_quote:
if word.casefold() not in stop_words:
filtered_list.append(word)
for word in words_in_quote:
if word.casefold() not in sagan_quote:
filtered_list.append(word)
for word in words_in_quote:
    if word.casefold() not in stop_words:
        filtered_list.append(word)
        
filtered_list = [word for word in words_in_quote if word.casefold() not in stop_words]
filtered_list
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
stemmer = PorterStemmer()
string_for_stemming = """ If you wish to make an apple pie from scratch, you must first invent the universe."""
words = word_tokenize(string_for_stemming)
words
stemmed_words = [stemmer.stem(word) for word in words]
stemmed_words
from nltk.tokenize import word_tokenize
text = word_tokenize("If you wish to make an apple pie from scratch, you must first invent the universe.")
nltk.pos_tag(text)
sagan_quote = """If you wish to make an apple pie from scratch, you must first invent the universe"""
words_in_sagan_quote = word_tokenize(sagan_quote)
import nltk
nltk.pos_tag(words_in_sagan_quote)

## ---(Wed Dec  6 23:40:28 2023)---
import nltk
from nltk .tokenize import word_tokenize
lotr_quote = "It's dangerous business, Frodo, goinf out your door."
words_in_lotr_quote = word_tokenize(lots_quote)
sagan_quote = """If you wish to make an apple pie from scratch, you must first invent the universe."""
words_in_sagan_quote = word_tokenize(sagan_quote)
import nltk
nltk.pos_tag(words_in_sagan_quote)
from nltk.tokenize import word_tokenize
lotr_quote = "It's dangerous business, Frodo, goinf out your door."
words_in_lotr_quote = word_tokenize(lotr_quote)
words_in_lotr_quote
nltk.download("averaged_perceptron_tagger")
lotr_pos_tags = nltk.pos_tag(words_in_lotr_quote)
lotr_pos_tags
grammar = "NP: {<DT>?<JJ>*<NN>}"
chunk_parser = nltk.RegexpParser(grammar)
tree = chunk_parser.parse(lotr_pos_tags)
tree.draw()
lotr_pos_tags
grammar = """
chunk: {<.*>+}
}<JJ>{"""
chunk_parser = nltk.RagexpParser(grammar)
chunk_parser = nltk.RegexpParser(grammar)
import nltk
pip install --upgrade nltk
grammar = """
chunk: {<.*>+}
}<JJ>{"""
chunk_parser = nltk.RegexpParser(grammar)
tree = chunk_parser.parse(lotr_pos_tags)
tree
tree.draw()
grammar = r"""
NP:
{<.*>+}
}<VBD|IN>+{
"""
sentence = [("the", "DT"),("little", "J"),("yellow", "JJ"),("dog","NN"),("barked","VBD"),("at","IN"),("the","DT"),("cat","NN")]
cp = nltk.RegexpParser(grammar)
print(cp.prse(sentence))
print(cp.parse(sentence))
clear
nltk.download("maxent_ne_chunker")
nltk.download("words")
tree = nltk.ne_chunk(lotr_pos_tags)
tree.draw()
tree = nltk.ne_chunk(lotr_pos_tags, binary=True)
tree.draw()
quote = """
Men like Schiaparelli watched the red planet-it is odd, by-the-bye, that for countless centuries Mars has been the star of war-but failed to interpret the fluctuating appearances of the markings they mapped so well. All that time the Martians must have been getting ready.
During the opposition of 1894 a great light was seen on the illuminated part of the disk, first at the Lick Observatory, then by Perrotin of Nice, and then by other observers. English readers heard of it first in the issue of Nature dated August 2."""
def extract_ne(quote):
words = word_tokenize(quote, language=language)
tags = nltk.pos_tag(words)
tree nltk.ne_chunk(tags, binary=True)
return set (
"".join(i[0] for i in t)
for t in tree
if hasattr(t, "label") and t. label() "NE"
)
def extract_ne(quote):
words = word_tokenize(quote, language=language)
tags = nltk.pos_tag(words)
tree nltk.ne_chunk(tags, binary=True)
return set (
    "".join(i[0] for i in t)
    for t in tree
    if hasattr(t, "label") and t. label() "NE"
)
def extract_ne(quote):
    words = word_tokenize(quote, language=language)
    tags = nltk.pos_tag(words)
    tree nltk.ne_chunk(tags, binary=True)
    return set (
        "".join(i[0] for i in t)
        for t in tree
        if hasattr(t, "label") and t. label() "NE"
)
def extract_ne(quote):
    words = word_tokenize(quote, language=language)
    tags = nltk.pos_tag(words)
    tree = nltk.ne_chunk(tags, binary=True)
    return set (
        "".join(i[0] for i in t)
        for t in tree
        if hasattr(t, "label") and t. label() "NE"
)
def extract_ne(quote):
    words = word_tokenize(quote, language=language)
    tags = nltk.pos_tag(words)
    tree = nltk.ne_chunk(tags, binary=True)
    return set (
        "".join(i[0] for i in t)
        for t in tree
        if hasattr(t, "label") and t.label() == "NE":
)
def extract_ne(quote):
    words = word_tokenize(quote, language=language)
    tags = nltk.pos_tag(words)
    tree = nltk.ne_chunk(tags, binary=True)
    return set (
        "".join(i[0] for i in t)
        for t in tree
        if hasattr(t, "label") and t.label() == "NE"
)
extract_ne(quote)
def extract_ne(quote, language='english'):
    words = word_tokenize(quote, language=language)
    
extract_ne(quote)
clear
def extract_ne(quote, language='english'):
    words = word_tokenize(quote, language=language)
    
extract_ne(quote)
nltk.download("book")
from nltk.book import *
clear
from nltk.tokenize import sent_tokenize, word_tokenize
example_tring = """If you wish to make an apple pie from scratch, you must first invent the universe."""
sent_tokenize(example_string)
clear
from nltk.tokenize import sent_tokenize, word_tokenize
example_string = """If you wish to make an apple pie from scratch, you must first invent the universe."""
sent_tokenize(example_string)
word_tokenize(example_string)
import nltk
nltk.download("stopwords")
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
worf_quote = "If you wish to make an apple pie from scratch, you must first invent the universe."
words_in_quote = word_tokenize(worf_quote)
words_in_quote
stop_words = set(stopwords.words("english"))
filtered_list = []
for word in words_in_quote:
    if word.casefold() not in stop_words:
        filtered_list.append(word)
        
filtered_list = [word for word in words_in_quote if word.casefold() not in stop_words]
filtered_list
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
stemmer = PorterStemmer()
string_for_stemming = """If you wish to make an apple pie from scratch, you must first invent the universe."""
words = word_tokenize(string_for_stemming)
words
stemmed_words = [stemmer.stem(word) for word in words]
stemmed_words
import nltk
from nltk.tokenize import word_tokenize
text = word_tokenize("If you wish to make an apple pie from scratch, you must first invent the universe.")
nltk.pos_tag(text)
sagan_quote = """If you wish to make an apple pie from scratch, you must first invent the universe."""
words_in_sagan_quote = word_tokenize(sagan_quote)
import nltk
nltk.pos_tag(words_in_sagan_quote)
nltk.help.upenn_tagset()
jabberwocky_excerpt = """If you wish to make an apple pie from scratch, you must first invent the universe."""
words_in_excerpt = word_tokenize(jabberwocky_excerpt)
nltk.pos_tag(words_in_excerpt)
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
lemmatizer.lemmatize("scarves")
string_for_lemmatizing = "The friends of DeSoto love scarves"
string_for_lemmatizing = "If you wish to make an apple pie from scratch, you must first invent the universe."
words = word_tokenize(string_for_lemmatizing)
words
lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
lemmatized_words
lemmatizer.lemmatize("worst")
lemmatizer.lemmatize("worst", pos="a")
from nltk.tokenize import word_tokenize
lotr_quote = "If you wish to make an apple pie from scratch, you must first invent the universe."
words_in_lotr_quote = word_tokenize(lotr_quote)
words_in_lotr_quote
lotr_pos_tags = nltk.pos_tag(words_in_lotr_quote)
lotr_pos_tags
grammar = "NP: {<DT>?<JJ>*<NN>}"
chunk_parser = nltk.RegexpParser(grammar)
tree = chunk_parser.parse(lotr_pos_tags)
tree.draw()
lotr_pos_tags
grammar = """chunk: {<.*>+}}<JJ>{"""
chunk_parser = nltk.RegexpParser(grammar)

## ---(Thu Dec  7 16:53:01 2023)---
from nltk.tokenize import sent_tokenize, word_tokenize
example_tring = """If you wish to make an apple pie from scratch, you must first invent the universe."""
sent_tokenize(example_string)
nltk import
import nltk
sent_tokenize(example_string)
example_tring = """If you wish to make an apple pie from scratch, you must first invent the universe."""
import nltk
nltk.pos_tag(words_in_sagan_quote)
import nltk
nltk.download("stopwords")
from nltk.corpus import stopwords
rom nltk.tokenize import word_tokenize
from nltk.tokenize import word_tokenize
worf_quote = "Sir, I protest. I am not a merry man!"
words_in_quote = word_tokenize(worf_quote)
words_in_quote
stop_words = set(stopwords.words("english"))
filtered_list = []
for word in words_in_quote:
    if word.casefold() not in stop_words:
        filtered_list.append(word)
        
filtered_list = [word for word in words_in_quote if word.casefold() not in stop_words]
filtered_list
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
stemmer = PorterStemmer()
string_for_stemming = """If you wish to make an apple pie from scratch, you must first invent the universe."""
words = word_tokenize(string_for_stemming)
words
stemmed_words = [stemmer.stem(word) for word in words]
stemmed_words
from nltk.tokenize import word_tokenize
text = word_tokenize("Hello welcome to the world of to learn Categorizing and POS Tagging with NLTK and Python")
nltk.pos_tag(text)
sagan_quote = """If you wish to make an apple pie from scratch, you must first invent the universe."""
words_in_sagan_quote = word_tokenize(sagan_quote)
import nltk
nltk.pos_tag(words_in_sagan_quote)
nltk.help.upenn_tagset()
jabberwocky_excerpt = """If you wish to make an apple pie from scratch, you must first invent the universe."""
words_in_excerpt = word_tokenize(jabberwocky_excerpt)
nltk.pos_tag(words_in_excerpt)
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
lemmatizer.lemmatize("scarves")
string_for_lemmatizing = "The friends of DeSoto love scarves"
words = word_tokenize(string_for_lemmatizing)
words
lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
lemmatized_words
lemmatizer.lemmatize("worst")
lemmatizer.lemmatize("worst", pos="a")
from nltk.tokenize import word_tokenize
lotr_quote = "It's dangerous business, Frodo, goinf out your door."
words_in_lotr_quote = word_tokenize(lotr_quote)
words_in_lotr_quote
lotr_pos_tags = nltk.pos_tag(words_in_lotr_quote)
lotr_pos_tags
grammar = "NP: {<DT>?<JJ>*<NN>}"
chunk_parser = nltk.RegexpParser(grammar)
tree = chunk_parser.parse(lotr_pos_tags)
tree.draw()
lotr_pos_tags
grammar = """
… chunk: {<.*>+}
… }<JJ>{"""
chunk_parser = nltk.RegexpParser(grammar)
tree = chunk_parser.parse(lotr_pos_tags)
tree
tree.draw()
sentence = "If you wish to make an apple pie from scratch, you must first invent the universe."
words_in_excerpt = nltk.word_tokenize(sentence)
pos_tags = nltk.pos_tag(words_in_excerpt)
chunked_tree = nltk.ne_chunk(pos_tags)
chunked_tree.draw()
pos_tree = Tree("POS", pos_tags)
pos_tags = nltk.pos_tag(words_in_excerpt)
pos_tree = Tree("POS", pos_tags)
sentence = "If you wish to make an apple pie from scratch, you must first invent the universe."
words_in_excerpt = nltk.word_tokenize(sentence)
pos_tags = nltk.pos_tag(words_in_excerpt)
pos_tree = Tree("POS", pos_tags)
chunked_tree = nltk.ne_chunk(pos_tags)
merged_tree = Tree("Merged", [pos_tree, chunked_tree])
merged_tree.draw()
clear
import nltk
from nltk import pos_tag, word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.chunk import RegexpParser
from nltk.tree import Tree
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
sentence = "If you wish to make an apple pie from scratch, you must first invent the universe."
words = word_tokenize(sentence)
stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(word) for word in words]
pos_tags = pos_tag(words)
lemmatizer = WordNetLemmatizer()
lemmatized_words = [lemmatizer.lemmatize(word, pos=tag[1][0].lower()) if tag[1][0].lower() in ['n', 'v'] else lemmatizer.lemmatize(word) for word, tag in pos_tags]
lemmatized_words = [
    lemmatizer.lemmatize(word, pos=get_wordnet_pos(tag[1])) if tag[1] and tag[1][0].lower() in ['n', 'v'] else lemmatizer.lemmatize(word)
    for word, tag in pos_tags
]
lemmatized_words = [
    lemmatizer.lemmatize(word, pos=get_wordnet(tag[1])) if tag[1] and tag[1][0].lower() in ['n', 'v'] else lemmatizer.lemmatize(word)
    for word, tag in pos_tags
]
words = word_tokenize(sentence)
stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(word) for word in words]
pos_tags = pos_tag(words)
lemmatizer = WordNetLemmatizer()
lemmatized_words = [lemmatizer.lemmatize(word, pos=tag[1][0].lower()) if tag[1][0].lower() in ['n', 'v'] else lemmatizer.lemmatize(word) for word, tag in pos_tags]
grammar = r"""
    NP: {<DT>?<JJ>*<NN>}   # Chunk sequences of DT, JJ, NN
    PP: {<IN><NP>}        # Chunk prepositions followed by NP
    VP: {<MD>?<VB.*><NP>?} # Chunk verbs and their arguments
"""
chunk_parser = RegexpParser(grammar)
chunks = chunk_parser.parse(pos_tags)
chunks.draw()
import nltk
from nltk.tree import Tree
sentence = "If you wish to make an apple pie from scratch, you must first invent the universe."
words_in_excerpt = nltk.word_tokenize(sentence)
token_tree = Tree("Tokenization", [Tree(word, []) for word in words_in_excerpt])
porter_stemmer = nltk.PorterStemmer()
stemmed_words = [porter_stemmer.stem(word) for word in words_in_excerpt]
stemming_tree = Tree("Stemming", [Tree(word, []) for word in stemmed_words])
pos_tags = nltk.pos_tag(words_in_excerpt)
pos_tree = Tree("POS Tags", [Tree(str(tag), []) for tag in pos_tags])
lemmatizer = nltk.WordNetLemmatizer()
lemmatized_words = [lemmatizer.lemmatize(word) for word in words_in_excerpt]
lemmatization_tree = Tree("Lemmatization", [Tree(word, []) for word in lemmatized_words])
grammar = "NP: {<DT>?<JJ>*<NN>}"
chunk_parser = nltk.RegexpParser(grammar)
chunks_tree = chunk_parser.parse(pos_tags)
merged_tree = Tree("Merged", [token_tree, stemming_tree, pos_tree, lemmatization_tree, chunks_tree])
merged_tree.draw()
runfile('C:/Users/NANCY/.spyder-py3/temp.py', wdir='C:/Users/NANCY/.spyder-py3')
runcell(0, 'C:/Users/NANCY/.spyder-py3/temp.py')
runfile('C:/Users/NANCY/.spyder-py3/temp.py', wdir='C:/Users/NANCY/.spyder-py3')

## ---(Fri Dec  8 18:44:52 2023)---
runfile('C:/Users/NANCY/.spyder-py3/tokenizador.py', wdir='C:/Users/NANCY/.spyder-py3')

## ---(Wed Feb 21 01:42:10 2024)---
runfile('C:/Users/NANCY/.spyder-py3/untitled0.py', wdir='C:/Users/NANCY/.spyder-py3')
runfile('C:/Users/NANCY/.spyder-py3/euclidina.py', wdir='C:/Users/NANCY/.spyder-py3')
runfile('C:/Users/NANCY/.spyder-py3/MetricaEuclidiana.py', wdir='C:/Users/NANCY/.spyder-py3')
runfile('C:/Users/NANCY/.spyder-py3/MetricaEuclidiana.py', wdir='C:/Users/NANCY/.spyder-py3')

## ---(Wed Feb 21 16:08:56 2024)---
runfile('C:/Users/NANCY/.spyder-py3/MetricaEuclidiana.py', wdir='C:/Users/NANCY/.spyder-py3')
runfile('C:/Users/NANCY/.spyder-py3/euclidina.py', wdir='C:/Users/NANCY/.spyder-py3')
runfile('C:/Users/NANCY/.spyder-py3/MetricaEuclidiana.py', wdir='C:/Users/NANCY/.spyder-py3')
runfile('C:/Users/NANCY/.spyder-py3/MetricaEuclidiana.py', wdir='C:/Users/NANCY/.spyder-py3')
runfile('C:/Users/NANCY/.spyder-py3/MetricaEuclidiana.py', wdir='C:/Users/NANCY/.spyder-py3')
runfile('C:/Users/NANCY/.spyder-py3/MetricaEuclidiana.py', wdir='C:/Users/NANCY/.spyder-py3')
runfile('C:/Users/NANCY/.spyder-py3/untitled0.py', wdir='C:/Users/NANCY/.spyder-py3')
runfile('C:/Users/NANCY/.spyder-py3/untitled0.py', wdir='C:/Users/NANCY/.spyder-py3')
runfile('C:/Users/NANCY/.spyder-py3/Euclidiana2.0.py', wdir='C:/Users/NANCY/.spyder-py3')
runfile('C:/Users/NANCY/.spyder-py3/MetricaEuclidiana.py', wdir='C:/Users/NANCY/.spyder-py3')
runfile('C:/Users/NANCY/.spyder-py3/Euclidiana2.0.py', wdir='C:/Users/NANCY/.spyder-py3')

## ---(Mon Feb 26 15:20:23 2024)---
runfile('C:/Users/NANCY/.spyder-py3/untitled0.py', wdir='C:/Users/NANCY/.spyder-py3')

## ---(Mon Mar  4 15:28:58 2024)---
runfile('C:/Users/NANCY/.spyder-py3/untitled0.py', wdir='C:/Users/NANCY/.spyder-py3')
runfile('C:/Users/NANCY/.spyder-py3/untitled1.py', wdir='C:/Users/NANCY/.spyder-py3')
runfile('C:/Users/NANCY/.spyder-py3/untitled0.py', wdir='C:/Users/NANCY/.spyder-py3')

## ---(Tue Mar  5 15:58:48 2024)---
runfile('C:/Users/NANCY/.spyder-py3/untitled0.py', wdir='C:/Users/NANCY/.spyder-py3')

## ---(Wed Mar  6 16:36:33 2024)---
runfile('C:/Users/NANCY/.spyder-py3/untitled0.py', wdir='C:/Users/NANCY/.spyder-py3')
runfile('C:/Users/NANCY/.spyder-py3/untitled1.py', wdir='C:/Users/NANCY/.spyder-py3')
runfile('C:/Users/NANCY/.spyder-py3/Actividad7-Codigo.py', wdir='C:/Users/NANCY/.spyder-py3')

## ---(Mon Mar 11 14:07:32 2024)---
runfile('C:/Users/NANCY/.spyder-py3/Actividad7-Codigo.py', wdir='C:/Users/NANCY/.spyder-py3')
runfile('C:/Users/NANCY/.spyder-py3/Actividad7-Codigo.py', wdir='C:/Users/NANCY/.spyder-py3')
runfile('C:/Users/NANCY/.spyder-py3/Actividad7-Datos.py', wdir='C:/Users/NANCY/.spyder-py3')
runfile('C:/Users/NANCY/.spyder-py3/Actividad7-Codigo.py', wdir='C:/Users/NANCY/.spyder-py3')
runfile('C:/Users/NANCY/.spyder-py3/Actividad7-Codigo2.py', wdir='C:/Users/NANCY/.spyder-py3')

## ---(Wed Mar 13 15:50:10 2024)---
runfile('C:/Users/NANCY/.spyder-py3/Actividad7-Codigo2.py', wdir='C:/Users/NANCY/.spyder-py3')
runfile('C:/Users/NANCY/.spyder-py3/untitled0.py', wdir='C:/Users/NANCY/.spyder-py3')
runfile('C:/Users/NANCY/.spyder-py3/Actividad7-Codigo2.py', wdir='C:/Users/NANCY/.spyder-py3')
runfile('C:/Users/NANCY/.spyder-py3/untitled0.py', wdir='C:/Users/NANCY/.spyder-py3')
runfile('C:/Users/NANCY/.spyder-py3/Actividad7-Codigo2.py', wdir='C:/Users/NANCY/.spyder-py3')
runfile('C:/Users/NANCY/.spyder-py3/untitled0.py', wdir='C:/Users/NANCY/.spyder-py3')
runfile('C:/Users/NANCY/.spyder-py3/Actividad7-Codigo.py', wdir='C:/Users/NANCY/.spyder-py3')
runfile('C:/Users/NANCY/.spyder-py3/Actividad7-Codigo2.py', wdir='C:/Users/NANCY/.spyder-py3')
runfile('C:/Users/NANCY/.spyder-py3/untitled1.py', wdir='C:/Users/NANCY/.spyder-py3')
runfile('C:/Users/NANCY/.spyder-py3/untitled2.py', wdir='C:/Users/NANCY/.spyder-py3')
runfile('C:/Users/NANCY/.spyder-py3/untitled3.py', wdir='C:/Users/NANCY/.spyder-py3')
runfile('C:/Users/NANCY/.spyder-py3/Actividad7-Codigo2.py', wdir='C:/Users/NANCY/.spyder-py3')
runfile('C:/Users/NANCY/.spyder-py3/Actividad7-Codigo.py', wdir='C:/Users/NANCY/.spyder-py3')
runfile('C:/Users/NANCY/.spyder-py3/Actividad7-Codigo2.py', wdir='C:/Users/NANCY/.spyder-py3')
runfile('C:/Users/NANCY/.spyder-py3/untitled4.py', wdir='C:/Users/NANCY/.spyder-py3')
runfile('C:/Users/NANCY/.spyder-py3/Actividad7-Codigo2.py', wdir='C:/Users/NANCY/.spyder-py3')
runfile('C:/Users/NANCY/.spyder-py3/untitled4.py', wdir='C:/Users/NANCY/.spyder-py3')
runfile('C:/Users/NANCY/.spyder-py3/Actividad7-Codigo2.py', wdir='C:/Users/NANCY/.spyder-py3')

## ---(Sat Apr  6 23:28:17 2024)---
runfile('C:/Users/NANCY/.spyder-py3/untitled0.py', wdir='C:/Users/NANCY/.spyder-py3')
runfile('C:/Users/NANCY/.spyder-py3/Actividad7-Codigo2.py', wdir='C:/Users/NANCY/.spyder-py3')
runfile('C:/Users/NANCY/.spyder-py3/Actividad7-Codigo.py', wdir='C:/Users/NANCY/.spyder-py3')
runfile('C:/Users/NANCY/.spyder-py3/untitled1.py', wdir='C:/Users/NANCY/.spyder-py3')

## ---(Wed Apr 10 16:21:53 2024)---
runfile('C:/Users/NANCY/.spyder-py3/Actividad8-Codigo.py', wdir='C:/Users/NANCY/.spyder-py3')
runfile('C:/Users/NANCY/.spyder-py3/untitled0.py', wdir='C:/Users/NANCY/.spyder-py3')
runfile('C:/Users/NANCY/.spyder-py3/Actividad8-Codigo.py', wdir='C:/Users/NANCY/.spyder-py3')
runfile('C:/Users/NANCY/.spyder-py3/untitled1.py', wdir='C:/Users/NANCY/.spyder-py3')
runfile('C:/Users/NANCY/.spyder-py3/untitled1.py', wdir='C:/Users/NANCY/.spyder-py3')
runfile('C:/Users/NANCY/.spyder-py3/Actividad8-Codigo.py', wdir='C:/Users/NANCY/.spyder-py3')
runfile('C:/Users/NANCY/.spyder-py3/Actividad8-Codigo.py', wdir='C:/Users/NANCY/.spyder-py3')
runfile('C:/Users/NANCY/.spyder-py3/untitled2.py', wdir='C:/Users/NANCY/.spyder-py3')
runfile('C:/Users/NANCY/.spyder-py3/Actividad8-Codigo.py', wdir='C:/Users/NANCY/.spyder-py3')
runfile('C:/Users/NANCY/.spyder-py3/untitled2.py', wdir='C:/Users/NANCY/.spyder-py3')
runfile('C:/Users/NANCY/.spyder-py3/untitled2.py', wdir='C:/Users/NANCY/.spyder-py3')
runfile('C:/Users/NANCY/.spyder-py3/Actividad8-Codigo.py', wdir='C:/Users/NANCY/.spyder-py3')
runfile('C:/Users/NANCY/.spyder-py3/untitled2.py', wdir='C:/Users/NANCY/.spyder-py3')
runfile('C:/Users/NANCY/.spyder-py3/untitled3.py', wdir='C:/Users/NANCY/.spyder-py3')
runfile('C:/Users/NANCY/.spyder-py3/untitled3.py', wdir='C:/Users/NANCY/.spyder-py3')
runfile('C:/Users/NANCY/.spyder-py3/Actividad8-Codigo.py', wdir='C:/Users/NANCY/.spyder-py3')
runfile('C:/Users/NANCY/.spyder-py3/untitled3.py', wdir='C:/Users/NANCY/.spyder-py3')

## ---(Fri Apr 12 23:35:44 2024)---
runfile('C:/Users/NANCY/.spyder-py3/tareaSubir.py', wdir='C:/Users/NANCY/.spyder-py3')

## ---(Tue Apr 23 11:19:26 2024)---
runfile('C:/Users/NANCY/.spyder-py3/Actividad9.py', wdir='C:/Users/NANCY/.spyder-py3')
print(data.columns)
runfile('C:/Users/NANCY/.spyder-py3/Actividad9.py', wdir='C:/Users/NANCY/.spyder-py3')
runfile('C:/Users/NANCY/.spyder-py3/Actividad9DOS.py', wdir='C:/Users/NANCY/.spyder-py3')
runfile('C:/Users/NANCY/.spyder-py3/Actividad9DOS.py', wdir='C:/Users/NANCY/.spyder-py3')
runfile('C:/Users/NANCY/.spyder-py3/Actividad9.py', wdir='C:/Users/NANCY/.spyder-py3')
runfile('C:/Users/NANCY/.spyder-py3/Actividad9DOS.py', wdir='C:/Users/NANCY/.spyder-py3')
runfile('C:/Users/NANCY/.spyder-py3/Actividad9DOS.py', wdir='C:/Users/NANCY/.spyder-py3')

## ---(Tue Apr 23 14:12:05 2024)---
runfile('C:/Users/NANCY/.spyder-py3/Actividad9DOS.py', wdir='C:/Users/NANCY/.spyder-py3')
runfile('C:/Users/NANCY/.spyder-py3/untitled0.py', wdir='C:/Users/NANCY/.spyder-py3')
runfile('C:/Users/NANCY/.spyder-py3/Actividad9DOS.py', wdir='C:/Users/NANCY/.spyder-py3')

## ---(Wed Apr 24 14:31:39 2024)---
runfile('C:/Users/NANCY/.spyder-py3/Actividad9DOS.py', wdir='C:/Users/NANCY/.spyder-py3')
runfile('C:/Users/NANCY/.spyder-py3/Actividad9.py', wdir='C:/Users/NANCY/.spyder-py3')
runfile('C:/Users/NANCY/.spyder-py3/Actividad9.py', wdir='C:/Users/NANCY/.spyder-py3')
runfile('C:/Users/NANCY/.spyder-py3/Actividad9DOS.py', wdir='C:/Users/NANCY/.spyder-py3')
runfile('C:/Users/NANCY/.spyder-py3/untitled0.py', wdir='C:/Users/NANCY/.spyder-py3')
runfile('C:/Users/NANCY/.spyder-py3/Actividad9DOS.py', wdir='C:/Users/NANCY/.spyder-py3')
runfile('C:/Users/NANCY/.spyder-py3/untitled0.py', wdir='C:/Users/NANCY/.spyder-py3')
runfile('C:/Users/NANCY/.spyder-py3/Actividad9DOS.py', wdir='C:/Users/NANCY/.spyder-py3')
runfile('C:/Users/NANCY/.spyder-py3/untitled0.py', wdir='C:/Users/NANCY/.spyder-py3')
runfile('C:/Users/NANCY/.spyder-py3/untitled1.py', wdir='C:/Users/NANCY/.spyder-py3')
runfile('C:/Users/NANCY/.spyder-py3/Actividad9DOS.py', wdir='C:/Users/NANCY/.spyder-py3')
runfile('C:/Users/NANCY/.spyder-py3/untitled1.py', wdir='C:/Users/NANCY/.spyder-py3')

## ---(Thu Apr 25 10:00:19 2024)---
runfile('C:/Users/NANCY/.spyder-py3/Actividad9TRES.py', wdir='C:/Users/NANCY/.spyder-py3')

## ---(Sun May 19 20:44:01 2024)---
runfile('C:/Users/NANCY/.spyder-py3/untitled0.py', wdir='C:/Users/NANCY/.spyder-py3')

## ---(Sun May 19 23:35:05 2024)---
runfile('C:/Users/NANCY/.spyder-py3/untitled0.py', wdir='C:/Users/NANCY/.spyder-py3')

## ---(Thu May 23 16:48:26 2024)---
runfile('C:/Users/NANCY/.spyder-py3/untitled0.py', wdir='C:/Users/NANCY/.spyder-py3')
runfile('C:/Users/NANCY/.spyder-py3/untitled1.py', wdir='C:/Users/NANCY/.spyder-py3')
runfile('C:/Users/NANCY/.spyder-py3/Parte1.py', wdir='C:/Users/NANCY/.spyder-py3')

## ---(Thu Oct 24 15:31:04 2024)---
runfile('C:/Users/NANCY/.spyder-py3/untitled0.py', wdir='C:/Users/NANCY/.spyder-py3')
pip install termcolor
runfile('C:/Users/NANCY/.spyder-py3/untitled0.py', wdir='C:/Users/NANCY/.spyder-py3')