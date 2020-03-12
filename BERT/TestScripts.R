library(tidyverse)
library(stringr)

setwd("~/gensim-data")

vec1 = read.table("bertWordVectors1.txt", sep=",")
vec1$V1 = str_replace(vec1$V1, "^\\[", "")
vec1$V3 = str_trim(vec1$V3)
vec1$V4 = str_replace(vec1$V4, "\\s\\[", "")
vec1$V771 = str_replace(vec1$V771, "\\]+$", "")
vec1$V771 = as.numeric(vec1$V771)
vec1$V1 = as.numeric(vec1$V1)
vec1$V2 = as.numeric(vec1$V2)
vec1$V3 = as.character(vec1$V3)

glimpse(vec1)

vec1_ = vec1 %>% filter(V3 == "few")

setwd("~/Google Drive/EBAC_G/NLP_Project/Embeddings/content")
text1 = read_delim("Annotated_Transcripts1.txt", delim = "|", col_names = FALSE)
text1 = text1[c(1,4)]
text1 = text1 %>% rownames_to_column()
text1$rowname = as.numeric(text1$rowname)
text1$rowname = text1$rowname -1 # Change to start from "0"

text1_ = text1 %>% filter(str_detect(text1$X1, "few"))

text1_sim = left_join(text1_, vec1_, by = c("rowname" = "V1" ), keep = FALSE)


## the cosine measure for all document vectors of a matrix
vec_long = text1_sim[c(-2,-3,-4,-5)]
vec_long = vec_long %>% column_to_rownames(var = "rowname")
vec_long = data.table::transpose(vec_long)

colnames(vec_long)[1:6] = text1_sim$rowname
matrix = sapply(vec_long, as.numeric)

glimpse(vec_long_)

#matrix = cbind(vec1,vec2, vec3)
library(lsa)
cosine(matrix)

