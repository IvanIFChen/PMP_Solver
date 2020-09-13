import re

with open('test.txt', 'r') as f:
    with open('matches.txt', 'w') as out:
        for i in re.findall(r'\s+([A-Z][\s\S]+?[.?!])', f.read()):
            txt = re.sub(r'\n', ' ', i)
            txt = re.sub(r'\s+', ' ', txt)
            out.write(txt)
            out.write('\n')
