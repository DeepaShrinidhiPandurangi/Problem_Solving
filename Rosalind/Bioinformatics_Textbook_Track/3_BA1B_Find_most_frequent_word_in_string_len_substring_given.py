# 3. BA1B . Find the most frequent words in a string 

s="ACGTTGCATGTCGCATGATGCATGAGAGCT"

k = 4
Dict = {}
for i in range(0,len(s)):
  if len(s[i:i+k]) == k: # We do not want to count substrings whose lengths are smaller than the value of "k".
    Dict[s[i:i+k]] = s.count(s[i:i+k])
#print(Dict)

for key,value in Dict.items():
  if value == max(Dict.values()):
      print(key,end=" ")
 
'''
{'ACGT': 1, 'CGTT': 1, 'GTTG': 1, 'TTGC': 1, 'TGCA': 2, 'GCAT': 3, 'CATG': 3, 'ATGT': 1, 'TGTC': 1, 
'GTCG': 1, 'TCGC': 1, 'CGCA': 1, 'ATGA': 2, 'TGAT': 1, 'GATG': 1, 'ATGC': 1, 'TGAG': 1, 'GAGA': 1, 'AGAG': 1, 'GAGC': 1, 'AGCT': 1}


GCAT CATG 
'''