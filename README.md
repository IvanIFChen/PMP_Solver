# PMP_Solver
A "Problem Solver" tool using Gensim's Doc2Vec implementation to answer general project management questions. Model is trained using a PMP exam prep questions.

## Code Overview
### /parse_questions.py
Parses all questions from the PMP exam prep pdf file.

### /train.py
Trains the model from pmp_questions.txt and then find the most similar one from sample_paragraph.txt.

## How to run
### Setup virtual environment
```
virtualenv -p python3 venv
. ./venv/bin/activate
pip install -r requirements.txt
```
### Running the model
Edit `sample_paragraph.txt` to desired sample text, then
```
python train.py
```

Then do `deactivate` to deactivate the virtual environment.

## References
* https://radimrehurek.com/gensim/auto_examples/tutorials/run_doc2vec_lee.html#sphx-glr-auto-examples-tutorials-run-doc2vec-lee-py
