# Author: Felipe Fronchetti
# Questions? fronchettiemail@gmail.com

require("effsize")

# Define your own working directory
setwd("/var/www/html/TCC-UTFPR")

# Reading files
receptive <- read.csv("data_receptive.csv")
nonreceptive <- read.csv("data_nonreceptive.csv")

# Calculating MWW and Effect Size for receptive data
# Newcomers x Open pull requests
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

# Scatterplots
# Violin Plot: De um lado receptivos, do outro não receptivos, pra cada métrica
plot(receptive$commits_mean, receptive$newcomers_mean, xlab="Requisições abertas por mês", ylab="Novatos distribuídos por semana")
plot(nonreceptive$commits_mean, nonreceptive$newcomers_mean, xlab="Requisições abertas por mês", ylab="Novatos distribuídos por semana")
