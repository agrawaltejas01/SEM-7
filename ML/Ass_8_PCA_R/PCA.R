data("iris")
ind <- sample(2,nrow(iris),
              replace = TRUE,
              prob = c(0.8,0.2))
trainig <- iris[ind==1,]
testing <- iris[ind==2,]

library(psych)
pairs.panels(trainig[,-5],
             gap=1,
             bg=c("red","yellow","blue")[trainig$Species],
             pch=21)

pc <- prcomp(trainig[,-5],
             center = TRUE,
             scale. = TRUE)
print(pc)
attributes(pc)
summary(pc)
pc$center   #mean
pc$scale #std deviation


pairs.panels(pc$x,
             gap=0,
             bg=c("red","yellow","blue")[trainig$Species],
             pch=21)

plot(pc)
biplot(pc)

screeplot(pc,type = "line",main = "Screen Plot")
