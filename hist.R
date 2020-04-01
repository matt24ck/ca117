#!/usr/bin/Rscripts

a <- c(0.1, 0.5, 1, 2, 5, 10,  100)
b <- c(0.1, 0.5, 1, 2, 5, 10,  100)
n <- 10000

pdf(file="practical_part_2_output.pdf", width=200, height=150)
par(mfrow=c(7, 7))

count <- 0
for (i in a)
{
    for (j in b)
    {
        x <- rgamma(n, i, j)
        hist(x,breaks=100)
        #count = count + 1
    }
}
dev.off()
#print(count)
