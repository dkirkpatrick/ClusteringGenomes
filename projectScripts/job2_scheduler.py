from subprocess import call
import sys

conditions =  ['C0__TSK_0.0', 'C1__TSK_1.0', 'C3__TSK_10']
replicates = range(101,116)

mode = 'analyze'

min_pts = '3'
epsilon = '0.5'

genoVal = '1'
phenoVal = '1'

outPrefix = 'spectral/'
inPrefix = 'analyze/'

count = 0
for cond in conditions:
	for iter in replicates:
		for generation in range(0, 1100, 100):
			combindedOFString1 = cond + '_' + str(iter) + '_' + str(generation) + '_1_1_' + min_pts + '_0.5.csv'
			combindedOFString2 = cond + '_' + str(iter) + '_' + str(generation) + '_1_0_' + min_pts + '_0.5.csv'
			combindedOFString3 = cond + '_' + str(iter) + '_' + str(generation) + '_0_1_' + min_pts + '_0.5.csv'
			print("python spectralClustering.py " + cond + " " + str(iter) + " " + str(generation) + " " + str(count))
			count += 1
			call(["qsub", "-v", "OUTPUT_PREFIX="+outPrefix+",INPUT_PREFIX="+inPrefix+",FILE1="+combindedOFString1+",FILE2="+combindedOFString2+",FILE3="+combindedOFString3, "./job2.sub"])

for cond in conditions:
	for iter in replicates:
		for generation in range(0, 1000, 100):
			combindedOFString1 = cond + '_' + str(iter) + '_' + str(generation) + '+' + str(generation+100) + '_1_1_' + min_pts + '_0.5.csv'
			combindedOFString2 = cond + '_' + str(iter) + '_' + str(generation) + '+' + str(generation+100) + '_1_0_' + min_pts + '_0.5.csv'
			combindedOFString3 = cond + '_' + str(iter) + '_' + str(generation) + '+' + str(generation+100) + '_0_1_' + min_pts + '_0.5.csv'
			print("python spectralClustering.py " + cond + " " + str(iter) + " " + str(generation) + '+' + str(generation+100) + " " + str(count))
			count += 1
			call(["qsub", "-v", "OUTPUT_PREFIX="+outPrefix+",INPUT_PREFIX="+inPrefix+",FILE1="+combindedOFString1+",FILE2="+combindedOFString2+",FILE3="+combindedOFString3, "./job2.sub"])