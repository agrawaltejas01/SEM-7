data <- read.csv("/home/test/BE/CL-7_practice/ML/Datasets/Abalone Dataset/abalone.data")
names(data)

colnames(data) <- c('Sex', 'Length', 'Diameter', 'Height', 'Whole.weight', 'Shucked.weight',
                    'Viscera.weight', 'Shell.weight', 'Rings')

ind <- sample(2,nrow(data),replace=TRUE,prob=c(0.8,0.2))
training <- data[ind==1,]
testing <- data[ind==2,]
nrow(training)
nrow(testing)

c <- cor(data$Length,data$Whole.weight)
summary(c)


reg <- lm(training$Length~training$Whole.weight)
summary(reg)
y_pred <-predict(reg,newdata=testing)
y_pred
plot(training$Length,training$Whole.weight)
abline(reg)