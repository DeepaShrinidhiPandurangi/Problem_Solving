# Computing GC Content 
'''Identifying Unknown DNA Quickly:
Problem
The GC-content of a DNA string is given by the percentage of symbols in the string that are 'C' or 'G'. For example, the GC-content of "AGCTATAG" is 37.5%.
 Note that the reverse complement of any DNA string has the same GC-content.
DNA strings must be labeled when they are consolidated into a database. A commonly used method of string labeling is called FASTA format.
 In this format, the string is introduced by a line that begins with '>', followed by some labeling information. 
Subsequent lines contain the string itself; the first line to begin with '>' indicates the label of the next string.
In Rosalind's implementation, a string in FASTA format will be labeled by the ID "Rosalind_xxxx", where "xxxx" denotes a four-digit code between 0000 and 9999.
Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. 
Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.'''

import io
 
FASTA='''>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT'''
 
infile = io.StringIO(FASTA)
count = 0
percentage =0
name = None
seqs = dict()
for line in infile: #or i,j in enumerate(infile)
    #let's discard the newline at the end (if any)
    line = line.rstrip()
    #distinguish header from sequence
    if line[0]=='>': #or line.startswith('>')
        #it is the header
        name = line[1:] #discarding the initial >
        seqs[name] = '' # no sequence in the header case
    else:
        #it is sequence
        seqs[name] = seqs[name] + line #for more than one line of sequence
#print(seqs)
dict_GC_content = {}
for key,value in seqs.items():
  #print(key,value)
  count = value.count("G") + value.count("C")
  percentage = ((count/ len(value))*100)
  percentage = (round(percentage,6)) # Rounding-off the value to the precision asked
  dict_GC_content[key] = percentage
for key,value in dict_GC_content.items():
  if value ==  max(dict_GC_content.values()):
    print(key)
    print(value)


#or
'''
import io
Header = ""
Dict = dict()
GC = dict()
infile = io.StringIO(FASTA)
for i,j in enumerate (infile):
  j=j.strip()
  if j[0]== ">":
    Header = j[1:14]
    Dict[Header] = ""
  else:
    Dict[Header] = Dict[Header]+ j
#print(Dict)

for key,value in Dict.items():
  GC[key]= ((value.count("G")+value.count("C"))/len(value))*100
print(GC)
  
for key,value in GC.items():
  if value == max(GC.values()):
    print(key)
    print(round(value,6))
'''


