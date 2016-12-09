from subprocess import call
import sys
import csv
import math

conditions =  ['C0__TSK_0.0', 'C1__TSK_1.0', 'C3__TSK_10']
replicates = range(101,116)

mode = 'analysis'
#mode = 'cluster'

count = 0
for cond in conditions: 
	for iter in replicates: 
		for generation in range(0, 1100, 100): 
			combindedIFString = 'clusterData/' + cond + '_' + str(iter) + '_' + 'clusterData_' + str(generation) + '.csv'
			with open(combindedIFString, newline='') as csvfile:
				csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
				next(csvreader)
				for row in csvreader:
					for item in row: 
						if math.isinf(float(item)) or math.isnan(float(item)): 
							print(combindedIFString1 + row[0] + item)

for cond in conditions: 
	for iter in replicates: 
		for generation in range(0, 1000, 100): 
			combindedIFString = 'combinedData/' + cond + '_' + str(iter) + '_' + 'clusterData_' + str(generation) + '+' + str(generation+100) + '.csv' 
			with open(combindedIFString, newline='') as csvfile:
				csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
				next(csvreader)
				for row in csvreader:
					for item in row: 
						if math.isinf(float(item)) or math.isnan(float(item)): 
							print(combindedIFString1 + row[0] + item)
