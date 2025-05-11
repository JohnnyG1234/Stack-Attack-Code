from collections import Counter
# get the counts of this string!!!
StringToCount = "mississippi"


# trad way!

counts = {}
for c in StringToCount:
    try:
        counts[c] += 1
    except KeyError:
        counts[c] = 1

#print(counts)


newCounts = Counter(StringToCount)

print(newCounts)
