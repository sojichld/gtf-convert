## Contents:

- `cdhit-convert.py` - conversion script
- `example1d.clstr` - example 1D cluster file
- `example1d.clstr.gtf` - example 1D output
- `example2d.clstr` - example 2D cluster file
- `example2d.clstr.gtf` - example 2D output
___

# cdhit-convert

## Functions

The ClusterFile contains cluster and count attributes that contain a dictionary of cluster entries for each cluster,and the total count of the file.

read() - Reads found clusters and total number of clusters from a .clstr file and stores cluster hits as a ClusterFile instance.This method creates an instance of the file.

showResults() - Prints contents of the ClusterFile instance.  Takes a parameter for the desired amount of clusters to be printed.

convertToGTF() - Prints contents of the ClusterFile instance out to a new GTF file.

Operation:
When executed the object representation and the first 10 clusters are printed out to the command line.

The GTF file produced contains attributes for the Transcript ID, Cluster and optionally the gene type (2D files).

## Usage:

[0]: Name of the script.
[i]: file path
[t]: file type

File type:

1 = 1D for standard files
2 = 2D for 2D files

`cdhit_convert.py <clstr file> <file type> `


## Example usage with 1D input

```bash
python3 cdhit-convert.py -i example1d.clstr -t 1
```


### Output:

```
transcript_3628	CD-HIT	transcript	0	1942	95.83	.	.	cluster="Cluster 7"
transcript_3629	CD-HIT	transcript	0	2021	100.0	.	.	cluster="Cluster 7"
transcript_13536	CD-HIT	transcript	0	1643	100.0	.	.	cluster="Cluster 15"
transcript_13537	CD-HIT	transcript	0	1627	99.88	.	.	cluster="Cluster 15"
transcript_13538	CD-HIT	transcript	0	1610	100.0	.	.	cluster="Cluster 17"
transcript_13539	CD-HIT	transcript	0	1610	100.00	.	.	cluster="Cluster 17"
transcript_1301	CD-HIT	transcript	0	1497	100.0	.	.	cluster="Cluster 22"
transcript_1302	CD-HIT	transcript	0	1497	100.00	.	.	cluster="Cluster 22"
transcript_8311	CD-HIT	transcript	0	1417	100.0	.	.	cluster="Cluster 25"
```

## Example usage with 2D input

```bash
python3 cdhit-convert.py -i example2d.clstr -t 1
```


### Output:

```
transcript_7781	CD-HIT	transcript	0	16	50.00	.	.	cluster="Cluster 0"; Name="adam_8"
transcript_14744	CD-HIT	transcript	0	11	54.55	.	.	cluster="Cluster 6"; Name="adam_11"
```

### Note:

When using the 2D type, it is assumed that the 'Name' of the transcript will be the sequence ID of the first entry on that cluster.
