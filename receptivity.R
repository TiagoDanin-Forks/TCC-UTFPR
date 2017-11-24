# Author: Felipe Fronchetti
# Questions? fronchettiemail@gmail.com
require("effsize")
library(ggplot2)
library("plyr")
# Define your own working directory
setwd("/var/www/html/TCC-UTFPR")

# Reading files
receptive <- read.csv("data_receptive.csv")
nonreceptive <- read.csv("data_nonreceptive.csv")

count(receptive$domain)
count(nonreceptive$domain)

language_frequency <- read.csv("languages_frequency.csv")
domain_frequency <- read.csv("domain_frequency.csv")

ggplot(domain_frequency, aes(factor(domain), count, fill = type)) + 
  geom_bar(stat="identity", position = "dodge", colour="black", width = 0.6) + labs(y="Frequência", x = "") + guides(fill=guide_legend(title="")) + 
  scale_fill_manual(values=c("white","gray")) + theme(axis.text=element_text(size=14, colour = "black"), axis.text.x = element_text(angle = 45, hjust = 1), axis.title.y = element_text(size = 14), legend.text=element_text(size=14)) + theme(legend.position="top") + theme(legend.key.width=unit(3,"line"))

ggplot(language_frequency, aes(factor(language), count, fill = type)) + 
  geom_bar(stat="identity", position = "dodge", colour="black") + labs(y="Frequência", x = "") + guides(fill=guide_legend(title="")) + 
  scale_fill_manual(values=c("white","gray")) + theme(axis.text=element_text(size=14, colour = "black"), axis.text.x = element_text(angle = 45, hjust = 1), axis.title.y = element_text(size = 14), legend.text=element_text(size=14)) + theme(legend.position="top") + theme(legend.key.width=unit(3,"line"))

cor.test(receptive$pull_opened_mean, receptive$newcomers_mean, method="spearman")
cor.test(receptive$pull_closed_mean, receptive$newcomers_mean, method="spearman")
cor.test(receptive$pull_merged_mean, receptive$newcomers_mean, method="spearman")
cor.test(receptive$commits_mean, receptive$newcomers_mean, method="spearman")
cor.test(receptive$stars_mean, receptive$newcomers_mean, method="spearman")
cor.test(receptive$forks_mean, receptive$newcomers_mean, method="spearman")

cor.test(nonreceptive$pull_opened_mean, nonreceptive$newcomers_mean, method="spearman")
cor.test(nonreceptive$pull_closed_mean, nonreceptive$newcomers_mean, method="spearman")
cor.test(nonreceptive$pull_merged_mean, nonreceptive$newcomers_mean, method="spearman")
cor.test(nonreceptive$commits_mean, nonreceptive$newcomers_mean, method="spearman")
cor.test(nonreceptive$stars_mean, nonreceptive$newcomers_mean, method="spearman")
cor.test(nonreceptive$forks_mean, nonreceptive$newcomers_mean, method="spearman")

# Boxplots
# Size: 270 460
boxplot(receptive$pull_merged_mean, outline=FALSE, ylab="# Requisições aceitas", cex.lab=1.2, cex.axis=1.1)
boxplot(receptive$pull_closed_mean, outline=FALSE, ylab="# Requisições fechadas", cex.lab=1.2, cex.axis=1.1)
boxplot(receptive$pull_opened_mean, outline=FALSE, ylab="# Requisições abertas", cex.lab=1.2, cex.axis=1.1)
boxplot(receptive$commits_mean, outline=FALSE, ylab="# Contribuições", cex.lab=1.2, cex.axis=1.1)
boxplot(receptive$stars_mean, outline=FALSE, ylab="# Estrelas", cex.lab=1.2, cex.axis=1.1)
boxplot(receptive$forks_mean, outline=FALSE, ylab="# Cópias", cex.lab=1.2, cex.axis=1.1)

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
# Distribuição de novatos entre os projetos de software livre
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
par(mfrow=(c(1,2)))
par(oma = c(4, 4, 0, 0)) 
par(mar = c(2, 2, 1, 1)) 
x <- receptive$newcomers_mean
h<-hist(x, breaks=10, col="gray", xlab="", ylab = "", main = "") 
xfit<-seq(min(x),max(x),length=40) 
yfit<-dnorm(xfit,mean=mean(x),sd=sd(x)) 
yfit <- yfit*diff(h$mids[1:2])*length(x) 
lines(xfit, yfit, col="black", lwd=2)

x <- nonreceptive$newcomers_mean
h<-hist(x, breaks=10, col="gray", xlab="", ylab="", main = "") 
xfit<-seq(min(x),max(x),length=40) 
yfit<-dnorm(xfit,mean=mean(x),sd=sd(x)) 
yfit <- yfit*diff(h$mids[1:2])*length(x) 
lines(xfit, yfit, col="black", lwd=2)

mtext("# Novos Contribuidores", 1, 1, outer=TRUE)
mtext("# Projetos", 2, 1, outer=TRUE, las=0)

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
# Cálculos: Wilcox, Cliff e Fisher
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
# Opened pull requests
wilcox.test(receptive$pull_opened_mean, nonreceptive$pull_opened_mean)
cliff.delta(receptive$pull_opened_mean, nonreceptive$pull_opened_mean)
# Closed pull requests
wilcox.test(receptive$pull_closed_mean, nonreceptive$pull_closed_mean)
cliff.delta(receptive$pull_closed_mean, nonreceptive$pull_closed_mean)
# Merged pull requests
wilcox.test(receptive$pull_merged_mean, nonreceptive$pull_merged_mean)
cliff.delta(receptive$pull_merged_mean, nonreceptive$pull_merged_mean)
# Commits
wilcox.test(receptive$commits_mean, nonreceptive$commits_mean)
cliff.delta(receptive$commits_mean, nonreceptive$commits_mean)
# Stars
wilcox.test(receptive$stars_mean, nonreceptive$stars_mean)
cliff.delta(receptive$stars_mean, nonreceptive$stars_mean)
# Forks
wilcox.test(receptive$forks_mean, nonreceptive$forks_mean)
cliff.delta(receptive$forks_mean, nonreceptive$forks_mean)

# Has readme / Hasn't readme (Receptive), Has Readme / Hasn't readme (Nonreceptive)
readme.df = matrix(c(sum(receptive$has_readme == 1), sum(receptive$has_readme == 0), sum(nonreceptive$has_readme == 1), sum(nonreceptive$has_readme == 0)), nrow = 2, ncol=2)
fisher.test(readme.df)
