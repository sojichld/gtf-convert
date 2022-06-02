## Contents:
- blast-convert.py - conversion script
- blastn.outfmt6.tsv - example blast file (tsv)
- blastn.outfmt6.tsv - example blast file (csv)
- blastn.outfmt6.xlsx - example blast file (xslx)
- transcripts_id090_k05.fa.clstr_converted.gtf - example output
___
# blast6-convert

Usage:

[0]: Name of the script.
[i]: file path
[t]: file type

ile type:
xlsx = Excel File Format
tsv = Tab Delimited File Format
csv = Commma Delimited File Format
example:

`python .\blast-convert.py -i blastn.outfmt6.tsv -t tsv`


Sample Output:
`20220121_Cuke	CD-HIT	CDS	0	1942	0.96	.	.	transcript_id 3628; cluster Cluster 7;O.brevi_RBPJ_SEQ1	BLAST	CDS	335	175	9.09e-80	.	.	cluster="Cluster-305980.8"; pident="100.000"; length="161"; mismatch="0"; gapopen="0"; bitscore="2", qstart="162": qend="298";O.brevi_RBPJ_SEQ1	BLAST	CDS	335	175	9.09e-80	.	.	cluster="Cluster-305980.8"; pident="100.000"; length="161"; mismatch="0"; gapopen="0"; bitscore="2", qstart="162": qend="298";  `

`O.brevi_RBPJ_SEQ1	BLAST	CDS	330	170	9.09e-80	.	.	cluster="Cluster-305980.7"; pident="100.000"; length="161"; mismatch="0"; gapopen="0"; bitscore="2", qstart="162": qend="298";20220123_Cuke	CD-HIT	CDS	1943	3964	1.0	.	.	transcript_id 3629; cluster Cluster 7;O.brevi_RBPJ_SEQ1	BLAST	CDS	330	170	9.09e-80	.	.	cluster="Cluster-305980.7"; pident="100.000"; length="161"; mismatch="0"; gapopen="0"; bitscore="2", qstart="162": qend="298"; `

` 20220121_Cuke	CD-HIT	CDS	3965	5321	0.99	.	.	transcript_id 8314; cluster Cluster 33;O.brevi_RBPJ_SEQ1	BLAST	CDS	335	175	9.09e-80	.	.	cluster="Cluster-305980.6"; pident="100.000"; length="161"; mismatch="0"; gapopen="0"; bitscore="2", qstart="162": qend="298";O.brevi_RBPJ_SEQ1	BLAST	CDS	335	175	9.09e-80	.	.	cluster="Cluster-305980.6"; pident="100.000"; length="161"; mismatch="0"; gapopen="0"; bitscore="2", qstart="162": qend="298"; `

` 20220121_Cuke	CD-HIT	CDS	5322	6690	1.0	.	.	transcript_id 8315; cluster Cluster 33;O.brevi_RBPJ_SEQ1	BLAST	CDS	316	156	9.09e-80	.	.	cluster="Cluster-305980.5"; pident="100.000"; length="161"; mismatch="0"; gapopen="0"; bitscore="2", qstart="162": qend="298";O.brevi_RBPJ_SEQ1	BLAST	CDS	316	156	9.09e-80	.	.	cluster="Cluster-305980.5"; pident="100.000"; length="161"; mismatch="0"; gapopen="0"; bitscore="2", qstart="162": qend="298";  `

` 20220121_Cuke	CD-HIT	CDS	6691	7639	0.95	.	.	transcript_id 17220; cluster Cluster 84;O.brevi_RBPJ_SEQ1	BLAST	CDS	320	160	9.09e-80	.	.	cluster="Cluster-305980.4"; pident="100.000"; length="161"; mismatch="0"; gapopen="0"; bitscore="2", qstart="162": qend="298";O.brevi_RBPJ_SEQ1	BLAST	CDS	320	160	9.09e-80	.	.	cluster="Cluster-305980.4"; pident="100.000"; length="161"; mismatch="0"; gapopen="0"; bitscore="2", qstart="162": qend="298"; `

` 20220121_Cuke	CD-HIT	CDS	7640	8743	1.0	.	.	transcript_id 17221; cluster Cluster 84;O.brevi_RBPJ_SEQ2	BLAST	CDS	329	181	1.79e-71	.	.	cluster="Cluster-305980.8"; pident="99.329"; length="149"; mismatch="1"; gapopen="0"; bitscore="1", qstart="149": qend="270";O.brevi_RBPJ_SEQ2	BLAST	CDS	329	181	1.79e-71	.	.	cluster="Cluster-305980.8"; pident="99.329"; length="149"; mismatch="1"; gapopen="0"; bitscore="1", qstart="149": qend="270"; `

` 20220121_Cuke	CD-HIT	CDS	8744	9847	1.0	.	.	transcript_id 17222; cluster Cluster 84;O.brevi_RBPJ_SEQ2	BLAST	CDS	329	181	1.79e-71	.	.	cluster="Cluster-305980.8"; pident="99.329"; length="149"; mismatch="1"; gapopen="0"; bitscore="1", qstart="149": qend="270";O.brevi_RBPJ_SEQ2	BLAST	CDS	324	176	1.79e-71	.	.	cluster="Cluster-305980.7"; pident="99.329"; length="149"; mismatch="1"; gapopen="0"; bitscore="1", qstart="149": qend="270"; `

` 20220121_Cuke	CD-HIT	CDS	9848	10941	1.0	.	.	transcript_id 27812; cluster Cluster 89;
O.brevi_RBPJ_SEQ2	BLAST	CDS	329	181	1.79e-71	.	.	cluster="Cluster-305980.6"; pident="99.329"; length="149"; mismatch="1"; gapopen="0"; bitscore="1", qstart="149": qend="270";O.brevi_RBPJ_SEQ2	BLAST	CDS	329	181	1.79e-71	.	.	cluster="Cluster-305980.6"; pident="99.329"; length="149"; mismatch="1"; gapopen="0"; bitscore="1", qstart="149": qend="270";
 `
