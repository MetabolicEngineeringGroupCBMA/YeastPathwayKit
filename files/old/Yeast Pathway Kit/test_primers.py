
from pydna import *
from pydna_helper.load_my_primers import primer, new_primer


p = sorted([x.seq.tostring()[6:] for x in primer if x.seq.tostring().lower().startswith("gcgcat")])

from pydna.amplify import tmbresluc as tm

for i in p:
    print tm(i), i 

print 
p = sorted([x.seq.tostring()[7:] for x in primer if x.seq.tostring().lower().startswith("taattaa")])

for i in p:
    print tm(i), i 


'''


>624_ScFBA1tpr_PacI (29-mer)
taattaaTTTGAATATGTATTACTTGGTT



>409_ScFBA1tpf (37-mer)
TTAAATAATAACAATACTGACAGTACTAAATAATTGC






'''