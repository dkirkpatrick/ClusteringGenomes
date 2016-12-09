import sys, csv 
	
conditions =  ['C0__TSK_0.0', 'C1__TSK_1.0', 'C3__TSK_10']
replicates = range(101,116)
count = 0
with open('gtSingleGenAccuracy.csv', 'w') as writeFile:
	csvWriter = csv.writer(writeFile, delimiter=',')
	header = ['Condition', 'Iteration', 'Generation', 'Method', 'Cluster_Params', 'Accuracy'] 
	csvWriter.writerow(header) 
	for cond in conditions:
		for iter in replicates:
			for generation in range(0, 1100, 100):
				accuracyOutputFile1 = 'spectral/Accuracy/' + cond + '_' + str(iter) + '_' + str(generation) + '_1_1_3_0.5.csv'
				row = []
				row.append(cond)
				row.append(str(iter))
				row.append(str(generation))
				row.append('spectral')
				row.append('1_1_6')
				with open(accuracyOutputFile1) as accFile:
					accreader = csv.reader(accFile, delimiter=',')
					data = next(accreader)
					row.append(data[2])
				csvWriter.writerow(row) 
				
				accuracyOutputFile2 = 'spectral/Accuracy/' + cond + '_' + str(iter) + '_' + str(generation) + '_1_0_3_0.5.csv'
				row = []
				row.append(cond)
				row.append(str(iter))
				row.append(str(generation))
				row.append('spectral')
				row.append('1_0_6')
				with open(accuracyOutputFile2) as accFile:
					accreader = csv.reader(accFile, delimiter=',')
					data = next(accreader)
					row.append(data[2])
				csvWriter.writerow(row) 
				
				accuracyOutputFile3 = 'spectral/Accuracy/' + cond + '_' + str(iter) + '_' + str(generation) + '_0_1_3_0.5.csv'
				row = []
				row.append(cond)
				row.append(str(iter))
				row.append(str(generation))
				row.append('spectral')
				row.append('0_1_6')
				with open(accuracyOutputFile3) as accFile:
					accreader = csv.reader(accFile, delimiter=',')
					data = next(accreader)
					row.append(data[2])
				csvWriter.writerow(row) 
				
				accuracyOutputFile4 = 'dbscan/Accuracy/' + cond + '_' + str(iter) + '_' + str(generation) + '_1_1_5_0.35.csv'
				row = []
				row.append(cond)
				row.append(str(iter))
				row.append(str(generation))
				row.append('dbscan')
				row.append('1_1_5_0.35')
				with open(accuracyOutputFile4) as accFile:
					accreader = csv.reader(accFile, delimiter=',')
					data = next(accreader)
					row.append(data[2])
				csvWriter.writerow(row) 
				
				accuracyOutputFile5 = 'dbscan/Accuracy/' + cond + '_' + str(iter) + '_' + str(generation) + '_1_0_5_0.60.csv'
				row = []
				row.append(cond)
				row.append(str(iter))
				row.append(str(generation))
				row.append('dbscan')
				row.append('1_0_5_0.60')
				with open(accuracyOutputFile5) as accFile:
					accreader = csv.reader(accFile, delimiter=',')
					data = next(accreader)
					row.append(data[2])
				csvWriter.writerow(row)
				
				accuracyOutputFile6 = 'dbscan/Accuracy/' + cond + '_' + str(iter) + '_' + str(generation) + '_0_1_5_0.15.csv'
				row = []
				row.append(cond)
				row.append(str(iter))
				row.append(str(generation))
				row.append('dbscan')
				row.append('0_1_5_0.15')
				with open(accuracyOutputFile6) as accFile:
					accreader = csv.reader(accFile, delimiter=',')
					data = next(accreader)
					row.append(data[2])
				csvWriter.writerow(row)
writeFile.close()

with open('gtDualGenAccuracy.csv', 'w') as writeFile:	
	csvWriter = csv.writer(writeFile, delimiter=',')
	header = ['Condition', 'Iteration', 'Generations', 'Method', 'Cluster_Params', 'Accuracy'] 
	csvWriter.writerow(header) 
	for cond in conditions:
		for iter in replicates:
			for generation in range(0, 1000, 100):
				accuracyOutputFile1 = 'dbscan/Accuracy/' + cond + '_' + str(iter) + '_' + str(generation) + '+' + str(generation+100) + '_1_1_5_0.35.csv' 
				row = []
				row.append(cond)
				row.append(str(iter))
				row.append(str(generation)+ '+' + str(generation+100))
				row.append('dbscan')
				row.append('1_1_5_0.35')
				with open(accuracyOutputFile1) as accFile:
					accreader = csv.reader(accFile, delimiter=',')
					data = next(accreader)
					row.append(data[2])
				csvWriter.writerow(row)
				
				accuracyOutputFile2 = 'dbscan/Accuracy/' + cond + '_' + str(iter) + '_' + str(generation) + '+' + str(generation+100) + '_1_0_5_0.60.csv' 
				row = []
				row.append(cond)
				row.append(str(iter))
				row.append(str(generation)+ '+' + str(generation+100))
				row.append('dbscan')
				row.append('1_0_5_0.60')
				with open(accuracyOutputFile2) as accFile:
					accreader = csv.reader(accFile, delimiter=',')
					data = next(accreader)
					row.append(data[2])
				csvWriter.writerow(row)
				
				accuracyOutputFile3 = 'dbscan/Accuracy/' + cond + '_' + str(iter) + '_' + str(generation) + '+' + str(generation+100) + '_0_1_5_0.15.csv' 
				row = []
				row.append(cond)
				row.append(str(iter))
				row.append(str(generation)+ '+' + str(generation+100))
				row.append('dbscan')
				row.append('0_1_5_0.15')
				with open(accuracyOutputFile3) as accFile:
					accreader = csv.reader(accFile, delimiter=',')
					data = next(accreader)
					row.append(data[2])
				csvWriter.writerow(row)
				
				accuracyOutputFile4 = 'spectral/Accuracy/' + cond + '_' + str(iter) + '_' + str(generation) + '+' + str(generation+100) + '_1_1_3_0.5.csv' 
				row = []
				row.append(cond)
				row.append(str(iter))
				row.append(str(generation)+ '+' + str(generation+100))
				row.append('spectral')
				row.append('1_1_6')
				with open(accuracyOutputFile4) as accFile:
					accreader = csv.reader(accFile, delimiter=',')
					data = next(accreader)
					row.append(data[2])
				csvWriter.writerow(row) 
				
				accuracyOutputFile5 = 'spectral/Accuracy/' + cond + '_' + str(iter) + '_' + str(generation) + '+' + str(generation+100) + '_1_0_3_0.5.csv' 
				row = []
				row.append(cond)
				row.append(str(iter))
				row.append(str(generation)+ '+' + str(generation+100))
				row.append('spectral')
				row.append('1_0_6')
				with open(accuracyOutputFile5) as accFile:
					accreader = csv.reader(accFile, delimiter=',')
					data = next(accreader)
					row.append(data[2])
				csvWriter.writerow(row) 
				
				accuracyOutputFile6 = 'spectral/Accuracy/' + cond + '_' + str(iter) + '_' + str(generation) + '+' + str(generation+100) + '_0_1_3_0.5.csv'
				row = []
				row.append(cond)
				row.append(str(iter))
				row.append(str(generation)+ '+' + str(generation+100))
				row.append('spectral')
				row.append('0_1_6')
				with open(accuracyOutputFile6) as accFile:
					accreader = csv.reader(accFile, delimiter=',')
					data = next(accreader)
					row.append(data[2])
				csvWriter.writerow(row) 
writeFile.close()	