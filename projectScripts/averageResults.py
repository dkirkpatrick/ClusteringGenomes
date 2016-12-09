from subprocess import call
import sys
import csv
import math 

conditions =  ['C0__TSK_0.0', 'C1__TSK_1.0', 'C3__TSK_10']
replicates = range(101,116)

mode = 'analyze'
#mode = 'cluster'

min_pts = '3'
epsilon = '0.5'

genoVal = '1'
phenoVal = '1'

count11 = 0
count10 = 0
count01 = 0
sumMin11 = 0.0
sumMin10 = 0.0
sumMin01 = 0.0
sumMax11 = 0.0
sumMax10 = 0.0
sumMax01 = 0.0
sumAvg11 = 0.0
sumAvg10 = 0.0
sumAvg01 = 0.0

for cond in conditions: 
	for iter in replicates: 
		for generation in range(0, 1100, 100): 
			combindedOFString1 = mode + '/' + cond + '_' + str(iter) + '_' + str(generation) + '_1_1_' + min_pts + '_' + epsilon + '.csv'
			combindedOFString2 = mode + '/' + cond + '_' + str(iter) + '_' + str(generation) + '_1_0_' + min_pts + '_' + epsilon + '.csv'
			combindedOFString3 = mode + '/' + cond + '_' + str(iter) + '_' + str(generation) + '_0_1_' + min_pts + '_' + epsilon + '.csv'
			with open(combindedOFString1) as file11csv, open(combindedOFString2) as file10csv, open(combindedOFString3) as file01csv:
				file11reader = csv.reader(file11csv, delimiter=',')
				file10reader = csv.reader(file10csv, delimiter=',')
				file01reader = csv.reader(file01csv, delimiter=',')
				row = 1
				col = 1
				for row11 in file11reader:
					countRow = 1
					if math.isinf(float(row11[1])) or math.isnan(float(row11[1])): 
						print(combindedOFString1 + ' 1 1 '+ row11[1])					
					min = float(row11[1])
					sum = float(row11[1])
					max = float(row11[1])
					if row == 1:
						if math.isinf(float(row11[2])) or math.isnan(float(row11[2])): 
							print(combindedOFString1 + ' 1 2 '+ row11[2])					
						min = float(row11[2])
						sum = float(row11[2])
						max = float(row11[2])
						countRow = 0
					for item in row11[2:]: 
						if math.isinf(float(item)) or math.isnan(float(item)): 
							print(combindedOFString1 + ' ' + str(row) + ' ' + str(col) + item)
						if row != col: 
							if min > float(item): 
								min = float(item)
							if max < float(item): 
								max = float(item)
							sum += float(item)
							countRow += 1
						col += 1
					col = 1
					row += 1
					count11 += 1
					sumMin11 += min 
					sumMax11 += max
					sumAvg11 += sum/countRow
				row = 1
				col = 1
				for row10 in file10reader:
					countRow = 1
					if math.isinf(float(row10[1])) or math.isnan(float(row10[1])): 
						print(combindedOFString2 + ' 1 1 '+ row10[1])
					min = float(row10[1])
					sum = float(row10[1])
					max = float(row10[1])
					if row == 1: 
						if math.isinf(float(row10[2])) or math.isnan(float(row10[2])): 
							print(combindedOFString2 + ' 1 2 '+ row10[2])
						min = float(row10[2])
						sum = float(row10[2])
						max = float(row10[2])
						countRow = 0
					for item in row10[2:]: 
						if math.isinf(float(item)) or math.isnan(float(item)): 
							print(combindedOFString2 + ' ' + str(row) + ' ' + str(col) + item)
						if row != col: 
							if min > float(item): 
								min = float(item)
							if max < float(item): 
								max = float(item)
							sum += float(item)
							countRow += 1
						col += 1
					col = 1
					row += 1
					count10 += 1
					sumMin10 += min 
					sumMax10 += max
					sumAvg10 += sum/countRow
				row = 1
				col = 1
				for row01 in file01reader:
					countRow = 1
					if math.isinf(float(row01[1])) or math.isnan(float(row01[1])): 
							print(combindedOFString3 + ' 1 1 '+ row01[1])
					min = float(row01[1])
					sum = float(row01[1])
					max = float(row01[1])
					if row == 1: 
						if math.isinf(float(row01[2])) or math.isnan(float(row01[2])): 
							print(combindedOFString3 + ' 1 2 '+ row01[2])
						min = float(row01[2])
						sum = float(row01[2])
						max = float(row01[2])
						countRow = 0
					for item in row01[2:]: 
						if math.isinf(float(item)) or math.isnan(float(item)): 
							print(combindedOFString3 + ' ' + str(row) + ' ' + str(col) + item)
						if row != col: 
							if min > float(item): 
								min = float(item)
							if max < float(item): 
								max = float(item)
							sum += float(item)
							countRow += 1
						col += 1
					col = 1
					row += 1
					count01 += 1
					sumMin01 += min 
					sumMax01 += max
					sumAvg01 += sum/countRow

for cond in conditions: 
	for iter in replicates: 
		for generation in range(0, 1000, 100): 
			combindedOFString1 = mode + '/' + cond + '_' + str(iter) + '_' + str(generation) + '+' + str(generation+100) + '_1_1_' + min_pts + '_' + epsilon + '.csv'
			combindedOFString2 = mode + '/' + cond + '_' + str(iter) + '_' + str(generation) + '+' + str(generation+100) + '_1_0_' + min_pts + '_' + epsilon + '.csv'
			combindedOFString3 = mode + '/' + cond + '_' + str(iter) + '_' + str(generation) + '+' + str(generation+100) + '_0_1_' + min_pts + '_' + epsilon + '.csv'
			with open(combindedOFString1) as file11csv, open(combindedOFString2) as file10csv, open(combindedOFString3) as file01csv:
				file11reader = csv.reader(file11csv, delimiter=',')
				file10reader = csv.reader(file10csv, delimiter=',')
				file01reader = csv.reader(file01csv, delimiter=',')
				row = 1
				col = 1
				for row11 in file11reader:
					countRow = 1
					if math.isinf(float(row11[1])) or math.isnan(float(row11[1])): 
						print(combindedOFString1 + ' 1 1 '+ row11[1])					

					min = float(row11[1])
					sum = float(row11[1])
					max = float(row11[1])
					if row == 1: 
						if math.isinf(float(row11[2])) or math.isnan(float(row11[2])): 
							print(combindedOFString1 + ' 1 2 '+ row11[2])
						min = float(row11[2])
						sum = float(row11[2])
						max = float(row11[2])
						countRow = 0
					for item in row11[2:]: 
						if math.isinf(float(item)) or math.isnan(float(item)): 
							print(combindedOFString1 + ' ' + str(row) + ' ' + str(col) + item)
						if row != col: 
							if min > float(item): 
								min = float(item)
							if max < float(item): 
								max = float(item)
							sum += float(item)
							countRow += 1
						col += 1
					col = 1
					row += 1
					count11 += 1
					sumMin11 += min 
					sumMax11 += max
					sumAvg11 += sum/countRow
				row = 1
				col = 1
				for row10 in file10reader:
					countRow = 1
					if math.isinf(float(row10[1])) or math.isnan(float(row10[1])): 
						print(combindedOFString2 + ' 1 1 '+ row10[1])
					min = float(row10[1])
					sum = float(row10[1])
					max = float(row10[1])
					if row == 1: 
						if math.isinf(float(row10[2])) or math.isnan(float(row10[2])): 
							print(combindedOFString2 + ' 1 2 '+ row10[2])
						min = float(row10[2])
						sum = float(row10[2])
						max = float(row10[2])
						countRow = 0
					for item in row10[2:]: 
						if math.isinf(float(item)) or math.isnan(float(item)): 
							print(combindedOFString2 + ' ' + str(row) + ' ' + str(col) + item)
						if row != col: 
							if min > float(item): 
								min = float(item)
							if max < float(item): 
								max = float(item)
							sum += float(item)
							countRow += 1
						col += 1
					col = 1
					row += 1
					count10 += 1
					sumMin10 += min 
					sumMax10 += max
					sumAvg10 += sum/countRow
				row = 1
				col = 1
				for row01 in file01reader:
					countRow = 1
					if math.isinf(float(row01[1])) or math.isnan(float(row01[1])): 
						print(combindedOFString3 + ' 1 1 '+ row01[1])
					min = float(row01[1])
					sum = float(row01[1])
					max = float(row01[1])
					if row == 1: 
						if math.isinf(float(row01[2])) or math.isnan(float(row01[2])): 
							print(combindedOFString3 + ' 1 2 '+ row01[2])
						min = float(row01[2])
						sum = float(row01[2])
						max = float(row01[2])
						countRow = 0
					for item in row01[2:]: 
						if math.isinf(float(item)) or math.isnan(float(item)): 
							print(combindedOFString3 + ' ' + str(row) + ' ' + str(col) + item)
						if row != col: 
							if min > float(item): 
								min = float(item)
							if max < float(item): 
								max = float(item)
							sum += float(item)
							countRow += 1
						col += 1
					col = 1
					row += 1
					count01 += 1
					sumMin01 += min 
					sumMax01 += max
					sumAvg01 += sum/countRow

print('MIN11: ' + str(sumMin11) +'\tMAX11: ' + str(sumMax11) +'\tAVG11: ' + str(sumAvg11) + '\tcount11: ' + str(count11))
print('MIN10: ' + str(sumMin10) +'\tMAX10: ' + str(sumMax10) +'\tAVG10: ' + str(sumAvg10) + '\tCOUNT10: ' + str(count10))
print('MIN01: ' + str(sumMin01) +'\tMAX01: ' + str(sumMax01) +'\tAVG01: ' + str(sumAvg01) + '\tCOUNT01: ' + str(count01)) 

print('\n')
					
print('MIN11: ' + str(sumMin11/count11) +'\tMAX11: ' + str(sumMax11/count11) +'\tAVG11: ' + str(sumAvg11/count11) + '\tcount11: ' + str(count11))
print('MIN10: ' + str(sumMin10/count10) +'\tMAX10: ' + str(sumMax10/count10) +'\tAVG10: ' + str(sumAvg10/count10) + '\tCOUNT10: ' + str(count10))
print('MIN01: ' + str(sumMin01/count01) +'\tMAX01: ' + str(sumMax01/count01) +'\tAVG01: ' + str(sumAvg01/count01) + '\tCOUNT01: ' + str(count01)) 
