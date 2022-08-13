import csv
import json


def main():
	contracts_with_risk()
	category_risk()

def category_risk():
	file = open("../data/ContractData.json")
	data = json.load(file)

	categories = []
	alreadyListed = []
	for contract in data: 
		unlisted = True
		dAppCategories = contract["risks"]
		if dAppCategories == None:
			continue
		for key, value in dAppCategories.items():
			for category in categories:
				if key == category["category"]:
					unlisted = False
					category["frequency"] = category["frequency"] + 1
					category["total risk"] = category["total risk"] + value

			risk = {}
			if unlisted == True:
				alreadyListed.append(key)
				risk["category"] = key
				risk["frequency"] = 1
				risk["total risk"] = value
				risk["average risk"] = risk["total risk"] / risk["frequency"]
				categories.append(risk)
			unlisted = True

	dataFile = open('../data/CategoryRisk.csv', 'w')
	csvWriter = csv.writer(dataFile)

	headers = categories[0].keys()

	rows = []
	for category in categories:
		rows.append(category.values())
	print(rows)

	csvWriter.writerow(headers)
	csvWriter.writerows(rows)

def contracts_with_risk():
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

if __name__ == "__main__":
	main()



