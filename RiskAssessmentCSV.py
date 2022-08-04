import json
import csv

def main():
    files = open('./data/Data.json')
    dAppContracts = json.load(files)

    associatedRisk = []

    for contracts in range(len(dAppContracts)):
        address = dAppContracts[contracts]["contractAddress"]
        TRMVerification(address, 'ethereum', associatedRisk)

    writeCSV(associatedRisk)

    
def TRMVerification(address, network, associatedRisk):
    url = "https://api.trmlabs.com/public/v2/screening/addresses"

    payload = [{"address": address, "chain": network}]
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, json=payload, headers=headers, auth=('a02b3ef5-bc27-4b0d-a7b2-1093c0c0e41b','a02b3ef5-bc27-4b0d-a7b2-1093c0c0e41b'))

    data = response.json()

    length = len(data[0]['addressRiskIndicators'])

    riskCSV(data, address, associatedRisk)

def riskCSV(data, address, associatedRisk):
    
    # The below

    files = open('./data/Data.json')
    dAppContracts = json.load(files)

    length = len(data[0]['addressRiskIndicators'])


    dAppName = ""
    for contracts in range(len(dAppContracts)):
        if dAppContracts[contracts]["contractAddress"] == address:
            dAppName = dAppContracts[contracts]["dAppName"]
            break

    contract = {}
    riskLevel = 0
    if length > 0:
        for index in range(length):
            risk = data[0]['addressRiskIndicators'][index]['categoryRiskScoreLevel']
            if risk >= riskLevel:
                riskLevel = risk

    contract['Contract Address'] = address
    contract['Contract Risk Level'] = riskLevel
    contract['Associate DApp'] = dAppName

    associatedRisk.append(contract)

def writeCSV(associatedRisk):
    data_file = open('./data/Data.csv', 'w', newline='')
    csv_writer = csv.writer(data_file)
     
    count = 0
    for data in associatedRisk:
        if count == 0:
            header = data.keys()
            csv_writer.writerow(header)
            count += 1
        csv_writer.writerow(data.values())
     
    data_file.close()
    

if __name__ == '__main__':
    main()
