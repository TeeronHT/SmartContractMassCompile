import pandas as pd
import csv
import matplotlib.pyplot as plt
import seaborn as sns

NoRisk = 0
LowRisk = 0
MediumRisk = 0
HighRisk = 0

with open("../data/RiskData.csv", 'r') as csvfile:
    datareader = csv.reader(csvfile)
    for row in datareader:
        if row[1] == '0':
            NoRisk = NoRisk + 1
        elif row[1] == '1':
            LowRisk = LowRisk + 1
        elif row[1] == '5':
            MediumRisk = MediumRisk + 1
        elif row[1] == '10':
            HighRisk = HighRisk + 1
        elif row[1] == '15':
            ExtremeRisk = ExtremeRisk + 1
            
riskDict = {'No Risk': NoRisk, 'Low Risk': LowRisk, 'Medium Risk': MediumRisk, 'High Risk': HighRisk, 'ExtremeRisk': ExtremeRisk}
        
labels = []
data = []

for riskLevel, riskFrequency in riskDict.items():
    labels.append(riskLevel + ': ' + str(riskFrequency) + ' contracts')
    data.append(riskFrequency)
    
sns.set_style('whitegrid')
plt.rcParams['text.color'] = 'black'
explode = (0, 0, 0, 0.1, 0)

colors = sns.color_palette('bright')[4:len(riskDict) + 5]
plt.pie(data, explode=explode, labels=labels, colors=colors, startangle=45)
plt.title('Frequency of Risk Levels', fontweight='bold')

plt.axis('equal')

plt.savefig("PieChart.png")

plt.show()
