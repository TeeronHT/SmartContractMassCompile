# Read data from CSV
data <- read.csv(file = '/Users/teeron/Desktop/Portal/SmartContractMassCompile/data/DAppRisk.csv')

# Create a matrix
matrixdata=as.matrix(data)

barplot(as.matrix(matrixdata), xlab = "dApps", ylab = "Number of Risky Contracts", main = "Risky Smart Contracts per Decentralized Apps", col = c("yellow", "darkorange1", "firebrick2", "firebrick4"))
legend("topright", legend=c("Low Risk Contracts", "Medium Risk Contracts", "High Risk Contracts", "Extreme Risk Contracts"), fill = c("yellow", "darkorange1", "firebrick2", "firebrick4"), cex=0.8)