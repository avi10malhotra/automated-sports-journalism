


import glob

files_summary = sorted(glob.glob('/Users/avimalhotra/Desktop/Uni/Year4/CS4514 FYP/FYP Code/summaries/*.csv'))
print(files_summary)

files_testing = sorted(glob.glob('/Users/avimalhotra/Desktop/Uni/Year4/CS4514 FYP/FYP Code/testing/*.csv'))
print(files_testing)

summary = []
testing = []

for i in range(64):
    with open(files_testing[i], 'r') as t:
        line_t = t.readline().strip('\n').strip('\t')
        while line_t == '\n'or line_t == '':
            line_t = t.readline().strip('\n').strip('\t')
    t.close()

    testing.append(line_t)

    with open(files_summary[i], 'r') as s:
        line_s = s.readline().strip('\n').strip('\t')
        while line_s == '\n' or line_s == '':
            line_s = s.readline().strip('\n').strip('\t')
    s.close()

    summary.append(line_s)

with open('testing_file.txt', 'w') as f:
    for line in testing:
        f.write(line + '\n')
f.close()

with open('summary_file.txt', 'w') as f:
    for line in summary:
        f.write(line + '\n')
f.close()


