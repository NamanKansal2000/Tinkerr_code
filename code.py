# coded in python
from collections import Counter
def func(arr):
    dict = Counter(arr)
    count = 0
    for i in dict:
        val = dict[i]-1
        count+=((val*(val+1))//2)
    return count

arr = [1,2,3,1,2,1]
print(func(arr))

# time complexity - O(N)
# Space complexity - O(N)


# Q2
keys = ["idea", "idae", "bsnl", "nsbl", "grasim", "bata"]

def anagram(arr):
    d = dict()
    ls = []
    for i in arr:
        val = ''.join(sorted(list(i)))
        if val in d:
            ls[d[val]].append(i)
        else:
            ls.append([i])

            d[val] = len(ls)-1
    return ls

print(anagram(keys))
# time complexity - O(nlog(mlen(m))) where m is len(word)
# Space complexity - O(n)
