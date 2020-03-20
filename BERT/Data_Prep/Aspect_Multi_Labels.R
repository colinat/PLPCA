library(tidyverse)

text <- read_csv("Annotated_text_combined_utf8.csv")

glimpse(text)

Aspect = text[c("mydata", "Aspects")]
  
table(Aspect$Aspects)

Aspect = Aspect %>% 
  mutate(sales=0, earnings=0, op_costs=0, 
         products_services=0, organic_expansion=0,
         acquisitions=0, competition=0,
         op_risks=0, debt=0, not_applicable=0, NIL=0)

Aspect$sales = str_detect(Aspect$Aspects, "sales")
Aspect$earnings = str_detect(Aspect$Aspects, "earnings")
Aspect$op_costs = str_detect(Aspect$Aspects, "op_costs")
Aspect$products_services = str_detect(Aspect$Aspects, "products_services")
Aspect$organic_expansion = str_detect(Aspect$Aspects, "organic_expansion")
Aspect$acquisitions = str_detect(Aspect$Aspects, "acquisitions")
Aspect$competition = str_detect(Aspect$Aspects, "competition")
Aspect$op_risks = str_detect(Aspect$Aspects, "op_risks")
Aspect$debt = str_detect(Aspect$Aspects, "debt")
Aspect$not_applicable = str_detect(Aspect$Aspects, "not_applicable")
Aspect$NIL = str_detect(Aspect$Aspects, "NIL")

glimpse(Aspect)

Aspect[3:13] <- lapply(Aspect[3:13], function(x) as.numeric(x))

colnames(Aspect) = c('text', 'Label', 'Label_f')

write.csv(Aspect2, "Aspect.csv", row.names = FALSE)







