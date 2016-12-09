import sys, csv 

def getAccuracy(gtFileString, clusterFileString, outFileString1, outFileString2): 
	with open(gtFileString) as gtFile, open(clusterFileString) as clusterFile, open(outFileString1, 'w') as outFile, open(outFileString2, 'w') as outFile2:
		groundtruthreader = csv.reader(gtFile, delimiter=',')
		clusterreader = csv.reader(clusterFile, delimiter=',')
		accuracywriter = csv.writer(outFile, delimiter=',')
		assignmentwriter = csv.writer(outFile2, delimiter=',')
		
		maxCluster = -1
		clustersByAgent = []
		row = next(clusterreader)
		for item in row: 
			clustersByAgent.append(int(item))
			if int(item) > maxCluster:
				maxCluster = int(item)
		
		agentsByCluster = []
		for i in range(0, maxCluster+1):
			temp = []
			agentsByCluster.append(temp)
		
		for i in range(0, len(clustersByAgent)): 
				agentsByCluster[clustersByAgent[i]].append(i)
		
		groundTruths = []
		for row in groundtruthreader:
			truths = []
			if len(row) > 1: 
				for item in row[1:]: 
					truths.append(int(item))
			groundTruths.append(truths)
		
		clusterAssignments =  [] 
		correct = 0
		for i in range(0, maxCluster+1):
			foodCounts = [0,0,0,0,0,0]
			temp = agentsByCluster[i]
			if len(temp) > 0: 
				for agent in temp: 
					truths = groundTruths[agent]
					if len(truths) > 0: 
						for item in truths: 
							foodCounts[item]+=1
			highest = max(foodCounts)
			correct += highest
			clusterAssignments.append(foodCounts.index(highest))
		
		assignmentwriter.writerow(clusterAssignments)
		accuracyVector = [correct, len(groundTruths), (correct/len(groundTruths))] 
		accuracywriter.writerow(accuracyVector)
	gtFile.close()
	clusterFile.close() 
	outFile.close()
	outFile2.close()
		
def getAccuracy2(gtFileString1, gtFileString2, clusterFileString, outFileString1, outFileString2): 
	with open(gtFileString1) as gtFile1, open(gtFileString2) as gtFile2, open(clusterFileString) as clusterFile, open(outFileString1, 'w') as outFile, open(outFileString2, 'w') as outFile2:
		groundtruthreader = csv.reader(gtFile1, delimiter=',')
		groundtruthreader2 = csv.reader(gtFile2, delimiter=',')
		clusterreader = csv.reader(clusterFile, delimiter=',')
		accuracywriter = csv.writer(outFile, delimiter=',')
		assignmentwriter = csv.writer(outFile2, delimiter=',')
		
		maxCluster = -1
		clustersByAgent = []
		row = next(clusterreader)
		for item in row: 
			clustersByAgent.append(int(item))
			if int(item) > maxCluster:
				maxCluster = int(item)
		
		agentsByCluster = []
		for i in range(0, maxCluster+1):
			temp = []
			agentsByCluster.append(temp)
		
		for i in range(0, len(clustersByAgent)): 
				agentsByCluster[clustersByAgent[i]].append(i)
		
		groundTruths = []
		for row in groundtruthreader:
			truths = []
			if len(row) > 1: 
				for item in row[1:]: 
					truths.append(int(item))
			groundTruths.append(truths)
		
		for row in groundtruthreader2:
			truths = []
			if len(row) > 1: 
				for item in row[1:]: 
					truths.append(int(item))
			groundTruths.append(truths)
		
		clusterAssignments =  [] 
		correct = 0
		for i in range(0, maxCluster+1):
			foodCounts = [0,0,0,0,0,0]
			temp = agentsByCluster[i]
			if len(temp) > 0: 
				for agent in temp: 
					truths = groundTruths[agent]
					if len(truths) > 0: 
						for item in truths: 
							foodCounts[item]+=1
			highest = max(foodCounts)
			correct += highest
			clusterAssignments.append(foodCounts.index(highest))
		
		assignmentwriter.writerow(clusterAssignments)
		accuracyVector = [correct, len(groundTruths), (correct/len(groundTruths))] 
		accuracywriter.writerow(accuracyVector)
	gtFile1.close()
	gtFile2.close()
	clusterFile.close() 
	outFile.close()
	outFile2.close()
	
if __name__ == "__main__":
	conditions =  ['C0__TSK_0.0', 'C1__TSK_1.0', 'C3__TSK_10']
	replicates = range(101,116)
	count = 0
	for cond in conditions:
		for iter in replicates:
			for generation in range(0, 1100, 100):
				groundTruthsFile = 'groundTruths/' + cond + '_' + str(iter) + '_' + str(generation) + '_groundTruths.csv'
				
				clusterFile1 = 'spectral/' + cond + '_' + str(iter) + '_' + str(generation) + '_1_1_3_0.5.csv'
				accuracyOutputFile1 = 'spectral/Accuracy/' + cond + '_' + str(iter) + '_' + str(generation) + '_1_1_3_0.5.csv'
				assignmentsOutputFile1 = 'spectral/Assignments/' + cond + '_' + str(iter) + '_' + str(generation) + '_1_1_3_0.5.csv'
				getAccuracy(groundTruthsFile, clusterFile1, accuracyOutputFile1, assignmentsOutputFile1)
				
				clusterFile2 = 'spectral/' + cond + '_' + str(iter) + '_' + str(generation) + '_1_0_3_0.5.csv'
				accuracyOutputFile2 = 'spectral/Accuracy/' + cond + '_' + str(iter) + '_' + str(generation) + '_1_0_3_0.5.csv'
				assignmentsOutputFile2 = 'spectral/Assignments/' + cond + '_' + str(iter) + '_' + str(generation) + '_1_0_3_0.5.csv'
				getAccuracy(groundTruthsFile, clusterFile2, accuracyOutputFile2, assignmentsOutputFile2)
				
				clusterFile3 = 'spectral/' + cond + '_' + str(iter) + '_' + str(generation) + '_0_1_3_0.5.csv'
				accuracyOutputFile3 = 'spectral/Accuracy/' + cond + '_' + str(iter) + '_' + str(generation) + '_0_1_3_0.5.csv'
				assignmentsOutputFile3 = 'spectral/Assignments/' + cond + '_' + str(iter) + '_' + str(generation) + '_0_1_3_0.5.csv'
				getAccuracy(groundTruthsFile, clusterFile3, accuracyOutputFile3, assignmentsOutputFile3)
				
				clusterFile4 = 'dbscan/' + cond + '_' + str(iter) + '_' + str(generation) + '_1_1_5_0.35.csv'
				accuracyOutputFile4 = 'dbscan/Accuracy/' + cond + '_' + str(iter) + '_' + str(generation) + '_1_1_5_0.35.csv'
				assignmentsOutputFile4 = 'dbscan/Assignments/' + cond + '_' + str(iter) + '_' + str(generation) + '_1_1_5_0.35.csv'
				getAccuracy(groundTruthsFile, clusterFile4, accuracyOutputFile4, assignmentsOutputFile4)
				
				clusterFile5 = 'dbscan/' + cond + '_' + str(iter) + '_' + str(generation) + '_1_0_5_0.60.csv'
				accuracyOutputFile5 = 'dbscan/Accuracy/' + cond + '_' + str(iter) + '_' + str(generation) + '_1_0_5_0.60.csv'
				assignmentsOutputFile5 = 'dbscan/Assignments/' + cond + '_' + str(iter) + '_' + str(generation) + '_1_0_5_0.60.csv'
				getAccuracy(groundTruthsFile, clusterFile5, accuracyOutputFile5, assignmentsOutputFile5)
				
				clusterFile6 = 'dbscan/' + cond + '_' + str(iter) + '_' + str(generation) + '_0_1_5_0.15.csv'
				accuracyOutputFile6 = 'dbscan/Accuracy/' + cond + '_' + str(iter) + '_' + str(generation) + '_0_1_5_0.15.csv'
				assignmentsOutputFile6 = 'dbscan/Assignments/' + cond + '_' + str(iter) + '_' + str(generation) + '_0_1_5_0.15.csv'
				getAccuracy(groundTruthsFile, clusterFile6, accuracyOutputFile6, assignmentsOutputFile6)
				
	for cond in conditions:
		for iter in replicates:
			for generation in range(0, 1000, 100):
				groundTruthsFile = 'groundTruths/' + cond + '_' + str(iter) + '_' + str(generation) + '_groundTruths.csv'
				groundTruthsFile2 = 'groundTruths/' + cond + '_' + str(iter) + '_' + str(generation+100) + '_groundTruths.csv'
				
				clusterFile1 = 'dbscan/' + cond + '_' + str(iter) + '_' + str(generation) + '+' + str(generation+100) + '_1_1_5_0.35.csv'
				accuracyOutputFile1 = 'dbscan/Accuracy/' + cond + '_' + str(iter) + '_' + str(generation) + '+' + str(generation+100) + '_1_1_5_0.35.csv' 
				assignmentsOutputFile1 = 'dbscan/Assignments/' + cond + '_' + str(iter) + '_' + str(generation) + '+' + str(generation+100) + '_1_1_5_0.35.csv' 
				getAccuracy2(groundTruthsFile, groundTruthsFile2, clusterFile1, accuracyOutputFile1, assignmentsOutputFile1)
				
				clusterFile2 = 'dbscan/' + cond + '_' + str(iter) + '_' + str(generation) + '+' + str(generation+100) + '_1_0_5_0.60.csv'
				accuracyOutputFile2 = 'dbscan/Accuracy/' + cond + '_' + str(iter) + '_' + str(generation) + '+' + str(generation+100) + '_1_0_5_0.60.csv' 
				assignmentsOutputFile2 = 'dbscan/Assignments/' + cond + '_' + str(iter) + '_' + str(generation) + '+' + str(generation+100) + '_1_0_5_0.60.csv'  
				getAccuracy2(groundTruthsFile, groundTruthsFile2, clusterFile2, accuracyOutputFile2, assignmentsOutputFile2)
				
				clusterFile3 = 'dbscan/' + cond + '_' + str(iter) + '_' + str(generation) + '+' + str(generation+100) + '_0_1_5_0.15.csv'
				accuracyOutputFile3 = 'dbscan/Accuracy/' + cond + '_' + str(iter) + '_' + str(generation) + '+' + str(generation+100) + '_0_1_5_0.15.csv' 
				assignmentsOutputFile3 = 'dbscan/Assignments/' + cond + '_' + str(iter) + '_' + str(generation) +  '+' + str(generation+100) + '_0_1_5_0.15.csv' 
				getAccuracy2(groundTruthsFile, groundTruthsFile2, clusterFile3, accuracyOutputFile3, assignmentsOutputFile3)
				
				clusterFile4 = 'spectral/' + cond + '_' + str(iter) + '_' + str(generation) + '+' + str(generation+100) + '_1_1_3_0.5.csv'
				accuracyOutputFile4 = 'spectral/Accuracy/' + cond + '_' + str(iter) + '_' + str(generation) + '+' + str(generation+100) + '_1_1_3_0.5.csv' 
				assignmentsOutputFile4 = 'spectral/Assignments/' + cond + '_' + str(iter) + '_' + str(generation) + '+' + str(generation+100) + '_1_1_3_0.5.csv'
				getAccuracy2(groundTruthsFile, groundTruthsFile2, clusterFile4, accuracyOutputFile4, assignmentsOutputFile4)
				
				clusterFile5 = 'spectral/' + cond + '_' + str(iter) + '_' + str(generation) + '+' + str(generation+100) + '_1_0_3_0.5.csv'
				accuracyOutputFile5 = 'spectral/Accuracy/' + cond + '_' + str(iter) + '_' + str(generation) + '+' + str(generation+100) + '_1_0_3_0.5.csv' 
				assignmentsOutputFile5 = 'spectral/Assignments/' + cond + '_' + str(iter) + '_' + str(generation) + '+' + str(generation+100) + '_1_0_3_0.5.csv' 
				getAccuracy2(groundTruthsFile, groundTruthsFile2, clusterFile5, accuracyOutputFile5, assignmentsOutputFile5)
				
				clusterFile6 = 'spectral/' + cond + '_' + str(iter) + '_' + str(generation) + '+' + str(generation+100) + '_0_1_3_0.5.csv'
				accuracyOutputFile6 = 'spectral/Accuracy/' + cond + '_' + str(iter) + '_' + str(generation) + '+' + str(generation+100) + '_0_1_3_0.5.csv'
				assignmentsOutputFile6 = 'spectral/Assignments/' + cond + '_' + str(iter) + '_' + str(generation) + '+' + str(generation+100) + '_0_1_3_0.5.csv'				
				getAccuracy2(groundTruthsFile, groundTruthsFile2, clusterFile6, accuracyOutputFile6, assignmentsOutputFile6)
