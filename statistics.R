library(ggplot2)

data <- read.csv("/var/www/html/TCC-UTFPR/statistics.csv") # Lê o arquivo com as estatísticas

dat = data[,c(2,3)]
dat

mydata <- dat
wss <- (nrow(mydata)-1)*sum(apply(mydata,2,var))
for (i in 2:15) wss[i] <- sum(kmeans(mydata,
                                     centers=i)$withinss)

plot(1:15, wss, type="b", xlab="Number of Clusters",
     ylab="Within groups sum of squares",
     main="Assessing the Optimal Number of Clusters with the Elbow Method",
     pch=20, cex=2)

# Perform K-Means with the optimal number of clusters identified from the Elbow method
set.seed(7)
km2 = kmeans(dat, 3, nstart=100)

# Examine the result of the clustering algorithm
plot(dat, col =(km2$cluster +1) , main="K-Means result with 3 clusters", pch=20, cex=2)


