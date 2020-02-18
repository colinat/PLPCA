library(pacman)

pacman::p_load(dplyr, shiny, shinythemes, shinyjs, DT,
               tidyverse, stringr, RSQLite, rstudioapi)
setwd(dirname(rstudioapi::getActiveDocumentContext()$path))

runApp()