import csv
import json

file = open("../data/RiskData.csv")
csvFile = csv.reader(file)
next(csvFile)

dApps = []
dAppRisk = {}

data = []

for line in csvFile:
	if line[2] not in dApps:
		dApps.append(line[2])
	data.append(line)

for dApp in dApps:
	totalRisk = {}
	totalRisk['Total Low Risk Contracts'] = 0
	totalRisk['Total Medium Risk Contracts'] = 0
	totalRisk['Total High Risk Contracts'] = 0
	totalRisk['Total Extreme Risk Contracts'] = 0
	dAppRisk[dApp] = totalRisk

for dApp in data:
	if dApp[1] == '1':
		dAppRisk[dApp[2]]['Total Low Risk Contracts'] = dAppRisk[dApp[2]]['Total Low Risk Contracts'] + 1
	elif dApp[1] == '5':
		dAppRisk[dApp[2]]['Total Medium Risk Contracts'] = dAppRisk[dApp[2]]['Total Medium Risk Contracts'] + 1
	elif dApp[1] == '10':
		dAppRisk[dApp[2]]['Total High Risk Contracts'] = dAppRisk[dApp[2]]['Total High Risk Contracts'] + 1
	elif dApp[1] == '15':
		dAppRisk[dApp[2]]['Total Extreme Risk Contracts'] = dAppRisk[dApp[2]]['Total Extreme Risk Contracts'] + 1

dataFile = open('../data/DAppRisk.csv', 'w')
csvWriter = csv.writer(dataFile)

row = []
rows = []
for key in dAppRisk:
	row.append(dAppRisk[key]['Total Low Risk Contracts'])
rows.append(row)

row = []
for key in dAppRisk:
	row.append(dAppRisk[key]['Total Medium Risk Contracts'])
rows.append(row)

row = []
for key in dAppRisk:
	row.append(dAppRisk[key]['Total High Risk Contracts'])
rows.append(row)

row = []
for key in dAppRisk:
	row.append(dAppRisk[key]['Total Extreme Risk Contracts'])
rows.append(row)
print(rows)	

 
header = dApps
csvWriter.writerow(header)

csvWriter.writerows(rows)

#print(dAppRisk)


# TODO: find the percent of each dApps contracts that are of each risk level (histogram)