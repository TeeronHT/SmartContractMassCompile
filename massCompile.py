import json
import requests

def main():
	

	files = open('portalDAppsList.json')
	portalDApps = json.load(files)
	
	# Not all of these work when imported into Retool for some reason
	# 'gem', 'curv'
	with open('EthereumMainnetContracts.json') as file:
		contractData = list(file)

	contracts = []
	for i in range(len(contractData)):
		for key in portalDApps:
			firstN = contractData[i][contractData[i].index("name") + 8:]
			name = firstN[:firstN.index("\"")]
			firstA = contractData[i][contractData[i].index("address") + 11:]
			address = firstA[:firstA.index("\"")]
			if key.replace(" ", "").upper() in name.upper():
				contractList = {}
				if 'V1' not in key.upper() and 'V2' not in key.upper():
					#if (TRMVerification(address, 'ethereum') == True):
					contractList['contractAddress'] = address
					contractList['dAppName'] = key
					contractList['contractUrl'] = portalDApps[key]
					contractList['networkName'] = "EthereumMainnet"
					contracts.append(contractList)

	with open('Data.json', 'w') as outfile:
		json.dump(contracts, outfile)

def TRMVerification(address, network):
	url = "https://api.trmlabs.com/public/v2/screening/addresses"

	payload = [{"address": address, "chain": network}]
	headers = {"Content-Type": "application/json"}
	response = requests.post(url, json=payload, headers=headers, auth=('<API_KEY>','<API_KEY>'))

	data = response.json()

	try:
		riskLevel = data[0]['addressRiskIndicators'][0]['categoryRiskScoreLevelLabel']

		if riskLevel == "Low" or riskLevel == "Unkown":
			return True
		else:
			return False
	except IndexError:
		return False
	

if __name__ == '__main__':
	main()
