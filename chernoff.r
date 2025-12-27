install.packages("aplpack")
library(aplpack)
#Example 1:Using manually created Data Frame
data=data.frame(height=c(150,160,170,180,190),weight=c(50,60,70,80,90),age=c(20,25,30,35,40),score=c(60,65,70,75,80))
data
summary(data) 
faces(data)
# Example 2:Using Normally Distributed Data of 50 Observations
set.seed(123)
data1=data.frame(height=rnorm(50,mean=170,sd=8),weight=rnorm(50,mean=65,sd=10),age=rnorm(50,mean=30,sd=5),score=rnorm(50,mean=75,sd=12))
data1
head(data1)
plot(data1)
faces(data1)
#example 3:using Built-in iris Dataset
data(iris)
head(iris)
faces(iris[,-5],main="chernoff faces for iris data")

# Create output folder and save plots
dir.create("plots", showWarnings = FALSE, recursive = TRUE)

# Save Chernoff faces for the iris dataset
png(filename = "plots/chernoff_iris.png", width = 800, height = 800)
faces(iris[,-5], main = "chernoff faces for iris data")
dev.off()

# Save Chernoff faces for the simulated data (data1)
png(filename = "plots/chernoff_data1.png", width = 800, height = 800)
faces(data1, main = "chernoff faces for simulated data1")
dev.off()

png(filename = "plots/chernoff_plot.png", width = 800, height = 800)
faces(data, main = "chernoff faces for data")
dev.off()
