#!/usr/bin/env python3

import argparse
import os
import re


def main():
    parser = argparse.ArgumentParser( description='Converts exonerate GFF output to GFF3')

    # output file to be written
    parser.add_argument('-i', '--input_file', type=str, required=True, help='Path to an input file to parse' )
    parser.add_argument('-o', '--output_file', type=str, required=True, help='Path to an output file to be created' )
    
    args = parser.parse_args()

    fout = open(args.output_file, 'w')
    fout.write("##gff-version 3\n")

    next_id_num = 1
    in_gff3_region = False
    current_sequence = None

    for line in open(args.input_file, 'r'):
        if line.startswith('# --- START OF GFF DUMP ---'):
            in_gff3_region = True
    
        elif line.startswith('# --- END OF GFF DUMP ---'):
            in_gff3_region = False
            current_sequence = None
        
        if line.startswith('#'):
            continue
        
        cols = line.split("\t")

        if len(cols) != 9 or in_gff3_region == False:
            continue

        if cols[2] == 'gene':
            m = re.search( 'sequence (\S+)', cols[8] )

            if m:
                current_sequence = m.group(1)
            else:
                raise Exception("ERROR: expected to find a sequence identifier in the 9th column but didn't.")

        elif cols[2] == 'exon':
            id = "exonerate.align.{0}".format(next_id_num)
            next_id_num += 1

            cols[2] = 'cDNA_match'
            cols[8] = "ID={0};Target={1}".format(id, current_sequence)

            fout.write("\t".join(cols) + "\n")


if __name__ == '__main__':
    main()