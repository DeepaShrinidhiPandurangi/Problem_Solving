'''Write a procedure called oddTuples, which takes a tuple as input, and returns a new tuple as output, where every other element of the input tuple is copied, starting with the first one. So if test is the tuple ('I', 'am', 'a', 'test', 'tuple'), then evaluating oddTuples on this input would return the tuple ('I', 'a', 'tuple').'''

def oddTuples(aTup):
  o = ()
  for i in range(0,len(aTup)):
    if i%2 == 0:
      o = o + (aTup[i],)

  return o

aTup = ('I', 'am', 'a', 'test', 'tuple')
print(oddTuples(aTup))

# Shorter way using slicing : t[start:stop:step]
def oddTuples(aTup):
 oddT = aTup[::2]
 return oddT