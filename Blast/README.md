## Contents:
- `blast-convert.py` - conversion script
- `blastn.outfmt6.tsv` - example blast file (tsv)
- `blastn.outfmt6.csv` - example blast file (csv)
- `blastn.outfmt6.xlsx` - example blast file (xslx)

- `blastn.outfmt6.tsv.gtf` - example output 
- `blastn.outfmt6.csv.gtf` - example output 
- `blastn.outfmt6.xlsx.gtf` - example output
___
# blast6-convert

## Arguments:

[0]: Name of the script.
[i]: file path
[t]: file type

File type:
xlsx = Excel File Format  
tsv = Tab Delimited File Format  
csv = Commma Delimited File Format   

## Example Usage:

```bash
python .\blast-convert.py -i blastn.outfmt6.tsv -t tsv
```


## Output:
``` Bash
O.brevi_RBPJ_SEQ1	BLAST	CDS	335	175	9.09e-80	.	.	cluster="Cluster-305980.8"; pident="100.000"; length="161"; mismatch="0"; gapopen="0"; bitscore="2", qstart="162": qend="298";  
O.brevi_RBPJ_SEQ1	BLAST	CDS	330	170	9.09e-80	.	.	cluster="Cluster-305980.7"; pident="100.000"; length="161"; mismatch="0"; gapopen="0"; bitscore="2", qstart="162": qend="298";  
O.brevi_RBPJ_SEQ1	BLAST	CDS	335	175	9.09e-80	.	.	cluster="Cluster-305980.6"; pident="100.000"; length="161"; mismatch="0"; gapopen="0"; bitscore="2", qstart="162": qend="298";  
O.brevi_RBPJ_SEQ1	BLAST	CDS	316	156	9.09e-80	.	.	cluster="Cluster-305980.5"; pident="100.000"; length="161"; mismatch="0"; gapopen="0"; bitscore="2", qstart="162": qend="298";  
O.brevi_RBPJ_SEQ1	BLAST	CDS	320	160	9.09e-80	.	.	cluster="Cluster-305980.4"; pident="100.000"; length="161"; mismatch="0"; gapopen="0"; bitscore="2", qstart="162": qend="298";  
O.brevi_RBPJ_SEQ2	BLAST	CDS	329	181	1.79e-71	.	.	cluster="Cluster-305980.8"; pident="99.329"; length="149"; mismatch="1"; gapopen="0"; bitscore="1", qstart="149": qend="270";  
O.brevi_RBPJ_SEQ2	BLAST	CDS	324	176	1.79e-71	.	.	cluster="Cluster-305980.7"; pident="99.329"; length="149"; mismatch="1"; gapopen="0"; bitscore="1", qstart="149": qend="270";  
O.brevi_RBPJ_SEQ2	BLAST	CDS	329	181	1.79e-71	.	.	cluster="Cluster-305980.6"; pident="99.329"; length="149"; mismatch="1"; gapopen="0"; bitscore="1", qstart="149": qend="270";  
O.brevi_RBPJ_SEQ2	BLAST	CDS	310	162	1.79e-71	.	.	cluster="Cluster-305980.5"; pident="99.329"; length="149"; mismatch="1"; gapopen="0"; bitscore="1", qstart="149": qend="270";
```