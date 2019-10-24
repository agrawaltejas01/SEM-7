"library(arules)
library(readxl)

data=read.transactions("/home/test/BE/CL-7_practice/ML/Datasets/Retail Dataset/Online Retail.csv")
inspect(data[1:5])

gr_rules <- apriori(data, parameter = list(conf = 0.8, supp = 0.001))
gr_rules
inspect(gr_rules[1:5])

#apriori()"

library(arules)
data("Groceries")
#data = read.transactions('/home/test/BE/CL-7_practice/ML/Datasets/Retail Dataset/Online Retail.csv')
rules <- apriori(Groceries, parameter = list(supp = 0.001, conf = 0.8))
inspect(rules[1:5])

rules <- sort(rules, by = 'support', decreasing = TRUE)
inspect(rules)

redundant <- is.redundant(rules)
rules <- rules[!redundant]
summary(redundant)

beer <- apriori(Groceries, parameter = list(supp = 0.001, conf = 0.08), appearance = list(default="rhs", lhs = c({"yogurt", "butter"})))
