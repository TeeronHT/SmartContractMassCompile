import json
import requests

def main():
	
	files = open('./data/portalDAppsList.json')
	portalDApps = json.load(files)
	# Not all of these work when imported into Retool for some reason
	# 'gem', 'curv'

	with open('./contracts/EthereumMainnetContracts.json') as file:
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
					if (TRMVerification(address, 'ethereum') == True):
						contractList['contractAddress'] = address
						contractList['dAppName'] = key
						contractList['contractUrl'] = portalDApps[key]
						contractList['networkName'] = "EthereumMainnet"
						contracts.append(contractList)

	with open('./data/Data.json', 'w') as outfile:
		json.dump(contracts, outfile)

def TRMVerification(address, network):
	url = "https://api.trmlabs.com/public/v2/screening/addresses"

	payload = [{"address": address, "chain": network}]
	headers = {"Content-Type": "application/json"}
	response = requests.post(url, json=payload, headers=headers, auth=('<API_KEY>','<API_KEY>'))

	data = response.json()

	length = len(data[0]['addressRiskIndicators'])

	# Returns true if no "medium" or higher alerts come up (floating risk to the top)
	
	if length == 0:
		return True
	else: 
		for index in range(length):
			if data[0]['addressRiskIndicators'][index]['categoryRiskScoreLevel'] >= 4:
				return False
		return True

if __name__ == '__main__':
	main()

