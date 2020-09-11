from math import floor
import pandas as pd

from nltk import pos_tag as tag
from nltk import word_tokenize as tok

def main():
       text = 'Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in ' \
              'Liberty, and dedicated to the proposition that all men are created equal. Now we are engaged in a great ' \
              'civil war, testing whether that nation, or any nation so conceived and so dedicated, can long endure. We are ' \
              'met on a great battle-field of that war. We have come to dedicate a portion of that field, as a final ' \
              'resting place for those who here gave their lives that that nation might live. It is altogether fitting and ' \
              'proper that we should do this. But, in a larger sense, we can not dedicate -- we can not consecrate -- we ' \
              'can not hallow -- this ground. The brave men, living and dead, who struggled here, have consecrated it, far ' \
              'above our poor power to add or detract. The world will little note, nor long remember what we say here, but ' \
              'it can never forget what they did here. It is for us the living, rather, to be dedicated here to the ' \
              'unfinished work which they who fought here have thus far so nobly advanced. It is rather for us to be here ' \
              'dedicated to the great task remaining before us -- that from these honored dead we take increased devotion ' \
              'to that cause for which they gave the last full measure of devotion -- that we here highly resolve that ' \
              'these dead shall not have died in vain -- that this nation, under God, shall have a new birth of freedom -- ' \
              'and that government of the people, by the people, for the people, shall not perish from the earth.'
       text_tok = tok(text)
       text_pos = pd.DataFrame(tag(text_tok), columns=['words', 'pos tags'])
       text_pos.insert(0, 'key', list(range(len(text_pos.index))))
       print(text_pos)

       repl_pos = {'pos tags': ['CD', 'JJ', 'JJR', 'JJS', 'NN', 'NNS', 'NNP', 'NNPS', 'RB', 'RBR', 'RBS'],
                   'pos names': ['number', 'adjective', 'comparative adjective', 'superlative adjective', 'singular noun',
                                 'plural noun', 'proper noun', 'plural proper noun', 'adverb', 'comparative adverb',
                                 'superlative adverb']}
       repl_pos = pd.DataFrame(data=repl_pos)

       print(repl_pos)

       text_repl = pd.merge(text_pos, repl_pos, on='pos tags', how='inner')
       text_repl['key'] = text_repl['key'].astype(int)

       print(text_repl)

       sparsity = 7
       repl_num = floor(len(text_repl.index) / sparsity)

       replace = text_repl.sample(n=repl_num)
       new_words = ['_____'] * repl_num
       replace.insert(4, 'new words', new_words)

       print(replace)

       output = ''
       #for i in range(len(text_pos.index)):
       #    if i in replace[key]:
       #        output = output +

if __name__ == "main":
       main()