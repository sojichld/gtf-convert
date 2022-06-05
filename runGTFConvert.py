#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Name: runGTFConvert.py
# Description: Converts all files in a directory into GTF format. 

##
# MODULES
##
import argparse, glob, sys, re, os


def main(args):
    #Top level directory
    DIR = args.directory
    #Find files in subdirectories with '.xlsx', '.outfmt6', '.tsv', .'csv', '.clstr'
    #Blast
    csv, tsv, xlsx, fmt6= glob.glob(f'{DIR}\**\*blast?.csv', recursive=True), glob.glob(f'{DIR}\**\*blast?.tsv', recursive=True), glob.glob(f'{DIR}\**\*blast?.xlsx', recursive=True), glob.glob(f'{DIR}\**\*.outfmt6', recursive=True)
    #CD-HIT
    clstr = glob.glob(f'{DIR}\**\*.clstr', recursive=True)
    #Exonerate
    gff2, out = glob.glob(f'{DIR}\**\*.gff2', recursive=True), glob.glob(f'{DIR}\**\*.out', recursive=True)

    #scripts
    blast, exonerate, cdhit = '.\Blast\\blast-convert.py','.\Exonerate\exonerate-convert.py', '.\CD-HIT\cdhit-convert.py'
    #Run appropriate script for each file type
    #Blast
    if csv:
        for i in csv:
                os.system('python {} -i {} -t csv'.format(blast, i))
    if tsv:
        for i in tsv:
                os.system('python {} -i {} -t tsv'.format(blast, i))
    if xlsx:
        for i in xlsx:
                os.system('python {} -i {} -t xlsx'.format(blast, i))
    if fmt6:
        for i in fmt6:
                os.system('python {} -i {} -t tsv'.format(blast, i))
    #CD-HIT
    if clstr:
        for i in clstr:
            if 'cd-hit-2d' in i:
                    os.system('python {} -i {} -t 2'.format(cdhit, i))
            else:
                    os.system('python {} -i {} -t 1'.format(cdhit, i))
    #Exonerate
    if gff2:
        for i in gff2:
                os.system('python {} -i {} -o {}.gtf'.format(exonerate, i, os.path.splitext(i)[0]))
    if out:
        for i in out:
                os.system('python {} -i {} -o {}.gtf'.format(exonerate, i, os.path.splitext(i)[0]))

if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument("-d", "--directory", help = "Top level directory", type=str, required=True)
    args = parser.parse_args()
    main(args)


exit()