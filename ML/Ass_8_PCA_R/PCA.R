# Read the file
mydata <- read.csv("/home/test/BE/CL-7_practice/ML/Ass_8_PCA_R/pca_gsp.csv")

# attach function attaches dataset to R search file
attach(mydata)

# Returns names of attributes
names(mydata)

# cbind function takes sequence of vector,matrix, or data-frame arguments and combine by columns or rows respectively
X <- cbind(Ag,Mining,Constr,Manuf,Manuf_nd,Transp,Comm,Energy,TradeW,TradeR,RE,Services,Govt)
summary(X)

# cor() function will calculate the correlation between two vectors, or will create a correlation matrix when given a matrix
cor(X)

# princomp performs a principal components analysis on the given numeric data matrix and returns the results as an object of class princomp
pcal <- princomp(X,scores = TRUE, cor = TRUE)
summary(pcal)

plot(pcal)
screeplot(pcal,type = "line",main = "Screen Plot")
biplot(pcal)
pcal$scores[1:10,]
