#!/usr/bin/env python3
import sys, csv
sniffer = csv.Sniffer()
first = sys.stdin.read(4096)
delim = '|'
try:
    dialect = sniffer.sniff(first, delimiters=",|;\t")
    delim = dialect.delimiter
except Exception:
    pass
sys.stdin = sys.__stdin__
sys.stdin = open(0, 'r')
reader = csv.reader([first] + list(sys.stdin), delimiter=delim)

for row in reader:
    if len(row) < 2:
        continue
    custkey = row[1].strip()
    if custkey:
        print(f"{custkey}\t1")
