import collections
import os
import gensim
import smart_open

# Reference from https://radimrehurek.com/gensim/auto_examples/tutorials/run_doc2vec_lee.html#sphx-glr-auto-examples-tutorials-run-doc2vec-lee-py 

train_file = 'pmp_questions.txt'

# Preprocess train data

def read_corpus(fname, tokens_only=False):
    with smart_open.open(fname, encoding="iso-8859-1") as f:
        for i, line in enumerate(f):
            tokens = gensim.utils.simple_preprocess(line)
            if tokens_only:
                yield tokens
            else:
                # For training data, add tags
                yield gensim.models.doc2vec.TaggedDocument(tokens, [i])

train_corpus = list(read_corpus(train_file))

# Initialize a model
# model = gensim.models.doc2vec.Doc2Vec(vector_size=50, min_count=2, epochs=40)
model = gensim.models.doc2vec.Doc2Vec(vector_size=30, min_count=2, epochs=80)

# Build a vocabulary
model.build_vocab(train_corpus)

# Begin training
model.train(train_corpus, total_examples=model.corpus_count, epochs=model.epochs)

# Assessing model (sanity check)
ranks = []
second_ranks = []
for doc_id in range(len(train_corpus)):
    inferred_vector = model.infer_vector(train_corpus[doc_id].words)
    sims = model.docvecs.most_similar([inferred_vector], topn=len(model.docvecs))
    rank = [docid for docid, sim in sims].index(doc_id)
    ranks.append(rank)

    second_ranks.append(sims[1])

counter = collections.Counter(ranks)
print(counter)
print(f'Model Consistency: {counter[0]/sum(counter.values())}')

# save the trained model
model.save('saved_model')
