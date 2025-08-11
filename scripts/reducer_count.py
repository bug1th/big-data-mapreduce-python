#!/usr/bin/env python3
import sys
current = None
cnt = 0
for line in sys.stdin:
    parts = line.rstrip('\n').split('\t')
    if len(parts) != 2:
        continue
    key, val = parts
    try:
        n = int(val)
    except:
        continue
    if key == current:
        cnt += n
    else:
        if current is not None:
            print(f"{current}\t{cnt}")
        current = key
        cnt = n
if current is not None:
    print(f"{current}\t{cnt}")
