# -*- coding:utf-8 -*-
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

sentence = "'I suppose I could,' I said. 'What sort of stories does he like?'"

# 품사 태깅
# import nltk   
# nltk.download("averaged_perceptron_tagger_eng")

wt = word_tokenize(sentence)
# 단어 list -> (단어, 품사) list : tuple
wt = pos_tag(wt)
for w in wt:
    print(w)