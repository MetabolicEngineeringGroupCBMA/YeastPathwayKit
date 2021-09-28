# Yeast pathway kit promoter and terminator vectors

This repository contain [pYPKa](sequences/pYPKa.gb) plasmids with a
total of 65 promoters and 66 terminators (2021-09-28)
in a total of 65 + 66 = 131 vectors.

Promoters and terminator are DNA fragments representing intergenic sequences from _S. cerevisiae_ tandemly
expressed genes, so the same DNA fragment can function as both a promoter and a terminator.

Fragments to be used as promoters were cloned in the [ZraI](http://rebase.neb.com/rebase/enz/ZraI.html) restriction site
while fragments to be used as terminators were cloned in [EcoRV](http://rebase.neb.com/rebase/enz/EcoRV.html).

![pYPKa_ZE](docs/figure_pYPKa_ZE.png)

Plasmids with an insert in ZraI are named **pYPKa_Z_*.gb** and plasmids with an insert in EcoRV are named  **pYPKa_E_*.gb**.

The sequences were assembled programmatically using [pydna](https://bmcbioinformatics.biomedcentral.com/articles/10.1186/s12859-015-0544-x).

The <plasmid_script.py> assembles plasmids using data in

- [promoter_list_001.csv](sequences/promoter_list_001.csv)
- [promoter_list_002.csv](sequences/promoter_list_002.csv)