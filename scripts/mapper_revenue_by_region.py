#!/usr/bin/env python3
import sys, csv, os

def load_lookup(path, key_idx, val_idx, delimiter='|'):
    d = {}
    if not os.path.exists(path):
        return d
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        sniffer = csv.Sniffer()
        sample = f.read(4096)
        f.seek(0)
        delim = delimiter
        try:
            dialect = sniffer.sniff(sample, delimiters=",|;\t")
            delim = dialect.delimiter
        except Exception:
            pass
        reader = csv.reader(f, delimiter=delim)
        for row in reader:
            if len(row) <= max(key_idx, val_idx):
                continue
            d[row[key_idx].strip()] = row[val_idx].strip()
    return d

SUPPLIER = os.environ.get("SUPPLIER_FILE", "supplier.csv")
NATION   = os.environ.get("NATION_FILE",   "nation.csv")
REGION   = os.environ.get("REGION_FILE",   "region.csv")

supp_to_nation = load_lookup(SUPPLIER, key_idx=0, val_idx=3)
nation_to_region = load_lookup(NATION, key_idx=0, val_idx=2)
region_to_name   = load_lookup(REGION, key_idx=0, val_idx=1)

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
    if len(row) < 7:
        continue
    suppkey = row[2].strip()
    extprice = row[5].strip()
    discount = row[6].strip()
    try:
        extprice = float(extprice)
        discount = float(discount)
    except ValueError:
        continue
    nationkey = supp_to_nation.get(suppkey)
    if nationkey is None:
        continue
    regionkey = nation_to_region.get(nationkey)
    regionname = region_to_name.get(regionkey, "UNKNOWN")
    revenue = extprice * (1.0 - discount)
    print(f"{regionname}\t{revenue:.6f}")
