import re

'''
This little script will parse out all "Practice Questions" from the input text 
(which is just the text from the pdfs). Then it writes all questions to an 
output file.

`doc_regexs` is a convenient data structure for specifying regex(es) for each 
document.
    "target" - the document name
    "regexs" - a list of list of regex pattern, each list of regex pattern
            is a multi-level regex match.
            First level of regex match is searched on the entire document.
            Second (and on) level of regex match is search from each of the
            previous matches
            e.g. document: "Apple, Banana, Carrot, Dot"
                            and we have [r'[ABC](...)', r'((.)\2)']
                            -> ["ppl", "ana", "arr"]
                            -> ["pp",  "rr"]
                            sanatize results and write to output document.
'''

doc_regexs = [
    {
        'target': 1,
        'regexs': [
            # "PMP Lite Mock Exam" and "Knowledge Area Quiz"
            # (1044 questions) TODO: didn't confirm
            [r'Test Questions\n([\S\s]*?)Answer Key and Explanations', r'\d\. ([\S\s]*?)A\.']
        ]
    },
    {
        'target': 2,
        'regexs': [
            # "Practice Questions" (400 questions)
            [r'Practice Questions\n([\S\s]*?)Answer Sheet', r'\d\. ([\S\s]*?)a\.'],
            # "Practice Test" at the end (200 questions)
            [r'\nPractice Test\n\n([\s\S]*?)Answer Sheet', r'\d\. ([\S\s]*?)a\.']
        ]
    },
    {
        'target': 4,
        'regexs': [
            # "Practice Questions" (400 questions)
            [r'Practice Questions\n([\s\S]*?)Answer Sheet', r'\d\. ([\S\s]*?)a\.'],
            # "Practice Test" at the end (200 questions)
            [r'\nPractice Test\n\n([\s\S]*?)Answer Sheet', r'\d\. ([\S\s]*?)a\.']
        ]
    },
    {
        'target': 5,
        'regexs': [
            # "Practice Questions" (400 questions)
            [r'Practice Questions\n([\s\S]*?)Answer Sheet', r'\d\. ([\S\s]*?)a\.'],
            # "Practice Test" at the end (200 questions)
            [r'\nPractice Test\n\n([\s\S]*?)Answer Sheet', r'\d\. ([\S\s]*?)a\.']
        ]
    },
    {
        'target': 6,
        'regexs': [
            # "Review Questions" at the end of each chapter
            # (~187 questions) TODO: didn't confirm
            [r'Review Questions\n([\s\S]*?)(?:CHAPTER|APPENDIX)', r'\d\. ([\S\s]*?)A\.']
        ]
    }
]

with open('pmp_questions.txt', 'w+') as out_file:
    for doc in doc_regexs:
        in_file_name = f'data/{doc["target"]}.txt'
        print('working on', in_file_name)
        with open(in_file_name, 'r') as in_file:
            content = in_file.read()
        for rs in doc['regexs']:
            if not rs:
                raise Exception('Require at least a regex per doc range')
            # the first level of regex match is applied to the entire document
            matches = re.findall(rs.pop(0), content)
            # rest are matches for all previous matches
            for r in rs:
                # perform the operation and flattens the list
                matches = [new_matches for match in matches for new_matches in re.findall(r, match)]
            # sanatization
            for match in matches:
                # remove repeating whitespaces
                match = re.sub(r'\s+', ' ', match)
                # foo- bar" -> "foobar"
                match = re.sub(r'- ', '', match)
                match = match.strip()
                out_file.write(match + '\n')
