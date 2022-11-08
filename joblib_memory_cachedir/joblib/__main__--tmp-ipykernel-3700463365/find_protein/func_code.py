# first line: 1
@memory.cache
def find_protein(s:str):
    from Bio.Blast import NCBIWWW
    from Bio.Blast import NCBIXML

    result_handle = NCBIWWW.qblast("blastp", 
                                   "nr", 
                                    s, 
                                    hitlist_size=10,
                                    alignments=1, 
                                    expect=1e-8)

    blast_records = NCBIXML.read(result_handle)
    
    result_handle.close()
    
    alignments = []
    
    for alignment in blast_records.alignments:
        alignments.append(alignment)
        
    return alignments
