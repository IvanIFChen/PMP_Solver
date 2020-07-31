# PMP_Solver
A "Problem Solver" tool using Gensim's Doc2Vec implementation to answer general project management questions. Model is trained using a PMP exam prep questions.

## Code Overview
### /parse_questions.py
Parses all questions from the PMP exam prep pdf file.

### /train.py
Trains the model from `pmp_questions.txt` and then find the most similar one from `sample_paragraph.txt`.

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

## Open Issues
* Still need to figure out the best parameters (size, epoch... etc) for the model.
  - While this is similar to the example code, some of the documents are much smaller, need to do some more research.
* Datasize is too small. Most sources are doing 10s, 100s, or even millions of dataset for training. What I have is definitely not enough.
