# exonerate-convert

## Contents

- `exonerate-convert.py`: conversion script  
- `exonerate_Sp_1.gff2`: example input (GFF2 file plus notes from exonerate)
- `exonerate_Sp_1.gtf`: example output

## Example usage

```bash
python3 exonerate-convert.py -i exonerate_Sp_1.gff2 -o exonerate_Sp_1.gtf
```

## Output:

``` bash
ctg4990_len=59915	exonerate:est2genome	cDNA_match	58928	59261	.	+	.	ID=exonerate.align.1;Target=GAUT01000780.1   
ctg859_len=453101	exonerate:est2genome	cDNA_match	329648	329747	.	-	.	ID=exonerate.align.2;Target=GAUT01000956.1  
ctg859_len=453101	exonerate:est2genome	cDNA_match	327191	327319	.	-	.	ID=exonerate.align.3;Target=GAUT01000956.1
ctg859_len=453101	exonerate:est2genome	cDNA_match	326926	327045	.	-	.	ID=exonerate.align.4;Target=GAUT01000956.1
ctg977_len=886491	exonerate:est2genome	cDNA_match	82580	82933	.	+	.	ID=exonerate.align.5;Target=GAUT01000850.1
ctg970_len=305932	exonerate:est2genome	cDNA_match	94516	95036	.	+	.	ID=exonerate.align.6;Target=GAUT01000878.1
ctg967_len=303867	exonerate:est2genome	cDNA_match	283921	284508	.	+	.	ID=exonerate.align.7;Target=GAUT01000376.1
ctg942_len=200313	exonerate:est2genome	cDNA_match	122250	122665	.	-	.	ID=exonerate.align.8;Target=GAUT01000822.1
ctg934_len=325016	exonerate:est2genome	cDNA_match	268096	268404	.	+	.	ID=exonerate.align.9;Target=GAUT01000096.1
```