import re

'''
This little script will parse out all "Practice Questions" from the 
input text (which is just the text from the pdf).

The process has two steps:
1.  Capture all text between "Practice Questions" and "Answer Sheet",
    this should contain all the "questions" that we want.
2.  For each of the captures from previous step, we look for question
    index ("1.", "2.", "3."... etc) then capture the text of the 
    questions.

Then it writes all questions to an "output.txt" file.

'''


content = ''

with open('pmp_original.txt', 'r') as f:
    content = f.read()

matches = re.findall(r'Practice Questions([\S\s]*?)Answer Sheet', content)

with open('pmp_questions.txt', 'w+') as f:
    for question in matches:
        q_texts = re.findall(r'\d\.([\S\s]*?)a\.', question)
        for text in q_texts:
            # remove repeating whitespaces
            text = re.sub(r'\s+', ' ', text)
            # foo- bar" -> "foobar"
            text = re.sub(r'- ', '', text)
            text = text.strip()
            f.write(text + '\n')
