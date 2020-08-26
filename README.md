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
### Training the model 
Simply run `python train.py` to train the model, it should display a sanity check value to show the consistency of the model. Saved to file system as `saved_model`.

### Querying the model
Running `python query.py` should allow you to query the model. By default, it queries the `sample_paragraph.txt` file as the input question, you can also pass it in as an input param.

### When done
Do `deactivate` to deactivate the virtual environment.

### Sample Output
```
Counter({0: 397, 3: 2, 1: 1})
Model Consistency: 0.9925
Sample Text: «When you review cost performance data on your project, different responses will be required depending on the degree of variance or control thresholds from the baseline.»

MOST (131, 0.8644323348999023): «when you review cost performance data on your project different responses will be required depending on the degree of variance or control thresholds from the baseline for example variance of percent might not require immediate action whereas variance of percent will require investigation description of how you plan to manage cost variances should be included in theâ»

SECOND (101, 0.8074396848678589): «schedule performance index of less than indicates that theâ»

MEDIAN (169, 0.3390151858329773): «your project scheduler has just started working with your project and has produced defective reports for the past two accounting cycles if this continues these defective reports could provide the potential for customer dissatisfaction and lost productivity that is due to rework you discovered that the project scheduler needs additional training on using the scheduling tool that is used on your project the cost of training falls under which one of the following categories»

LEAST (8, -0.2862987220287323): «interpersonal and team skills are used throughout project management your company is embarking on project to completely eliminate defects in its products you are the project manager for this project and you are developing your project charter to assist you which of the following interpersonal and team skills do you plan to useâ»
```

## Open Issues
* Still need to figure out the best parameters (size, epoch... etc) for the model.
  - While this is similar to the example code, some of the documents are much smaller, need to do some more research.
* Some questions doesn't fit to our application:
  - some too short, we want a scenario
  - some have diagrams, info already lost during pdf to txt conversion, so disregard those too (maybe possible through regex)
* Issue parsing 4.pdf, parsing function (pdftotext) seems to have trouble parsing things correctly for some texts. It's adding/removing spaces at sentences.

## References
* https://radimrehurek.com/gensim/auto_examples/tutorials/run_doc2vec_lee.html#sphx-glr-auto-examples-tutorials-run-doc2vec-lee-py

# Test
