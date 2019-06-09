from Bio.Alphabet import DNAAlphabet
from Bio.Seq import Seq
import itertools
from Bio.Restriction import *

from Bio.Restriction import CommOnly, AllEnzymes

vec =  "atccgga"
"atttaaat"

seqs = [Seq("".join(s)+vec, DNAAlphabet) for s in itertools.product("acgt", repeat=7)]

enz = [e for e in AllEnzymes if e.freq == 65536]

#seqs = seqs[0:1]

for seq in seqs:
    for x in range(7):
        c = seq[x:x+8]
        for e in enz:
            if e.search(c):
                print c, e




'''


bjorn@bjorn-UL30A:~/Desktop$ python tails.py
atttaaat SwaI
atttaaat SmiI
atttaaat SwaI
atttaaat SmiI
atttaaat SwaI
atttaaat SmiI
atttaaat SwaI
atttaaat SmiI
ttaattaa PacI
bjorn@bjorn-UL30A:~/Desktop$ python

'''