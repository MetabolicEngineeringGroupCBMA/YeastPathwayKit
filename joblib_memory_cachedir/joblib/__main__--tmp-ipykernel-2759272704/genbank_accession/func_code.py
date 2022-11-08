# first line: 1
@memory.cache
def genbank_accession(s:str):
    
    from Bio.Blast import NCBIWWW
    from Bio.Blast import NCBIXML

    result_handle = NCBIWWW.qblast("blastn",
                                   "nt",
                                    s,
                                    hitlist_size=10,
                                    alignments = 1,
                                    expect=1e-8)

    blast_records = NCBIXML.read(result_handle)
    
    result_handle.close()

    results = []
    length = len(s)

    for alignment in blast_records.alignments:
        
        for hsp in alignment.hsps:
            
            if hsp.identities == length: # only **perfect** matches !
                
                results.append((alignment.accession, *sorted((hsp.sbjct_start, hsp.sbjct_end))))

    return results
