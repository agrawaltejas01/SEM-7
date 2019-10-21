data <- read.csv("/home/test/BE/CL-7_practice/ML/Ass_2_Regression_R/real_estate.csv")
data = data[, c(3:5, 8)] # only take independent variable (3:5) and dependent variable(8)

mse_test = c(1:8)
mse_train = c(1:8)  #make array of mse_test and mse_train for 