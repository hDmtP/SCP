#!/bin/python3
import os
import sys

## THIS IS IN TESTING PHRASE

os.system(f'''
./scp_detail.py {sys.argv[1]} > 1.txt
''')

with open('1.txt', 'rt') as lines:
    for line in lines:
        if line.startswith('rating') or line.startswith('Item') or line.startswith('Object Class') or line.startswith('Special Containment') or line.startswith('Description') or line.startswith('Safe'.lower()) or line.startswith('Euclid'.lower()) or line.startswith('Keter'.lower()):
            print(line)

os.system('rm 1.txt')
