
#Source: https://rdrr.io/github/jonathanbratt/RBERT/man/extract_features.html
#https://rdrr.io/github/jonathanbratt/RBERT/src/R/extract_features.R
# https://github.com/jonathanbratt/RBERT/

install.packages("remotes")
remotes::install_github("jonathanbratt/RBERT")

#install.packages("devtools")
devtools::install_github(
  "jonathanbratt/RBERT", 
  build_vignettes = TRUE
)

devtools::install_github("rstudio/reticulate")

reticulate::install_miniconda()

# RBERT requires TensorFlow. Currently the version must be <= 1.13.1. 
# You can install it using the tensorflow package

tensorflow::install_tensorflow(version = "1.13.1")

library(tidyverse)
library(RBERT)
library(tensorflow)




examples <- c("I saw the branch on the bank.",
              "Pick up the branch from the bank.")
# Total 10 Tokens including [CLS] and [SEP] and punctuation

# Method 1: Specify the BERT Pre-trained Model
feats <- extract_features(
  examples = examples,
  model = "bert_base_uncased")

# Method 2: Download the BERT model and specify the folder where it is saved
BERT_PRETRAINED_DIR <- download_BERT_checkpoint("bert_base_uncased")

BERT_PRETRAINED_DIR

feats2 <- extract_features(
  examples = examples,
  ckpt_dir = BERT_PRETRAINED_DIR)


# Method 3: Use Fine-tuned BERT Model






# Extract the embeddings
df = feats$output

# There are 4 hidden layers index 9 to 12 containing the word embeddings
# creating the word vectors by summing together the last four layers.
# http://mccormickml.com/2019/05/14/BERT-word-embeddings-tutorial/
# Target Embedding shape is: No. of Tokens (10) x Fixed Number of hidden units (768)
glimpse(df)

df1 = df %>% 
    group_by(sequence_index, token_index, token) %>%
    summarise_all(.funs = sum) %>%
    select(-layer_index, -segment_index)
  





