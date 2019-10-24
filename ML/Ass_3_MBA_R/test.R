library(arules)
data("Groceries")
data=read.transactions("/home/test/BE/CL-7_practice/ML/Datasets/Retail Dataset/Online Retail.csv",format = 'basket', sep=',')
rules <- apriori(data, parameter = list(supp = 0.001, conf = 0.8))
inspect(rules[1:5])

rules <- sort(rules, by = 'support', decreasing = TRUE)
inspect(rules)

redundant <- is.redundant(rules)
rules <- rules[!redundant]
summary(redundant)

