library(ggplot2)

# Read data from CSV
data <- read.csv(file = '~/Desktop/Portal/SmartContractMassCompile/data/CategoryRisk.csv', header=TRUE)

# Selected variables
frequency <- data[, c(1, 2)]
totalRisk <- data[, c(1, 3)]
averageRisk <- data[, c(1, 4)]

# Risk Categories and their Frequency
print(ggplot(frequency, aes(x = category, y = frequency)) +
  geom_bar(stat="identity",fill="firebrick4") +
  geom_text(data = subset(data[, c(1, 2)], frequency > 30), aes(label = frequency), vjust = 1.5, colour = "White") +
  theme(axis.text.x = element_text(angle = 90, size = 5)) +
  ggtitle("Risk Categories and their Frequency") +
  labs(y = "Frequency of Risk", x = "Categories of Risk"))

# Risk Categories and their Cumulative Risk
print(ggplot(totalRisk, aes(x = category, y = total.risk)) +
  geom_bar(stat="identity",fill= "red", position = position_stack()) +
  geom_text(data = subset(data[, c(1, 3)], total.risk > 150), aes(label = total.risk), vjust = 1.5, colour = "White", size = 3) +
  theme(axis.text.x = element_text(angle = 90, size = 5)) +
  ggtitle("Risk Categories and their Cumulative Risk") +
  labs(y = "Cumulative Risk", x = "Categories of Risk"))

# Risk Categories and their Average Risk
print(ggplot(averageRisk, aes(x = category, y = average.risk)) +
  geom_bar(stat="identity",fill= "darkorange", position = position_stack()) +
  geom_text(data = subset(data[, c(1, 4)]), aes(label = average.risk), vjust = 1.5, colour = "White", size = 3) +
  theme(axis.text.x = element_text(angle = 90, size = 5)) +
  ggtitle("Risk Categories and their Average Risk") +
  labs(y = "Average Risk", x = "Categories of Risk"))
