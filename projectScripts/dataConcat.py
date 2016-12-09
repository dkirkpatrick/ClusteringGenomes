import csv
conditions =  ['C0__TSK_0.0', 'C1__TSK_1.0', 'C3__TSK_10']
replicates = range(101,116)

for cond in conditions: 
	for iter in replicates: 
		for generation in range(0, 1000, 100): 
			firstCSVString = 'clusterData/' + cond +'_' + str(iter) + '_' + 'clusterData_' + str(generation) + '.csv' 
			secondCSVString = 'clusterData/' + cond + '_' + str(iter) + '_' + 'clusterData_' + str(generation+100) + '.csv' 
			combindedOFString = 'combinedData/' + cond + '_' + str(iter) + '_' + 'clusterData_' + str(generation) + '+' + str(generation+100) + '.csv' 
			with open(firstCSVString, newline='') as firstCSVfile, open(secondCSVString, newline='') as secondCSVfile, open(combindedOFString, 'w', newline='') as combinedfile:
					firstCSVReader = csv.reader(firstCSVfile, delimiter=',')
					secondCSVReader = csv.reader(secondCSVfile, delimiter=',')
					combinedWriter = csv.writer(combinedfile, delimiter=',')
					
					header = next(firstCSVReader)
					next(secondCSVReader)
					
					combinedWriter.writerow(header)
					
					for row in firstCSVReader: 
						combinedWriter.writerow(row)
					
					for row in secondCSVReader:  	
						combinedWriter.writerow(row)
			firstCSVfile.close()
			secondCSVfile.close()
			combinedfile.close()
