seq_a = input("Enter the first sequence: ")  
seq_b = input("Enter the second sequence: ")    
len_a = len(seq_a)    
len_b = len(seq_b)    
print("Length of Sequence A: " + str(len_a))    
print()    
print("Length of Sequence B: " + str(len_b))
print()

def sequence_compare(seq_a, seq_b):
        len1 = len(seq_a)
        len2 = len(seq_b)
        mismatches = []
        for pos in range (0, min(len1, len2)) :
              if seq_a[pos] != seq_b[pos]:
                  mismatches.append('|')
              else:
                  mismatches.append(' ')
        print (seq_a)
        print ("".join(mismatches))
        print (seq_b)
sequence_compare(seq_a,seq_b)
print()
print()
print()
# This program finds all the occurrences of a motif
# in a DNA sequence and reports the motifs found as a list.
# The motif, in regular expression, here consists of
# substrings of A and/or T of lengths between 3 and 6, with two groups.
import re
import sys
print("PART - 1")
DNA_sequence = seq_a + seq_b
print('DNA_sequence:', DNA_sequence)

htt_pattern = '(CAG|CAA){12,}'
match = re.findall(htt_pattern,DNA_sequence)
print("The number of PolyQ repeats found are: " + str(len(match)))

if re.search('CC(G|C)GG', DNA_sequence):
    print('Restriction enzyme found!')

N_glycosylation_pattern = 'A[^T][GT][^C]'
# putting a caret ^ at the start of the group will negate it
# and match any character that is not in that group

Protein_seq = DNA_sequence

if re.search(N_glycosylation_pattern, Protein_seq):
    print("N-glycosylation site motif found")
else:
    print("No motif found for N-glycosylation site")


motif = r'(([AT]){3,6})'
print('Motif:', motif)

# Checking if motif is a valid regular expression
try:
    re.compile(motif)
except:
    print('Invalid regular expression, exiting the program!')
    sys.exit()

matches = re.findall(motif, DNA_sequence)

if matches:
    print('List of matches:', matches)
else:
    print('Did not find any match.')
print()
print()
print()
# This program reports if a motif (ATG followed by zero or more any
# characters-non greedy-ending with TAA) is present in a DNA sequence,
# and prints the matched substring, the start and end indices.
print("PART - 2")  
motif = r'ATG.*?TAA'         # r for raw string
#motif = r'[ATG.*?TAA'       # This is an invalid regular expression
print('Motif:', motif)

# Checking if motif is a valid regular expression
try:
    re.compile(motif)
except:
    print('Invalid regular expression, exiting the program!')
    sys.exit()

match = re.search(motif, DNA_sequence)

if match:
    print('Found the motif   :', match.group())
    print('Starting at index :', match.start())
    print('Ending at index   :', match.end())
else:
    print('Did not find the motif.')
print()
print()
print()

# This program reports if a motif (ATG followed by zero or more any
# characters-non greedy-ending with TAA) is present in a DNA sequence
# and lists the groupings (two groups are the motif found and the characters
# between ATG and TAA in the found motif).
print("PART-3")
motif = r'(ATG(.*?)TAA)'
print('Motif:', motif)

# Checking if motif is a valid regular expression
try:
    re.compile(motif)
except:
    print('Invalid regular expression, exiting the program!')
    sys.exit()

match = re.search(motif, DNA_sequence)

if match:
    print('group0           :', match.group(0))
    print('group0 start-end :', match.start(0), match.end(0))
    print('group1           :', match.group(1))
    print('group1 start-end :', match.start(1), match.end(1))
    print('group2           :', match.group(2))
    print('group2 start-end :', match.start(2), match.end(2))
    print('groups as tuples :', match.groups())
else:
    print('Did not find the motif.')
print()
print()
print()

# The program herein stores a DNA sequence in uppercase letters and 
# asks the user to enter a motif in regular expression. If the motif 
# is an invalid regular expression, it asks the user to enter another  
# motif. If the regular expression is valid, it finds all matches of 
# the motif in the DNA sequence and reports the matches, including 
# groups and positions. Matches are displayed in lowercase letters.
# If no motif is entered, the program terminates.
#
print("PART-4")
while True:
    motif = input('Enter a motif to search for or enter to exit : ')
    if motif == '':
        break
    print('Motif:', motif)
    print('-'*len(DNA_sequence))
    # Checking if motif is a valid regular expression
    try:
        re.compile(motif)
    except:
        print('Invalid regular expression!')
    else:
       motif_found = False
       matches = re.finditer(motif, DNA_sequence)
       for match in matches:
           for i in range(0, len(match.groups()) + 1):
               print('group%02d %02d-%02d: %s' % (i, match.start(i), match.end(i), match.group(i)))
           DNA_sequence = DNA_sequence[0:match.start()] + match.group().lower() + DNA_sequence[match.end():]
           print('-'*len(DNA_sequence))
           motif_found = True
       if motif_found == True:
           print('Motif search is completed:')
           print(DNA_sequence)
       else:
           print('Did not find any motif match!')
    print('~'*len(DNA_sequence))
print('Terminated')
print()
print()
print()
print("PART-5 SUFFIX TREE IMPLEMENTATION")
# Python3 program for building suffix
# array of a given text

# Class to store information of a suffix
class suffix:
	
	def __init__(self):
		
		self.index = 0
		self.rank = [0, 0]

# This is the main function that takes a
# string 'txt' of size n as an argument,
# builds and return the suffix array for
# the given string
def buildSuffixArray(txt, n):
	
	# A structure to store suffixes
	# and their indexes
	suffixes = [suffix() for _ in range(n)]

	# Store suffixes and their indexes in
	# an array of structures. The structure
	# is needed to sort the suffixes alphabetically
	# and maintain their old indexes while sorting
	for i in range(n):
		suffixes[i].index = i
		suffixes[i].rank[0] = (ord(txt[i]) -
							ord("a"))
		suffixes[i].rank[1] = (ord(txt[i + 1]) -
						ord("a")) if ((i + 1) < n) else -1

	# Sort the suffixes according to the rank
	# and next rank
	suffixes = sorted(
		suffixes, key = lambda x: (
			x.rank[0], x.rank[1]))

	# At this point, all suffixes are sorted
	# according to first 2 characters. Let
	# us sort suffixes according to first 4
	# characters, then first 8 and so on
	ind = [0] * n # This array is needed to get the
				# index in suffixes[] from original
				# index.This mapping is needed to get
				# next suffix.
	k = 4
	while (k < 2 * n):
		
		# Assigning rank and index
		# values to first suffix
		rank = 0
		prev_rank = suffixes[0].rank[0]
		suffixes[0].rank[0] = rank
		ind[suffixes[0].index] = 0

		# Assigning rank to suffixes
		for i in range(1, n):
			
			# If first rank and next ranks are
			# same as that of previous suffix in
			# array, assign the same new rank to
			# this suffix
			if (suffixes[i].rank[0] == prev_rank and
				suffixes[i].rank[1] == suffixes[i - 1].rank[1]):
				prev_rank = suffixes[i].rank[0]
				suffixes[i].rank[0] = rank
				
			# Otherwise increment rank and assign
			else:
				prev_rank = suffixes[i].rank[0]
				rank += 1
				suffixes[i].rank[0] = rank
			ind[suffixes[i].index] = i

		# Assign next rank to every suffix
		for i in range(n):
			nextindex = suffixes[i].index + k // 2
			suffixes[i].rank[1] = suffixes[ind[nextindex]].rank[0] \
				if (nextindex < n) else -1

		# Sort the suffixes according to
		# first k characters
		suffixes = sorted(
			suffixes, key = lambda x: (
				x.rank[0], x.rank[1]))

		k *= 2

	# Store indexes of all sorted
	# suffixes in the suffix array
	suffixArr = [0] * n
	
	for i in range(n):
		suffixArr[i] = suffixes[i].index

	# Return the suffix array
	return suffixArr

# A utility function to print an array
# of given size
def printArr(arr, n):
	
	for i in range(n):
		print(arr[i], end = " ")
		
	print()

# Driver code
if __name__ == "__main__":
	
	txt = DNA_sequence
	n = len(txt)
	
	suffixArr = buildSuffixArray(txt, n)
	
	print("Following is suffix array for", txt)
	
	printArr(suffixArr, n)

from suffix_tree import Tree
tree = Tree()
tree = Tree({"A":DNA_sequence})
part = input("Enter the part to be found:")
print("The result is : "+str(tree.find(part)))
print("Following are the maximal repeats:")
for C,path in sorted(tree.maximal_repeats()):
        print(C,path)

from suffix_trees import STree
n = int(input("Enter the size of list : "))
parts = []

for i in range(0,n):
    number = (input())
    parts = parts + [number]

st = STree.STree(parts)
print("The common strand is: " + st.lcs())
print()
print()
print()
print("PART-6 EQUAL LENGTH OF DNA STRANDS")
from Bio import motifs
from Bio.Seq import Seq
n = int(input("Enter the size of list : "))
instances = []

for i in range(0,n):
    number = (input())
    instances = instances + [number]
m = motifs.create(instances)
print(m.counts)

print("The alphabets in the motif are: " + str(m.alphabet))
print()
#largest values in the columns
print("The consensus sequence of the motif is: " + str(m.consensus))
print()
#smallest values in the columns
print("The anti-consensus sequence of the motif is: " + str(m.anticonsensus))
print()
#Degenerate follows IUPAC nomenclature
# W is either A or T
# V is either A or C or G
print("The degenerate sequence of the motif is: " + str(m.degenerate_consensus))
print()
#Position weight matrix is basically the probability of each nucleotide along the alignment
pwm = m.counts.normalize(pseudocounts = 0.5)
print("The position weight matrix is :")
print(pwm)
print("The reverse complement position weight matrix is :")
print(pwm.reverse_complement())
#Using the background distribution and PWM , we can tell the log odds of a motif coming against the background
pssm = pwm.log_odds()
print("The position-specific mscoring matrix will be: ")
print(pssm)
DNA_upper = DNA_sequence.upper()
print(DNA_upper)
A = DNA_upper.count("A")
T = DNA_upper.count("T")
G = DNA_upper.count("G")
C = DNA_upper.count("C")

GC_count = round(((G+C/(G+C+A+T)*100)),2)
AT_count = round(((A+T/(G+C+A+T)*100)),2)
#print("The GC content of your DNA sequence is:\n{0}%".format(GC_count))

import matplotlib.pyplot as plt
x_axis = ["A","T","G","C"]
y_axis = [A,T,G,C]
plt.subplot(2,1,1)
plt.bar(x_axis,y_axis,label = "Nucleotide Frequency")

plt.subplot(2,1,2)
x2 = ["GC_content","AT_content"]
y2 = [GC_count,AT_count]
plt.bar(x2,y2,label = "GC% and AT%")

plt.legend(loc="best")
plt.show()

#This method uses the concept of calculus for central dogma.
#Segments of DNA called genes are transcribed into mRNA or messenger RNA and then strands are converted into code of amino acid which acts as a building block for proteins
#This code intends to present the breakdown rate of mRNA and protein because of which they floaat in the cytoplasm.

import matplotlib.pyplot as plt
from scipy.integrate import odeint
import numpy as np

m_init = 0
p_init = 0
tend = 200


k_m = 0.4
gamma_m = 0.1
k_p = 0.2
gamma_p = 0.05

M = [m_init]
P = [p_init]
t = [0]

delta_t = 0.5


while t[-1] < tend:

    next_M = M[-1] + (k_m - gamma_m * M[-1]) * delta_t
    M.append(next_M)

    next_P = P[-1] + (k_p * M[-1] - gamma_p * P[-1]) * delta_t
    P.append(next_P)  

    next_t = t[-1] + delta_t
    t.append(next_t)



f,ax = plt.subplots(1)

line1, = ax.plot(t,M, color="b", label="Euler M")
line2, = ax.plot(t,P, color="r", label="Euler P")

ax.set_ylabel("Abundance")
ax.set_xlabel("Time")
# ax.legend(handles=[line1,line2])
# plt.show()





y0 = [m_init,p_init]
t = np.linspace(0,tend,num=100)
params = [k_m, gamma_m,k_p,gamma_p]

def sim(variables, t, params):

    M = variables[0]
    P = variables[1]

    k_m = params[0]
    gamma_m = params[1]
    k_p = params[2]
    gamma_p = params[3]

    dMdt = k_m - gamma_m * M
    dPdt = k_p * M - gamma_p * P




    return([dMdt,dPdt])


y = odeint(sim, y0, t, args=(params,))

line3, = ax.plot(t,y[:,0], color="black", label="scipy M",linestyle="dashed")
line4, = ax.plot(t,y[:,1], color="black", label="scipy P",linestyle="dashed")

ax.legend(handles=[line1,line2,line3,line4])
plt.show()




