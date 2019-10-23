library(arules)
library(readxl)

data=read.transactions("/home/test/BE/CL-7_practice/ML/Datasets/Retail Dataset/Online Retail.csv")
inspect(data[1:5])

gr_rules <- apriori(data, parameter = list(conf = 0.8, supp = 0.001))
gr_rules
inspect(gr_rules[1:5])

#apriori()