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
* ~Datasize is too small. Most sources are doing 10s, 100s, or even millions of dataset for training. What I have is definitely not enough.~ Now around 3k with some duplicates
* Some questions doesn't fit to our application:
  - some too short, we want a scenario
  - some have diagrams, info already lost during pdf to txt conversion, so disregard those too (maybe possible through regex)
* ~Source PDFs have duplicate questions, causing the model consistency to be very low, if we see carefully there are a bunch of 2, 3 ranks, they are likely caused by duplicates. May need to find a way to remove them, maybe do a diff? Say if difference in chars is < 5 then we assume they are a duplicate.~ Created a way to remove *identical* sentences.
* Run time on my 2016 MBP is around 1:30, need to consider [saving](https://tedboy.github.io/nlps/generated/generated/gensim.models.Doc2Vec.save.html) the model when we have decent result.
* Issue parsing 4.pdf, parsing function (pdftotext) seems to have trouble parsing things correctly for some texts. It's adding/removing spaces at sentences.

## References
* https://radimrehurek.com/gensim/auto_examples/tutorials/run_doc2vec_lee.html#sphx-glr-auto-examples-tutorials-run-doc2vec-lee-py
