"""
Given directory of distance matrices:
	* load matrix
	* interpret distances and transform matrix
	* cluster transformed matrix
	* output clusters
"""

import os, math, sys, csv
from sklearn.cluster import DBSCAN, SpectralClustering

NCLUSTERS = 6
infile = ''
outfile = ''
# Sys arg: mode, algorithm, [epsilon], [minpts], [nclusters]
try:
	print(sys.argv)
	infile = str(sys.argv[1])
	outfile = str(sys.argv[2])
except:
	print("Could not load parameters")
	exit(-1)

print("Alg: spectral, Nclusters: "+ str(NCLUSTERS))
# Load matrix.
affin_mat = []
with open(infile) as datafile:
	dataReader = csv.reader(datafile, delimiter=',')
	for dataRow in dataReader: 
		myRow = []
		for item in dataRow[1:]:
			value = 1.0 - float(item)
			if value > 1: 
				value = 1.0;
			if value < 0: 
				value = 0.0; 
			myRow.append(value)
		affin_mat.append(myRow)
	datafile.close()

print("  Clustering...")
db = SpectralClustering(n_clusters = NCLUSTERS, affinity = 'precomputed').fit(affin_mat)
# clusters = {}
cluster_content = ""
for i in range(0, len(db.labels_)):
	cluster_content += "%d," % db.labels_[i]
# print clusters
cluster_content = cluster_content[:-1] + "\n"
with open(outfile, "w") as fp:
	fp.write(cluster_content)