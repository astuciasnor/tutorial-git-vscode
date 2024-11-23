library(tidyverse)
x <- -10:10
y <- x^2

df <- tibble(x, y)
df

df |> ggplot(aes(x, y)) + geom_point()