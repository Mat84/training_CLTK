#!/usr/bin/env python3 
import greek_module as gk


from cltk.corpus.utils.importer import CorpusImporter

greek = CorpusImporter('greek')

#print(greek.list_corpora)

greek.import_corpus('tlg', '~/cltk_data/originals/TLG_E/')

from cltk.corpus.greek.tlg.parse_tlg_indices import get_female_authors

from cltk.corpus.greek.tlg.parse_tlg_indices import get_epithet_index

from cltk.corpus.greek.tlg.parse_tlg_indices import get_epithets

from cltk.corpus.greek.tlg.parse_tlg_indices import select_authors_by_epithet

from cltk.corpus.greek.tlg.parse_tlg_indices import get_epithet_of_author

from cltk.corpus.greek.tlg.parse_tlg_indices import get_geo_index

from cltk.corpus.greek.tlg.parse_tlg_indices import get_geographies

from cltk.corpus.greek.tlg.parse_tlg_indices import select_authors_by_geo

from cltk.corpus.greek.tlg.parse_tlg_indices import get_geo_of_author

from cltk.corpus.greek.tlg.parse_tlg_indices import get_lists

from cltk.corpus.greek.tlg.parse_tlg_indices import get_id_author

from cltk.corpus.greek.tlg.parse_tlg_indices import select_id_by_name

select_id_by_name('novum')

from cltk.corpus.utils.formatter import tlg_plaintext_cleanup
import os

file = os.path.expanduser('~/cltk_data/greek/text/tlg/plaintext/TLG0031.TXT')

with open(file) as f:
    r = f.read()

#print(r)

tlg_plaintext_cleanup(r, rm_punctuation=True, rm_periods=False)

from cltk.tokenize.word import WordTokenizer

word_tokenizer = WordTokenizer('greek')

text = r

#print(word_tokenizer.tokenize(text))

from nltk.tokenize.punkt import PunktLanguageVars

from cltk.stop.greek.stops import STOPS_LIST

sentence = r

p = gk.PunktLanguageVars_greek()

tokens = p.word_tokenize(sentence.lower())


#ACCRESCIMENTO STOPS_LIST
STOPS_LIST.extend(['.', ',', "'", '·', '[',']',';','·', '-'])
#print(STOPS_LIST)

tokens_no_punctuation = [w for w in tokens if w not in STOPS_LIST]

tokens_clean = [w.strip('.') for w in tokens_no_punctuation]

#print([w for w in tokens if w not in STOPS_LIST])


#questo ciclo serve per stampare gli elementi della lista senza parentesi e virgole
for j in tokens_clean:
	print(j)  





