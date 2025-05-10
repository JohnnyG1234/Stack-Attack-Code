from collections import Counter

StringToCount = "mississippi"

# trad way

counts =  {}

for c in StringToCount:
    try:
        counts[c] += 1
    except KeyError:
        counts[c] = 1

print(counts)

# new method
newCounts = Counter(StringToCount)

print(newCounts)