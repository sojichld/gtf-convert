## Contents:  
- cdhit-convert.py - conversion script  
- transcripts_id090_k05.fa.clstr - example cluster file  
- transcripts_id090_k05.fa.clstr_converted.gtf - example output  
___
# cdhit-convert 
The ClusterFile contains cluster and count attributes that contain a dictionary of cluster entries for each cluster,and the total count of the file.

read() - Reads found clusters and total number of clusters from a .clstr file and stores cluster hits as a ClusterFile instance.This method creates an instance of the file. 

showResults() - Prints contents of the ClusterFile instance.  Takes a parameter for the desired amount of clusters to be printed.

convertToGTF() - Prints contents of the ClusterFile instance out to a new GTF file.

Operation:
When executed the object representation and the first 10 clusters are printed out to the command line.

The GTF file produced contains attributes for the Transcript ID, Cluster and optionally the gene type (2D files).

Usage:

[0]: Name of the script.  
[i]: file path   
[t]: file type  

File type: 

1 = 1D for standard files
2 = 2D for 2D files

cdhit_convert.py <clstr file> <file type>


Example:

`python cdhit-convert.py -i .\transcripts_id090_k05.fa.clstr -t 1`


Sample Output:  
`20220121_Cuke	CD-HIT	CDS	0	1942	0.96	.	.	transcript_id 3628; cluster Cluster 7;  `

`20220123_Cuke	CD-HIT	CDS	1943	3964	1.0	.	.	transcript_id 3629; cluster Cluster 7; ` 

` 20220121_Cuke	CD-HIT	CDS	3965	5321	0.99	.	.	transcript_id 8314; cluster Cluster 33; `  

` 20220121_Cuke	CD-HIT	CDS	5322	6690	1.0	.	.	transcript_id 8315; cluster Cluster 33;  `

` 20220121_Cuke	CD-HIT	CDS	6691	7639	0.95	.	.	transcript_id 17220; cluster Cluster 84; ` 

` 20220121_Cuke	CD-HIT	CDS	7640	8743	1.0	.	.	transcript_id 17221; cluster Cluster 84; ` 

` 20220121_Cuke	CD-HIT	CDS	8744	9847	1.0	.	.	transcript_id 17222; cluster Cluster 84; ` 

` 20220121_Cuke	CD-HIT	CDS	9848	10941	1.0	.	.	transcript_id 27812; cluster Cluster 89; ` 