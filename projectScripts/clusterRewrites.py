import sys, csv 

conditions =  ['C0__TSK_0.0', 'C1__TSK_1.0', 'C3__TSK_10']
replicates = range(101,116)


min_pts = '5'
epsilon = '0.5'

inPrefix = 'cluster'
outPrefix = 'dbscan'

count = 0
for cond in conditions:
	for iter in replicates:
		for generation in range(0, 1100, 100):
			inFile1 = inPrefix + '/' + cond + '_' + str(iter) + '_' + str(generation) + '_1_1_' + min_pts + '_0.35.csv'
			outFile1 = outPrefix + '/' + cond + '_' + str(iter) + '_' + str(generation) + '_1_1_' + min_pts + '_0.35.csv'
			cluster_content = ""
			with open(inFile1) as datafile:
				dataReader = csv.reader(datafile, delimiter=',')
				for dataRow in dataReader: 
					if len(dataRow) == 2: 
						cluster_content += dataRow[1][1:] + ","
				datafile.close()
			cluster_content = cluster_content[:-1] + "\n"
			with open(outFile1, "w") as fp:
				fp.write(cluster_content)
			
			inFile2 = inPrefix + '/' + cond + '_' + str(iter) + '_' + str(generation) + '_1_0_' + min_pts + '_0.60.csv'
			outFile2 = outPrefix + '/' + cond + '_' + str(iter) + '_' + str(generation) + '_1_0_' + min_pts + '_0.60.csv'
			cluster_content = ""
			with open(inFile2) as datafile:
				dataReader = csv.reader(datafile, delimiter=',')
				for dataRow in dataReader: 
					if len(dataRow) == 2: 
						cluster_content += dataRow[1][1:] + ","
				datafile.close()
			cluster_content = cluster_content[:-1] + "\n"
			with open(outFile2, "w") as fp:
				fp.write(cluster_content)
			
			inFile3 = inPrefix + '/' + cond + '_' + str(iter) + '_' + str(generation) + '_0_1_' + min_pts + '_0.15.csv'
			outFile3 = outPrefix + '/' + cond + '_' + str(iter) + '_' + str(generation) + '_0_1_' + min_pts + '_0.15.csv'
			cluster_content = ""
			with open(inFile3) as datafile:
				dataReader = csv.reader(datafile, delimiter=',')
				for dataRow in dataReader: 
					if len(dataRow) == 2: 
						cluster_content += dataRow[1][1:] + ","
				datafile.close()
			cluster_content = cluster_content[:-1] + "\n"
			with open(outFile3, "w") as fp:
				fp.write(cluster_content)

for cond in conditions:
	for iter in replicates:
		for generation in range(0, 1000, 100):
			inFile1 = inPrefix + '/' + cond + '_' + str(iter) + '_' + str(generation) + '+' + str(generation+100) + '_1_1_' + min_pts + '_0.35.csv'
			outFile1 = outPrefix + '/' + cond + '_' + str(iter) + '_' + str(generation) + '+' + str(generation+100) + '_1_1_' + min_pts + '_0.35.csv'
			cluster_content = ""
			with open(inFile1) as datafile:
				dataReader = csv.reader(datafile, delimiter=',')
				for dataRow in dataReader: 
					if len(dataRow) == 2: 
						cluster_content += dataRow[1][1:] + ","
				datafile.close()
			cluster_content = cluster_content[:-1] + "\n"
			with open(outFile1, "w") as fp:
				fp.write(cluster_content)
			
			inFile2 = inPrefix + '/' + cond + '_' + str(iter) + '_' + str(generation) + '+' + str(generation+100) + '_1_0_' + min_pts + '_0.60.csv'
			outFile2 = outPrefix + '/' + cond + '_' + str(iter) + '_' + str(generation) + '+' + str(generation+100) + '_1_0_' + min_pts + '_0.60.csv'
			cluster_content = ""
			with open(inFile1) as datafile:
				dataReader = csv.reader(datafile, delimiter=',')
				for dataRow in dataReader: 
					if len(dataRow) == 2: 
						cluster_content += dataRow[1][1:] + ","
				datafile.close()
			cluster_content = cluster_content[:-1] + "\n"
			with open(outFile2, "w") as fp:
				fp.write(cluster_content)
			
			inFile3 = inPrefix + '/' + cond + '_' + str(iter) + '_' + str(generation) + '+' + str(generation+100) + '_0_1_' + min_pts + '_0.15.csv'
			outFile3 = outPrefix + '/' + cond + '_' + str(iter) + '_' + str(generation) + '+' + str(generation+100) + '_0_1_' + min_pts + '_0.15.csv'
			cluster_content = ""
			with open(inFile1) as datafile:
				dataReader = csv.reader(datafile, delimiter=',')
				for dataRow in dataReader: 
					if len(dataRow) == 2: 
						cluster_content += dataRow[1][1:] + ","
				datafile.close()
			cluster_content = cluster_content[:-1] + "\n"
			with open(outFile3, "w") as fp:
				fp.write(cluster_content)
