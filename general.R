# Author: Felipe Fronchetti
# Questions? fronchettiemail@gmail.com

require("effsize")
library(ggplot2)
install.packages('plyr')
install.packages('xtable')
library("xtable")
# Define your own working directory
setwd("/var/www/html/TCC-UTFPR")

# Reading files
general <- read.csv("data_general.csv")

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
#          CHARTS 
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

# Contributors per language 
# Perl
summary(subset(general, Language == "Perl", select=c(Contributors))$Contributors)
sd(subset(general, Language == "Perl", select=c(Contributors))$Contributors)
# Clojure
summary(subset(general, Language == "Clojure", select=c(Contributors))$Contributors)
sd(subset(general, Language == "Clojure", select=c(Contributors))$Contributors)
# Erlang
summary(subset(general, Language == "Erlang", select=c(Contributors))$Contributors)
sd(subset(general, Language == "Erlang", select=c(Contributors))$Contributors)
# Objective-C
summary(subset(general, Language == "Objective-C", select=c(Contributors))$Contributors)
sd(subset(general, Language == "Objective-C", select=c(Contributors))$Contributors)
# Haskell
summary(subset(general, Language == "Haskell", select=c(Contributors))$Contributors)
sd(subset(general, Language == "Haskell", select=c(Contributors))$Contributors)
# CoffeeScript
summary(subset(general, Language == "CoffeeScript", select=c(Contributors))$Contributors)
sd(subset(general, Language == "CoffeeScript", select=c(Contributors))$Contributors)
# Java
summary(subset(general, Language == "Java", select=c(Contributors))$Contributors)
sd(subset(general, Language == "Java", select=c(Contributors))$Contributors)
# Scala
summary(subset(general, Language == "Scala", select=c(Contributors))$Contributors)
sd(subset(general, Language == "Scala", select=c(Contributors))$Contributors)
# TypeScript
summary(subset(general, Language == "TypeScript", select=c(Contributors))$Contributors)
sd(subset(general, Language == "TypeScript", select=c(Contributors))$Contributors)
# PHP
summary(subset(general, Language == "PHP", select=c(Contributors))$Contributors)
sd(subset(general, Language == "PHP", select=c(Contributors))$Contributors)
# Go
summary(subset(general, Language == "Go", select=c(Contributors))$Contributors)
sd(subset(general, Language == "Go", select=c(Contributors))$Contributors)
# Python
summary(subset(general, Language == "Python", select=c(Contributors))$Contributors)
sd(subset(general, Language == "Python", select=c(Contributors))$Contributors)
# JavaScript
summary(subset(general, Language == "JavaScript", select=c(Contributors))$Contributors)
sd(subset(general, Language == "JavaScript", select=c(Contributors))$Contributors)
# C
summary(subset(general, Language == "C", select=c(Contributors))$Contributors)
sd(subset(general, Language == "C", select=c(Contributors))$Contributors)
# Ruby
summary(subset(general, Language == "Ruby", select=c(Contributors))$Contributors)
sd(subset(general, Language == "Ruby", select=c(Contributors))$Contributors)

barplot(languagens_mean,beside=T, horiz = TRUE, space = 0.25, border = TRUE, xlim = c(0,1000), xlab = "", names.arg = c("Perl", "Clojure", "Erlang", "Objective-C", "Haskell", "CoffeeScript", "Java", "Scala", "TypeScript", "PHP", "Go", "Python", "JavaScript", "C", "Ruby"), las=1,  cex.names=0.7, cex.axis = 0.75)
title(xlab = "# Contribuidores", line = 2, cex.lab = 0.7)

# Boxplots: Stars, Age, Contributors, Contributions, Pull requests and Forks
boxplot(general$Stars, outline=FALSE, ylab="# Estrelas", cex.lab=1.2, cex.axis=1.1)
boxplot(general$Age, outline=FALSE, ylab="# Idade (Anos)", cex.lab=1.2, cex.axis=1.1)
boxplot(general$Contributors, outline=FALSE, ylab="# Contribuidores", cex.lab=1.2, cex.axis=1.1)
boxplot(general$Contributions, outline=FALSE, ylab="# Contribuições", cex.lab=1.2, cex.axis=1.1)
boxplot(general$Total_pulls, outline=FALSE, ylab="# Requisições", cex.lab=1.2, cex.axis=1.1)
boxplot(general$Forks, outline=FALSE, ylab="# Cópias", cex.lab=1.2, cex.axis=1.1)

