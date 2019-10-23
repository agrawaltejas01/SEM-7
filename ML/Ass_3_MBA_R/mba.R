library(arules)
data("Groceries")
Groceries
#View(Groceries)
gr_rules <- apriori(Groceries,parameter = list(supp = 0.001,conf = 0.8))

gr_rules <- sort(gr_rules,by ="support",decreasing = TRUE)
gr_rules
inspect(gr_rules[1:5])


gr_redundant <- is.redundant(gr_rules)
summary(gr_redundant)

gr_rules <- gr_rules[!gr_redundant]
gr_rules
summary(gr_rules)


gr_rules_wholeMilk <- apriori(Groceries,parameter = list(supp=0.001,conf=0.08),appearance = list(default="rhs",lhs="whole milk"))
gr_rules_wholeMilk

inspect(gr_rules_wholeMilk[1:35])
