#!/usr/bin/python3
"""Performs log parsing from stdin"""
import sys


out = sys.stdin
def parsing():
    """Parsing the giving"""
    lists = []
    items = 0
    status = {}
    
    try:
        for lines in out:
            d = lines.strip().split()
            helping(d, lists, items, status)
    except KeyboardInterrupt:
        return
    
def helping(output, l, i, s):
    """Helping in parsing the giving"""
    code = int(output[-2])
    size = int(output[-1])
    if isinstance(code, int) and isinstance(size, int):
        diction = {'status_code': code, 'file_size': size}
        l.append(diction)
        if len(l) == 10:
            for item in l:
                i = i + item.get('file_size')
                c = item.get('status_code')
                s[c] = s.get(c, 0) + 1
            print(f'File size: {i}')
            for key, value in sorted(s.items()):
                print(f'{key}: {value}')
            print(l)
            l.clear()

if __name__ == "__main__":
    parsing()
