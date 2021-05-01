#3. Longest Substring Without Repeating Characters
def lengthOfLongestSubstring(s):
  d = {}
  longest = 0
  i = 0
  for j,k in enumerate(s):
    if k in d:
      i = max(i,d[k]+1)
    longest = max(longest,j-i+1)
    d[k] = j
  return longest

print(lengthOfLongestSubstring("pwwkew"))