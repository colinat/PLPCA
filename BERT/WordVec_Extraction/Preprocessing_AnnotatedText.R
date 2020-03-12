library(tidyverse)

text <- read_csv("Annotated_text_combined_utf8.csv")

glimpse(text)

text$annotation = str_c(text$Aspects, text$Sentiment, text$`Emotional Sentiment`,
                        sep = " ")

text$annotation = str_replace(text$annotation, "NIL ", "")
text$annotation = str_replace(text$annotation, " NIL", "")
text$annotation = str_replace(text$annotation, "not_applicable ", "")

# Combine Transcript with Annotation with a delimiter " ||| "
text$sentences = str_c(text$mydata, text$annotation, sep = " ||| ")

Annotated_Transcripts = tibble(text$sentences)

write.table(Annotated_Transcripts, file = "Annotated_Transcripts.txt", 
            sep = "", quote = FALSE, eol = "\n",
            row.names = FALSE, col.names = FALSE)

Annotated_Transcripts1 = Annotated_Transcripts[1:1000,]
write.table(Annotated_Transcripts1, file = "Annotated_Transcripts1.txt", 
            sep = "", quote = FALSE, eol = "\n",
            row.names = FALSE, col.names = FALSE)

Annotated_Transcripts2 = Annotated_Transcripts[1001:2000,]
write.table(Annotated_Transcripts2, file = "Annotated_Transcripts2.txt", 
            sep = "", quote = FALSE, eol = "\n",
            row.names = FALSE, col.names = FALSE)

Annotated_Transcripts3 = Annotated_Transcripts[2001:3000,]
write.table(Annotated_Transcripts3, file = "Annotated_Transcripts3.txt", 
            sep = "", quote = FALSE, eol = "\n",
            row.names = FALSE, col.names = FALSE)


Annotated_Transcripts4 = Annotated_Transcripts[3001:4000,]
write.table(Annotated_Transcripts4, file = "Annotated_Transcripts4.txt", 
            sep = "", quote = FALSE, eol = "\n",
            row.names = FALSE, col.names = FALSE)


Annotated_Transcripts5 = Annotated_Transcripts[4001:5000,]
write.table(Annotated_Transcripts5, file = "Annotated_Transcripts5.txt", 
            sep = "", quote = FALSE, eol = "\n",
            row.names = FALSE, col.names = FALSE)


Annotated_Transcripts6 = Annotated_Transcripts[5001:6000,]
write.table(Annotated_Transcripts6, file = "Annotated_Transcripts6.txt", 
            sep = "", quote = FALSE, eol = "\n",
            row.names = FALSE, col.names = FALSE)


Annotated_Transcripts7 = Annotated_Transcripts[6001:6697,]
write.table(Annotated_Transcripts7, file = "Annotated_Transcripts7.txt", 
            sep = "", quote = FALSE, eol = "\n",
            row.names = FALSE, col.names = FALSE)



library(stringr)
max(str_count(Annotated_Transcripts, "\\S+"))

#----------------------------------------------------------------------------#

data = read.table("bertWordVectors.txt", sep =",")











