import sys
import re

infile = open(sys.argv[1], 'r')
outfile = open(sys.argv[2], 'w')
lineinfo = []
repeat = False #used to prevent blank space at the start of the file

for line in infile:

        #pull position and id
        if '>' in line[0]:
                if repeat:
                        outfile.write('\n')
                lineinfo = line.lstrip().rstrip().split('|')

                m = re.search('[0-9]+\.[A-Z]+\.[0-9]+\.[0-9]+\.[0-9]+', lineinfo[3]) ##match Sequence ID in last segment
                outfile.write(m.group(0) + '-' + lineinfo[2] + '\t') ##write ID / location

        #pull sequence
        else:
                outfile.write(line.lstrip().rstrip()) ##Write protein sequence

        repeat = True
