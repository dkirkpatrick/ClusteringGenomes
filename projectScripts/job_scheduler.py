from subprocess import call
import sys

conditions =  ['C0__TSK_0.0', 'C1__TSK_1.0', 'C3__TSK_10']
replicates = range(101,116)

#mode = 'analyze'
mode = 'cluster'

min_pts = '5'
epsilon = '0.5'

genoVal = '1'
phenoVal = '1'

count = 0
for cond in conditions: 
	for iter in replicates: 
		for generation in range(0, 1100, 100): 
			combindedIFString = 'clusterData/' + cond + '_' + str(iter) + '_' + 'clusterData_' + str(generation) + '.csv'
			combindedOFString1 = mode + '/' + cond + '_' + str(iter) + '_' + str(generation) + '_1_1_' + min_pts + '_0.35.csv'
			combindedOFString2 = mode + '/' + cond + '_' + str(iter) + '_' + str(generation) + '_1_0_' + min_pts + '_0.60.csv'
			combindedOFString3 = mode + '/' + cond + '_' + str(iter) + '_' + str(generation) + '_0_1_' + min_pts + '_0.15.csv'
			print("./clusteringTool " + cond + " " + str(iter) + " " + str(generation) + " " + str(count))
			count += 1
			call(["qsub", "-v", "MODE="+mode+",MIN_PTS="+min_pts+",EPSILON="+epsilon+",INPUT_FILE="+combindedIFString+",OUTPUT_FILE1="+combindedOFString1+",OUTPUT_FILE2="+combindedOFString2+",OUTPUT_FILE3="+combindedOFString3, "./job.sub"]) 

for cond in conditions: 
	for iter in replicates: 
		for generation in range(0, 1000, 100): 
			combindedIFString = 'combinedData/' + cond + '_' + str(iter) + '_' + 'clusterData_' + str(generation) + '+' + str(generation+100) + '.csv' 
			combindedOFString1 = mode + '/' + cond + '_' + str(iter) + '_' + str(generation) + '+' + str(generation+100) + '_1_1_' + min_pts + '_0.35.csv'
			combindedOFString2 = mode + '/' + cond + '_' + str(iter) + '_' + str(generation) + '+' + str(generation+100) + '_1_0_' + min_pts + '_0.60.csv'
			combindedOFString3 = mode + '/' + cond + '_' + str(iter) + '_' + str(generation) + '+' + str(generation+100) + '_0_1_' + min_pts + '_0.15.csv'
			print("./clusteringTool " + cond + " " + str(iter) + " " + str(generation) + '+' + str(generation+100) + " " + str(count))
			count += 1
			call(["qsub", "-v", "MODE="+mode+",MIN_PTS="+min_pts+",EPSILON="+epsilon+",INPUT_FILE="+combindedIFString+",OUTPUT_FILE1="+combindedOFString1+",OUTPUT_FILE2="+combindedOFString2+",OUTPUT_FILE3="+combindedOFString3, "./job.sub"]) 
