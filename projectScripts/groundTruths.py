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
			inFile1 = 'clusterData/' + cond + '_' + str(iter) + '_clusterData_' + str(generation) + '.csv'
			outFile1 = 'groundTruths/' + cond + '_' + str(iter) + '_' + str(generation) + '_groundTruths.csv'
			with open(inFile1) as datafile, open(outFile1, 'w') as combinedfile:
				combinedWriter = csv.writer(combinedfile, delimiter=',')
				dataReader = csv.reader(datafile, delimiter=',')
				next(dataReader)
				for row in dataReader: 
					foods = []
					foods.append(row[0])
					food = 0 
					for i in range(504, 539, 6): 
						count = 0; 
						for j in range(0,5): 
							if int(row[i+j]) > 0:
								count += 1
						if count > 3:
							foods.append(food)
						food+=1
					combinedWriter.writerow(foods)
				datafile.close()
				combinedfile.close()