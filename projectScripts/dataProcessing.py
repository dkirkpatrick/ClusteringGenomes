import csv
conditions =  ['C0__TSK_0.0', 'C1__TSK_1.0', 'C3__TSK_10']
replicates = range(101,116)

for cond in conditions: 
	for iter in replicates: 
		for generation in range(0, 1100, 100): 

			dataIFString = cond + '/' + str(iter) + '/' + 'snapshotData_' + str(generation) + '.csv' 
			genomeIFString = cond + '/' + str(iter) + '/' + 'snapshotGenome_' + str(generation) + '.csv' 
			combindedOFString = 'clusterData/' + cond + '_' + str(iter) + '_' + 'clusterData_' + str(generation) + '.csv' 
			with open(genomeIFString, newline='') as genomefile, open(dataIFString, newline='') as datafile, open(combindedOFString, 'w', newline='') as combinedfile:
					dataReader = csv.reader(datafile, delimiter=',')
					genomeReader = csv.reader(genomefile, delimiter=',')
					combinedWriter = csv.writer(combinedfile, delimiter=',')
					
					dataHeader = next(dataReader)
					genomeHeader = next(genomeReader)
					
					testGenomeLine = next(genomeReader)
					testDataLine = next(dataReader)
					
					myRow = []
					myHeader = []
					myRow.append(testGenomeLine[1])
					myHeader.append('id')
					
					genome = testGenomeLine[4].replace('[', '').replace(']', '').split(',')
					i = 0
					for site in genome: 
						myRow.append(site)
						myHeader.append('genome-site'+str(i))
						i+=1
					
					myRow.append(testDataLine[0])
					myHeader.append(dataHeader[0])
					myRow.append(testDataLine[2])
					myHeader.append(dataHeader[2])
					
					
					for j in range(0,6):
						myRow.append(testDataLine[4+j*2])
						myHeader.append(dataHeader[4+j*2])
						
						foodiList = testDataLine[4+j*2+1].replace('[', '').replace(']', '').split(',')
						i = 0
						for rep in foodiList: 
							myRow.append(rep)
							myHeader.append('food'+str(j)+'-rep'+str(i))
							i+=1
					
					myRow.append(testDataLine[16])
					myHeader.append(dataHeader[16])
						
					nextNodes = testDataLine[18].replace('[', '').replace(']', '').split(',')
					i = 0
					for node in nextNodes: 
						myRow.append(node)
						myHeader.append('nextCon-node'+str(i))
						i+=1
					
					nodes = testDataLine[19].replace('[', '').replace(']', '').split(',')
					i = 0
					for node in nodes: 
						myRow.append(node)
						myHeader.append('nodeCon-node'+str(i))
						i+=1

					myRow.append(testDataLine[20])
					myHeader.append(dataHeader[20])
					
					myRow.append(testDataLine[21])
					myHeader.append(dataHeader[21])
				
					myRow.append(testDataLine[22])
					myHeader.append(dataHeader[22])
					
					scores = testDataLine[23].replace('[', '').replace(']', '').split(',')
					i = 0
					for rep in scores: 
						myRow.append(node)
						myHeader.append('score-rep'+str(i))
						i+=1

					myRow.append(testDataLine[24])
					myHeader.append(dataHeader[24])

					myRow.append(testDataLine[26])
					myHeader.append(dataHeader[26])

					myRow.append(testDataLine[27].replace('[', '').replace(']', ''))
					myHeader.append('ancestor')
					
					combinedWriter.writerow(myHeader)
					combinedWriter.writerow(myRow)
					
					for dataRow in dataReader: 
						genomeRow = next(genomeReader)
						myRow = []
						myRow.append(genomeRow[1])
						
						genome = genomeRow[4].replace('[', '').replace(']', '').split(',')
						for site in genome: 
							myRow.append(site)
						
						myRow.append(dataRow[0])
						myRow.append(dataRow[2])
						
						for j in range(0,6):
							myRow.append(dataRow[4+j*2])
						
							foodiList = dataRow[4+j*2+1].replace('[', '').replace(']', '').split(',')
							for rep in foodiList: 
								myRow.append(rep)
						
						myRow.append(dataRow[16])
							
						nextNodes = dataRow[18].replace('[', '').replace(']', '').split(',')
						for node in nextNodes: 
							myRow.append(node)
						
						nodes = dataRow[19].replace('[', '').replace(']', '').split(',')
						for node in nodes: 
							myRow.append(node)

						myRow.append(dataRow[20])
						myRow.append(dataRow[21])
						myRow.append(dataRow[22])
						
						scores = dataRow[23].replace('[', '').replace(']', '').split(',')
						for rep in scores: 
							myRow.append(node)

						myRow.append(dataRow[24])
						myRow.append(dataRow[26])
						myRow.append(dataRow[27].replace('[', '').replace(']', ''))
						
						combinedWriter.writerow(myRow)
					
			genomefile.close()
			datafile.close()
			combinedfile.close()
