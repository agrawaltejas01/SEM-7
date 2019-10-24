"
#Import
data <- read.csv('/home/test/BE/CL-7_practice/ML/Ass_8_PCA_R/diabetes_csv.csv')
data$class = ifelse(data$class == 'tested_positive', 1, 0)
#Split in train and test
ind <- sample(2,nrow(data), replace = TRUE, prob = c(0.8, 0.2) )
train <- data[ind == 1,]
test <- data[ind==2, ]

nrow(train)
nrow(test)

#PCA
library(psych)
pairs.panels(train[, -5],
             gap = 0,
             bg=c('red', 'green', 'blue')[train$class],
             pch = 21)
pc <- prcomp(train[, -5], center = TRUE, scale. = TRUE)
summary(pc)
attributes(pc)

pairs.panels(pc$x,
             gap = 0,
             bg=c('red', 'green', 'blue')[train$class],
             pch = 21)

plot(pc)
biplot(pc)
screeplot(pc, type = 'line'')"

"
#Import
data <- read.csv('/home/test/BE/CL-7_practice/ML/Datasets/Wine Dataset/wine.data', header = TRUE)

#Split
ind <- sample(2, nrow(data), replace = TRUE, prob = c(0.8, 0.2))

train <- data[ind == 1, ]
test <- data[ind==2, ]

#PCA
library(psych)
pairs.panels(train[, -1],
             gap = 0,
             bg = c('red', 'green', 'blue'),
             pch = 21)
pc <- prcomp(train[, -1],
             center = TRUE,
             scale. = TRUE)

attributes(pc)
summary(pc)
pc$x
pairs.panels(pc$x,
             gap = 0,
             bg = c('red', 'green', 'blue'),
             pch = 21)

plot(pc)
biplot(pc)
screeplot(pc, type = 'line')
"
"
#Import
data <- read.csv('/home/test/BE/CL-7_practice/ML/Ass_8_PCA_R/diabetes_csv.csv')
data$class = ifelse(data$class == 'tested_positive', 1, 0)

#Split data
ind <- sample(2, nrow(data), replace = TRUE ,prob = c(0.8, 0.2))
train = data[ind == 1,]
test = data[ind == 2,]

#PCA
library(psych)

pairs.panels(train[,-8], gap = 0, pch = 21, bg = c('red', 'green'))

pc <- prcomp(train[, -8], center = TRUE, scale. = TRUE)
summary(pc)
attributes(pc)
pc$center

pairs.panels(pc$x, gap = 0, bg = c('red', 'green'), pch = 21)
"

library(arules)

data <- read.csv('/home/test/BE/CL-7_practice/ML/Datasets/Wine Dataset/wine.data')

ind <- sample(2, nrow(data), prob = c(0.8, 0.2), replace = TRUE)

train <- data[ind==1, ]
test <- data[ind==2, ]

library(psych)
pairs.panels(train[, -1], gap = 0, bg = c('red', 'green', 'blue')[train$X1], pch = 21)

pc <- prcomp(train[, -1],
             center = TRUE,
             scale. = TRUE)
summary(pc)
pairs.panel(pc$x,
            gap = 0,
            bg = c('red', '))