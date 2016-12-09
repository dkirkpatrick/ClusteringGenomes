"""
This script will generate the following file:
cluster_phylo_data
    * cluster_id, time, back_cluster_id
        - cluster_id: id of this cluster
        - back_cluster_id: id of back cluster
        - time: time that this cluster exists at
"""

import os, math, sys, csv

def getPhylogeny(backName, transitionName, currentName, update):
	cluster_info = ""
	#############
	# Get all relevant cluster assignment information.
	#############
	# Open back
	back_cids = None
	with open(backName, "r") as fp:
		back_cids = fp.read().strip("\n").split(",")
	# Open transition
	trans_cids = None
	with open(transitionName, "r") as fp:
		trans_cids = fp.read().strip("\n").split(",")
	# Partition transition
	back_co_cids = trans_cids[:200]
	cur_co_cids = trans_cids[-1 * 200:]
	# Open current
	cur_cids = None
	with open(currentName, "r") as fp:
		cur_cids = fp.read().strip("\n").split(",")
	#############
	# For each co cluster:
	#   * determine back-cluster makeup
	#   * determine cur-cluster makeup
	# For each cur cluster:
	#   * determine co-cluster makeup
	#   * pick majority co-cluster's majority back-cluster
	coclusters = {}
	curclusters = {}
	for i in range(0, len(back_co_cids)):
		back_cid = back_cids[i]
		co_cid = back_co_cids[i]
		if not co_cid in coclusters:
			coclusters[co_cid] = {"back":{}, "cur":{}}
		if not back_cid in coclusters[co_cid]["back"]:
			coclusters[co_cid]["back"][back_cid] = 0
		coclusters[co_cid]["back"][back_cid] += 1
	for i in range(0, len(cur_co_cids)):
		cur_cid = cur_cids[i]
		co_cid = cur_co_cids[i]
		if not co_cid in coclusters:
			coclusters[co_cid] = {"back":{}, "cur":{}}
		if not cur_cid in coclusters[co_cid]["cur"]:
			coclusters[co_cid]["cur"][cur_cid] = 0
		coclusters[co_cid]["cur"][cur_cid] += 1
		# add co-cluster vote to cur cluster
		if not cur_cid in curclusters:
			curclusters[cur_cid] = {"coclusters":{}}
		if not co_cid in curclusters[cur_cid]["coclusters"]:
			curclusters[cur_cid]["coclusters"][co_cid] = 0
		curclusters[cur_cid]["coclusters"][co_cid] += 1
	
	# For each co-cluster, pick a back cluster rep.
	for co_cid in coclusters:
		backs = coclusters[co_cid]["back"]
		if len(backs) == 0:
			mback = "NONE"
		else:
			mback = max(backs, key=backs.get)
		if mback == "-1": mback = "NONE"
		coclusters[co_cid]["back-rep"] = mback
	# For each cur cluster, determine which co-cluster the majority of these orgs get assigned to
	for cur_cid in curclusters:
		cos = curclusters[cur_cid]["coclusters"]
		mcos = max(cos, key=cos.get)
		curclusters[cur_cid]["co-rep"] = mcos
	# For each cur cluster, pick a back cluster
	for cur_cid in curclusters:
		curclusters[cur_cid]["back-cluster"] = coclusters[curclusters[cur_cid]["co-rep"]]["back-rep"]
	
	print("Coclusters:")
	for cid in coclusters:
		print("%s: %s" % (cid, str(coclusters[cid])))
	print("Cur clusters:")
	for cid in curclusters:
		print("%s: %s" % (cid, str(curclusters[cid])))
	
	# Append info to cluster info file
	time = update
	update_step = 100
	for cid in curclusters:
		cluster_id = "%s_%s" % (str(time+update_step), str(cid))
		back_cluster_id = "%s_%s" % (str(time), str(curclusters[cid]["back-cluster"]))
		line = "%s,%s,%s\n" % (str(time+update_step), cluster_id, back_cluster_id)
		cluster_info += line
	return cluster_info


if __name__ == "__main__":
	conditions =  ['C0__TSK_0.0', 'C1__TSK_1.0', 'C3__TSK_10']
	cluster_types = ['dbscan', 'spectral']
	variants = []
	replicates = range(101,116)
	count = 0
	for type in cluster_types: 
		if type[0] == 'd': 
			variants = ['_1_1_5_0.35.csv', '_1_0_5_0.60.csv' , '_0_1_5_0.15.csv']
		elif type[0] == 's': 
			variants = ['_1_1_3_0.5.csv', '_1_0_3_0.5.csv', '_0_1_3_0.5.csv']
		for var in variants: 
			for cond in conditions:
				for iter in replicates:
					cluster_inf = ""
					for generation in range(0, 1000, 100):
						previousGenerationFile = type + '/' + cond + '_' + str(iter) + '_' + str(generation) + var
						combinedGenerationFile = type + '/' + cond + '_' + str(iter) + '_' + str(generation) + '+' + str(generation+100) + var
						currentGenerationFile = type + '/' + cond + '_' + str(iter) + '_' + str(generation+100) + var
						cluster_inf += getPhylogeny(previousGenerationFile, combinedGenerationFile, currentGenerationFile, generation)
					outFile = type + '/Phylogeny/' + cond + '_' + str(iter) + '_' + var
					with open(outFile, "w") as fp:
						fp.write(cluster_inf)