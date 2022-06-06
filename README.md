# READ_ME

## Description

Series of scripts that converters outputs from different programs (BLAST, exonerate, and CD-HIT) to GTF format. Each subdirectory is here is its own subproject. See their `README` files for more details.

## Types of input that can be converted to GTF

### BLAST output format 6

Converts BLAST output format 6 (`outfmt6`) to GTF. Read formatting details [here](https://www.metagenomics.wiki/tools/blast/blastn-output-format-6).

### exonerate

See exonerate's homepage [here](https://www.ebi.ac.uk/about/vertebrate-genomics/software/exonerate).

### CD-HIT

CD-HIT is available from [here](https://github.com/weizhongli/cdhit).


# Contents
___
## **Blast**
Script and samples for the running of gtf-convert on blast output.
## **CD-HIT**  
Script and samples for the running of gtf-convert on CD-HIT output.  
## **Exonerate**  
Script and samples for the running of gtf-convert on exonerate output.

___
`runGTFConvert.py`  - Operate to run gtf-convert on files in the target directory.

### Example Usage:  
-d : Top Level Directory
```
python .\runGTFConvert.py -d .\transcripts
```
