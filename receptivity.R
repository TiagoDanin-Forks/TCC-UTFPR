# Author: Felipe Fronchetti
# Questions? fronchettiemail@gmail.com
install.packages("vioplot")
require("effsize")
library(ggplot2)
require(gridExtra)
theme_minimal()

# Define your own working directory
setwd("/var/www/html/TCC-UTFPR")

# Reading files
receptive <- read.csv("data_receptive.csv")
nonreceptive <- read.csv("data_nonreceptive.csv")

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
# Gráficos violino para comparar os indicadores de receptividade com novatos
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
receptive_pulls_opened <- ggplot(receptive, aes(newcomers_mean, pull_opened_mean), outline = FALSE) + geom_violin(trim = FALSE, draw_quantiles = TRUE, ylim = c(0, max(pull_opened_mean))) + 
  labs(x="", y="# Requisições abertas") + theme(axis.text=element_text(size=10), panel.background = element_rect(fill = "white"))
receptive_pulls_closed <- ggplot(receptive, aes(newcomers_mean, pull_closed_mean), outline = FALSE) + geom_violin(trim = FALSE, draw_quantiles = TRUE) + 
  labs(x="", y="# Requisições fechadas") + theme(axis.text=element_text(size=10), panel.background = element_rect(fill = "white"))
receptive_pulls_merged <- ggplot(receptive, aes(newcomers_mean, pull_merged_mean), outline = FALSE) + geom_violin(trim = FALSE, draw_quantiles = TRUE) + 
  labs(x="", y="# Requisições aceitas") + theme(axis.text=element_text(size=10), panel.background = element_rect(fill = "white"))
receptive_commits <- ggplot(receptive, aes(newcomers_mean, commits_mean), outline = FALSE) + geom_violin(trim = FALSE, draw_quantiles = TRUE) + 
  labs(x="", y="# Contribuições") + theme(axis.text=element_text(size=10), panel.background = element_rect(fill = "white"))
receptive_stars <- ggplot(receptive, aes(newcomers_mean, stars_mean), outline = FALSE) + geom_violin(trim = FALSE, draw_quantiles = TRUE) + 
  labs(x="", y="# Estrelas") + theme(axis.text=element_text(size=10), panel.background = element_rect(fill = "white"))
receptive_forks <- ggplot(receptive, aes(newcomers_mean, forks_mean), outline = FALSE) + geom_violin(trim = FALSE, draw_quantiles = TRUE) + 
  labs(x="", y="# Cópias") + theme(axis.text=element_text(size=10), panel.background = element_rect(fill = "white"))

grid.arrange(receptive_pulls_opened, receptive_pulls_closed, receptive_pulls_merged, ncol=3)
grid.arrange(receptive_commits, receptive_stars, receptive_forks, ncol=3)
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
# Newcomers x Opened pull requests
wilcox.test(receptive$newcomers_mean, receptive$pull_opened_mean)
cliff.delta(receptive$newcomers_mean, receptive$pull_opened_mean)
# Newcomers x Closed pull requests
wilcox.test(receptive$newcomers_mean, receptive$pull_closed_mean)
cliff.delta(receptive$newcomers_mean, receptive$pull_closed_mean)
# Newcomers x Merged pull requests
wilcox.test(receptive$newcomers_mean, receptive$pull_merged_mean)
cliff.delta(receptive$newcomers_mean, receptive$pull_merged_mean)
# Newcomers x Commits
wilcox.test(receptive$newcomers_mean, receptive$commits_mean)
cliff.delta(receptive$newcomers_mean, receptive$commits_mean)
# Newcomers x Stars
wilcox.test(receptive$newcomers_mean, receptive$stars_mean)
cliff.delta(receptive$newcomers_mean, receptive$stars_mean)
# Newcomers x Forks
wilcox.test(receptive$newcomers_mean, receptive$forks_mean)
cliff.delta(receptive$newcomers_mean, receptive$forks_mean)

# Calculating MWW and Effect Size for nonreceptive data
# Newcomers x Open pull requests
wilcox.test(nonreceptive$newcomers_mean, nonreceptive$pull_opened_mean)
cliff.delta(nonreceptive$newcomers_mean, nonreceptive$pull_opened_mean)
# Newcomers x Closed pull requests
wilcox.test(nonreceptive$newcomers_mean, nonreceptive$pull_closed_mean)
cliff.delta(nonreceptive$newcomers_mean, nonreceptive$pull_closed_mean)
# Newcomers x Merged pull requests
wilcox.test(nonreceptive$newcomers_mean, nonreceptive$pull_merged_mean)
cliff.delta(nonreceptive$newcomers_mean, nonreceptive$pull_merged_mean)
# Newcomers x Commits
wilcox.test(nonreceptive$newcomers_mean, nonreceptive$commits_mean)
cliff.delta(nonreceptive$newcomers_mean, nonreceptive$commits_mean)
# Newcomers x Stars
wilcox.test(nonreceptive$newcomers_mean, nonreceptive$stars_mean)
cliff.delta(nonreceptive$newcomers_mean, nonreceptive$stars_mean)
# Newcomers x Forks
wilcox.test(nonreceptive$newcomers_mean, nonreceptive$forks_mean)
cliff.delta(nonreceptive$newcomers_mean, nonreceptive$forks_mean)

# Has readme / Hasn't readme (Receptive), Has Readme / Hasn't readme (Nonreceptive)
readme.df = matrix(c(sum(receptive$has_readme == 1), sum(receptive$has_readme == 0), sum(nonreceptive$has_readme == 1), sum(nonreceptive$has_readme == 0)), nrow = 2, ncol=2)
fisher.test(readme.df)
