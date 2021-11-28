#!/usr/bin/env python3


import re
import sys

try:
    sys.argv[2]
    sys.argv[1]
except:
    print(
          'first param - input file, second param - output file \n'
          'example: sys.argv[0] file_input.sh file_output.sh'
    )
    sys.exit(1)

file_from = sys.argv[1]
file_to = sys.argv[2]


def modif(file_from,file_to):
    a = open(file_from,'r')
    lines = a.read().splitlines()
    a.close()
    b = open(file_to,'w')
    for line in lines:
        if re.match('^\s{10}',line):
            x = re.sub('^\s{10}',' ' * 20,line)
            b.write(x)
            b.write('\n')
        elif re.match('^\s{8}',line):
            x = re.sub('^\s{8}',' ' * 16,line)
            b.write(x)
            b.write('\n')
        elif re.match('^\s{6}',line):
            x = re.sub('^\s{6}',' ' * 12,line)
            b.write(x)
            b.write('\n')
        elif re.match('^\s{4}',line):
            x = re.sub('^\s{4}',' ' * 8,line)
            b.write(x)
            b.write('\n')
        elif re.match('^\s{2}',line):
            x = re.sub('^\s{2}',' ' * 4,line)
            b.write(x)
            b.write('\n')
        else:
            b.write(line)
            b.write('\n')
    b.close()

if __name__ == "__main__":
    try:
        modif(file_from,file_to)
    except Exception as e:
        print('Have error: {}'.format(e))
