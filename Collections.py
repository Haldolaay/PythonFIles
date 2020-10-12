
import collections

arr = collections.Counter('hamzah')
print(arr)
arr = collections.Counter()     
print(arr)                     
c = collections.Counter('so this should work somehow')
print(arr) 
c = collections.Counter({'red': 4, 'blue': 2})
print(arr) 
c = collections.Counter(how=4, what=8)        
print(arr)
def lowest(s):
    if not s: return 0
    yo = collections.Counter(s)
    pairs,seeds = map(sum, zip(*(divmod(n,2) for n in yo.values())))
    return len(s) if not seeds else pairs//seeds*2+1
print(lowest('hamzah'))
