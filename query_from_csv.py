import subprocess 
import csv

'''
This script will automatically fetch all `Content` column from the csv file,
perform query using `query.py`, then save all the stdout to an text file.
'''

def run(question):
    cmd = ['python', 'query.py', f'"{question}"']
    print(' '.join(cmd))
    out = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout,stderr = out.communicate()
    return stdout.decode('utf8')
with open('query_from_csv_output.txt', 'w+') as out_file:
    with open('pm_problems.csv', 'r') as f:
        reader = csv.reader(f, delimiter=',')
        for i, row in enumerate(reader):
            if not i:
                continue
            output = run(row[2])
            out_file.write(output)
            out_file.write('\n---------------\n\n\n')
