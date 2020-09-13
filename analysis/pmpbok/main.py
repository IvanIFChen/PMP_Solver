import nltk
import csv

def tokenize(s):
    tokens = nltk.word_tokenize(s)
    tagged = nltk.pos_tag(tokens)
    return tagged

# output.csv
# with open('output.csv', 'w') as out:
#     writer = csv.writer(out, delimiter=',')
#     writer.writerow(['Original', 'POS'])

#     with open('matches.txt', 'r') as f:
#         for line in f.readlines():
#             line = line.strip()
#             tags = tokenize(line)
#             writer.writerow([line, [t[1] for t in tags]])

# unique_pos.txt
# unique_pos = set()
# with open('matches.txt', 'r') as f:
#     for line in f.readlines():
#         tags = tokenize(line)
#         unique_pos.add(' '.join([x[1] for x in tags]))
#     with open('unique_pos.txt', 'w+') as out:
#         for v in sorted(list(unique_pos)):
#             out.write(v + '\n')

# unique_verbs.txt
# verbs = set()
# with open('matches.txt', 'r') as f:
#     for i, line in enumerate(f.readlines()):
#         for t in tokenize(line):
#             if t[1].startswith('VB'):
#                 verbs.add(t[0].lower())
#     with open('unique_verbs.txt', 'w+') as out:
#         for v in sorted(list(verbs)):
#             out.write(v + '\n')