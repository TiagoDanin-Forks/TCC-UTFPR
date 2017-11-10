# Tutorial: http://www.sthda.com/english/articles/25-cluster-analysis-in-r-practical-guide/111-types-of-clustering-methods-overview-and-quick-start-r-code/
install.packages("factoextra")
install.packages("factoextra")
install.packages("Hmisc")
install.packages("cluster")
install.packages("magrittr")
library("ggplot2")
library("cluster")
library("factoextra")
library("magrittr")
library(dplyr)
library("Hmisc")

data_project <- read.csv("/var/www/html/TCC-UTFPR/projects_cluster_data.csv")
# data_newcomers <- read.csv("/var/www/html/TCC-UTFPR/newcomers_cluster_data.csv")

values <- unique(data_project[,-1]) 
row.names(values) <- unique(data_project[,1])
values <- values %>%
          na.omit() %>%          # Remove missing values (NA)
          scale()                # Scale variables

variaveis_independentes = subset(values, select = c(2,4,5,6,8))
correlationCluster = varclus(~., data=variaveis_independentes,trans="abs")
plot(correlationCluster, main="2013")
thresh = 0.7
abline(h = 1 - thresh , col="#bf0000", lty =2, lwd=3)

fviz_nbclust(variaveis_independentes, kmeans, method = "gap_stat") # Suggested number of cluster: 8

set.seed(123)
km.res <- kmeans(variaveis_independentes, 3, nstart = 25)
km.res$cluster
# Visualize
fviz_cluster(km.res, data = values,
             ellipse.type = "convex",
             palette = "jco",
             ggtheme = theme_minimal())

pam.res <- pam(values, 8)
fviz_cluster(pam.res)

# Compute hierarchical clustering
res.hc <- data_project[,c(2:14)] %>%
  scale() %>%                    # Scale the data
  dist(method = "euclidean") %>% # Compute dissimilarity matrix
  hclust(method = "ward.D2")     # Compute hierachical clustering

png(filename="/var/www/html/TCC-UTFPR/cluster.png")
# Visualize using factoextra
# Cut in 4 groups and color by groups
fviz_dend(res.hc, k = 4, # Cut in four groups
          cex = 0.5, # label size
          k_colors = c("#2E9FDF", "#00AFBB", "#E7B800", "#FC4E07"),
          color_labels_by_k = TRUE, # color labels by groups
          rect = TRUE # Add rectangle around groups
)
dev.off()
