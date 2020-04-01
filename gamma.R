#!/usr/bin/Rscripts

a <- c(0.1, 0.5, 1, 2, 5, 10,  100)
b <- c(0.1, 0.5, 1, 2, 5, 10,  100)
n <- 10000

count <- 0
amt <- length(a) * length(b)
while (count <= amt)
{
    for (i in a)
    {
        for (j in b)
        {
            count = count + 1
            x <- rgamma(n, i, j)
            assign(paste0("rgamma", count), x)
        }
    }
}
print(mean(rgamma1))
print(var(rgamma1))
