#!/usr/bin/env python3
import sys
cur = None
s = 0.0
n = 0
for line in sys.stdin:
    parts = line.rstrip('\n').split('\t')
    if len(parts) != 2:
        continue
    k, v = parts
    try:
        vf = float(v)
    except:
        continue
    if k == cur:
        s += vf; n += 1
    else:
        if cur is not None and n > 0:
            print(f"{cur}\t{s/n:.6f}")
        cur = k
        s = vf; n = 1
if cur is not None and n > 0:
    print(f"{cur}\t{s/n:.6f}")
