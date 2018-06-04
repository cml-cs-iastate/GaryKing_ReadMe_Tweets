setwd("C:/Users/xapponi/Documents/R/win-library/3.5/ReadMe/demofiles")
oldwd <- getwd()
setwd(system.file("demofiles/tweets", package="ReadMe"))
library(ReadMe)
library(quadprog)

undergrad.results <- undergrad(sep=",")
undergrad.preproccess <- preprocess(undergrad.results)
readme.results <- readme(undergrad.preproccess)

true <- readme.results$true.CSMF
estimate <- readme.results$est.CSMF
comb <- data.frame(cbind(true,estimate))
comb$truemin <- comb$true - comb$estimate

setwd(oldwd)

show(comb)

setwd("C:/Users/xapponi/Documents/Research\ Assistant/GaryKing_ReadMe")
write.csv(comb, file=("data_1.csv")
