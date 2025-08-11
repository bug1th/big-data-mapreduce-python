#!/usr/bin/env python3
import sys
current_key = None
acc = 0.0
for line in sys.stdin:
    parts = line.rstrip('\n').split('\t')
    if len(parts) != 2:
        continue
    key, val = parts
    try:
        valf = float(val)
    except:
        continue
    if key == current_key:
        acc += valf
    else:
        if current_key is not None:
            print(f"{current_key}\t{acc:.6f}")
        current_key = key
        acc = valf
if current_key is not None:
    print(f"{current_key}\t{acc:.6f}")
