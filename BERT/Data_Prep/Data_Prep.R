library(tidyverse)

text <- read_csv("Annotated_text_combined_utf8.csv")

glimpse(text)

# For Dataset
text$text = str_c(text$mydata, text$Aspects, sep = " ||| ")
text$Label = str_c(text$Sentiment, text$`Emotional Sentiment`, sep = "_")
text$Label = str_replace(text$Label, "NIL", " ")
text$Label = str_replace(text$Label, "not_applicable", " ")
text$Label = str_replace(text$Label, "_ ", "")
table(text$Label, useNA = "always")
text$Label = factor(text$Label)
text$Label_f = as.numeric(text$Label)
text$Label_f = text$Label_f-1 # Start from "0"
table(text$Label_f, text$Label)

Sentiment_Emotion = text[c("text", "Label", "Label_f")]
write.csv(dataset, "Sentiment_Emotion.csv", row.names = FALSE)

#----------------------------------------------------------------------------#

text <- read_csv("Annotated_text_combined_utf8.csv")
Aspect = text[c("mydata", "Aspects")]

table(Aspect$Aspects)

Aspect$Aspects = factor(Aspect$Aspects)
Aspect$Label_f = as.numeric(Aspect$Aspects)
Aspect$Label_f = Aspect$Label_f-1 # Start from "0"

table(Aspect$Label_f)


glimpse(Aspect)
colnames(Aspect) = c('text', 'Label', 'Label_f')

write.csv(Aspect, "Aspect.csv", row.names = FALSE)

#----------------------------------------------------------------------------#

text <- read_csv("Annotated_text_combined_utf8.csv")
Sentiment = text[c("mydata", "Sentiment")]
  
table(Sentiment$Sentiment)

Sentiment$Sentiment = factor(Sentiment$Sentiment)
Sentiment$Label_f = as.numeric(Sentiment$Sentiment)
Sentiment$Label_f = Sentiment$Label_f-1 # Start from "0"

table(Sentiment$Label_f)


glimpse(Sentiment)
colnames(Sentiment) = c('text', 'Label', 'Label_f')

write.csv(Sentiment, "Sentiment.csv", row.names = FALSE)

#----------------------------------------------------------------------------#

text <- read_csv("Annotated_text_combined_utf8.csv")
Emotion = text[c("mydata", "Emotional Sentiment")]
colnames(Emotion) = c('text', 'Label')

table(Emotion$Label)

Emotion$Label = factor(Emotion$Label)
Emotion$Label_f = as.numeric(Emotion$Label)
Emotion$Label_f = Emotion$Label_f-1 # Start from "0"

table(Emotion$Label_f)


glimpse(Emotion)
write.csv(Emotion, "Emotion.csv", row.names = FALSE)




