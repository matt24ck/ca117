#!/usr/bin/Rscripts

library(gridExtra)

set.seed(1337)
a <- c(0.1, 0.5, 1, 2, 5, 10, 100)
b <- c(0.1, 0.5, 1, 2, 5, 10, 100)

n <- 10000

#Question 1

count <- 1
sets <- c()

for (i in a)
{
  for (j in b)
  {
    x <- list(rgamma(n, i, j))
    #assign(paste0("set", count), x)
    sets <- c(sets, x)
    count = count + 1
  }
  
}
#print(var(as.numeric(as.character(unlist(sets[1])))))
#print(mean(as.numeric(as.character(unlist(sets[1])))))

#Question 2

pdf(file="practical_output.pdf", width=200,height=150)
par(mfrow=c(7, 7))

for (set in sets)
{
  hist(set, breaks=100)
}
dev.off()

#Question3

#Make 49 lists with elements theor. var. real var, etc

matrixA <- matrix(data = c("Values", "Sample Mean", "Theoretical Expected Value", "Sample Variance", "Theoretical Variance"), nrow = 1, ncol = 5)

#Testing for one case before I put it in the loop
#matrixB <- rbind(matrixA, c("0.1-0.1", toString(mean(as.numeric(as.character(unlist(sets[1]))))), toString(0.1 / 0.1), toString(var(as.numeric(as.character(unlist(sets[1]))))), toString(0.1 / (0.1 * 0.1))))
#print(matrixB)

count <- 1
while (count <= length(sets))
{
  
  for (k in a)
  {
    for (l in b)
    {
      tmp <- matrixA
      matrixA <- rbind(tmp, c(paste0(toString(k), ",", toString(l)), toString(mean(as.numeric(as.character(unlist(sets[count]))))), toString(k / l), toString(var(as.numeric(as.character(unlist(sets[count]))))), toString(k / (l * l))))
      count = count + 1
    }
  }
  count = count + 1
}
pdf("practical_output3.pdf", height=15, width=10)
matrixA <- as.table(matrixA)

#Testing how the matrix looks
#print(matrixA)


#write.table(matrixA, file="practical_output3.csv", row.names=F, col.names=F, sep=",")
grid.table(matrixA)
dev.off()
