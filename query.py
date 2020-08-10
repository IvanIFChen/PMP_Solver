import gensim
import sys

'''
This queries a pre-trained model from the file system. If missing an input 
param, it will look at `sample_paragraph.txt` as the input question instead.
'''

model = gensim.models.Doc2Vec.load('saved_model')

if len(sys.argv) > 1:
    question = sys.argv[1]
else:
    with open('sample_paragraph.txt', 'r') as f:
        question = f.read()

print('Sample Text: «{}»\n'.format(question))

test_doc = gensim.utils.simple_preprocess(question)

inferred_vector = model.infer_vector(test_doc)
sims = model.docvecs.most_similar([inferred_vector], topn=len(model.docvecs))

with open('pmp_questions.txt', 'r') as f:
    lines = f.readlines()

    for label, index in [('MOST', 0), ('SECOND', 1), ('THIRD', 2), ('MEDIAN', len(sims)//2), ('LEAST', len(sims) - 1)]:
        print(u'%s %s: «%s»\n' % (label, sims[index], lines[sims[index][0]].strip()))
