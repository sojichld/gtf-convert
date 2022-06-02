#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Name: cdhit-convert.pdf
# Description: Reads a cluster (.clstr file) from CD-Hit and re-writes it as a GTF file.

##
# MODULES
##

import sys, re, argparse
from tkinter       import scrolledtext
from tracemalloc   import start
from typing        import List, Dict 
from xmlrpc.client import Boolean
from itertools     import islice

class ClusterFile:
	def __init__(self, clusters: Dict[str, List[str]], count: int) -> None:
		self.clusters = clusters
		self.count    = count

	def __str__(self) -> str:
		return 'A cluster file containing {} clusters.'.format(self.count)

	def __repr__(self) -> str:
		'''Returns representation of cluster obj.''' 
		preview = list(islice(self.clusters.items(), 2))
		return "ClusterFile('{}', '{}', '{}')".format(preview, self.count, self.attributes)

	def read(clstr_file: str) -> any: 
		'''Reads clusters and number of clusters from .clstr file. Returns ClusterFile object.'''
		clusters: Dict[str , List[str]] = {}
		CLUSTR = open(clstr_file, 'r', encoding="utf8")
		reads: List[str] = []
		tag: str = ''
		isCluster: Boolean = False
		for line in CLUSTR:
			if line[0] == '>':
				if isCluster == True and tag not in clusters:
					# Retrieve every other string value in the reads. --> Reads[[] [x] [] [x]]
					clusters[tag] = reads[1::2]
				tag = line.strip()
				tag = tag.replace('>', '')
				reads = []
				isCluster = False
			else:
				reads += line.strip().split('\t')
				#print(reads)
				# Mark as a cluster if there is at least one identity entry in the cluster.
				for r in reads:
					if '%' in r:
						isCluster = True
		CLUSTR.close()
		numClusters = len(clusters)
		print(f'{numClusters} clusters retrieved.')
		newCluster = ClusterFile(clusters, numClusters)
		return newCluster

	def convertToGTF(self, source: str, feature: str, strand: str, frame: str):
		'''Writes ClusterFile objects as GTF files.'''
		name = args.input
		with open(f'converted_{name}', 'w') as f:
			start: int = 0
			for i in self.clusters.items():
				cluster = i[0]
				for j in i[1]: 
					end = int(re.search('^(\d+)aa', j).group(1))
					#end = start + seqLength
					if '*' in j:
						score: float = 1.0
					else:
						score: float = float(re.search('(\d+(\.\d+)?)%', j).group(1)) / 100
						score = round(score, 2)
					seq_id = 'seq_#' + re.search('_(\d+).', j).group(1).strip()
					if args.type == 1:
						attr: str = 'cluster="{}";'.format(cluster)
						f.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format(seq_iq, source, feature, start, end, score, strand, frame, attr))
					else:
						gene_biotype = re.search('>(.*)_', j).group(1)
						attr: str = 'cluster="{}"; gene_biotype="{}";'.format(cluster, gene_biotype)
						f.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format(seq_iq, source, feature, start, end, score, strand, frame, attr))
					#start = end + 1
			f.close()
		return

	def showResults(self, rmax: int) -> None:
		'''print n results to console'''
		j = 0
		n = 1
		print(f'Clusters Retrieved: First {rmax}.')
		for i in self.clusters.items():
			if j >= rmax:
				break
			else:
				print(f'[{n}] {i}')
				j += 1
				n += 1
		return

def main(args):
	clstr_file = args.input
	source, feature, strand, frame = 'CD-HIT', 'CDS', '.', '.'
	newFile = ClusterFile.read(clstr_file)
	newFile.showResults(10)
	newFile.convertToGTF(source, feature, strand, frame)

##
# INITIALIZATION
##

if __name__ == '__main__':
    	# The arguments are defined in the next few lines
	parser=argparse.ArgumentParser()
	parser.add_argument("-i", "--input", help = "A cluster file (.clstr) from CD-HIT", type = str)
	parser.add_argument("-t", "--type", help = "Either 1 for 1D or 2 for 2D (default = 1)", type = int, required = False, choices=[1, 2], default=1)
	args = parser.parse_args()
	main(args) # This will call the main fuction

exit() # Quit this script