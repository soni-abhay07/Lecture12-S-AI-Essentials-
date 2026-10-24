import sys
from collections import Counter

filename = sys.argv[1]
with open(filename) as f:
    lines = f.readlines()

print("Total lines:", len(lines))

counts = Counter()
for line in lines:
    fields = line.split()
    if len(fields) > 4:
        key = fields[4] 
        counts[key] += 1

print("Top 5:")
for item, n in counts.most_common(5):
    print(item, n)