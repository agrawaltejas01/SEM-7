#apriori need transaction not dataframe
#Hence if given a csv file use read.transaction()

#Get Library and dataset

"library(arules)
data("Groceries")

# Apply apriori algo to get assosciation rule
gr_rules <- apriori(Groceries, parameter = list(conf = 0.8, supp = 0.001))
gr_rules
inspect(gr_rules[1:5])

#Sort by some parameter
gr_rules <- sort(gr_rules, decreasing = TRUE, by = "support")
inspect(gr_rules)

#Remove redundant rules
redundant_rules = is.redundant(gr_rules)
redundant_rules
summary(redundant_rules)

gr_rules = gr_rules[!redundant_rules]
gr_rules

#Check rules for a given product
rule_liquor <- apriori(Groceries, parameter = list(conf = 0.08, supp = 0.001),
                       appearance = list(default = "rhs", lhs = "liquor"))
inspect(rule_liquor[1:5])
"
#Get Library and dataset
library(arules)
data("Groceries")

#Apply algo
rules <- apriori(Groceries, parameter = list(supp = 0.001, conf = 0.8))
rules
inspect(rules)

#Sort by some parameter
rules <- sort(rules, by = "support", decreasing = TRUE)
inspect(rules[1:5])

#Remove redundant rules
redundant <- is.redundant(rules)
summary(redundant)
rules <- rules[!redundant]
rules

#Check for a given item
rule_curd <- apriori(Groceries, parameter = list(supp = 0.0001, conf = 0.8))
