#install.packages('rsconnect')
#rsconnect::setAccountInfo(name='nelsonljs', token='F72CC8AF77392083ACC8DD349F12289D', secret='cSWNeJd1d0trSXcFiA9L0Pmhj6vXfmGp7qyQi4Xc')
#to deploy the app
#library(rsconnect)
#deployApp()
#terminateApp()

# setwd(dirname(rstudioapi::getActiveDocumentContext()$path))
library(dplyr)
library(shiny)
library(shinyjs)
library(stringr)
library(RSQLite)
library(DT)

# mydbconn = dbConnect(RSQLite::SQLite(), "healthcare.db")
# query = paste0("SELECT * FROM infotable")
# annotate_text = dbGetQuery(mydbconn, query)

updatedb = function(my_inputs, rvs) {
  rvs$annotate_text[rvs$mytext[1],"Aspects"] = paste(my_inputs$aspect1, collapse = ', ')
  rvs$annotate_text[rvs$mytext[1],"Sentiment"] = my_inputs$sentiment1
  rvs$annotate_text[rvs$mytext[1],"Emotional Sentiment"] = my_inputs$e_sentiment1
  
  rvs$annotate_text[rvs$mytext[2],"Aspects"] = paste(my_inputs$aspect2, collapse = ', ')
  rvs$annotate_text[rvs$mytext[2],"Sentiment"] = my_inputs$sentiment2
  rvs$annotate_text[rvs$mytext[2],"Emotional Sentiment"] = my_inputs$e_sentiment2
  
  rvs$annotate_text[rvs$mytext[3],"Aspects"] = paste(my_inputs$aspect3, collapse = ', ')
  rvs$annotate_text[rvs$mytext[3],"Sentiment"] = my_inputs$sentiment3
  rvs$annotate_text[rvs$mytext[3],"Emotional Sentiment"] = my_inputs$e_sentiment3
  
  rvs$annotate_text[rvs$mytext[4],"Aspects"] = paste(my_inputs$aspect4, collapse = ', ')
  rvs$annotate_text[rvs$mytext[4],"Sentiment"] = my_inputs$sentiment4
  rvs$annotate_text[rvs$mytext[4],"Emotional Sentiment"] = my_inputs$e_sentiment4
  
  rvs$annotate_text[rvs$mytext[5],"Aspects"] = paste(my_inputs$aspect5, collapse = ', ')
  rvs$annotate_text[rvs$mytext[5],"Sentiment"] = my_inputs$sentiment5
  rvs$annotate_text[rvs$mytext[5],"Emotional Sentiment"] = my_inputs$e_sentiment5
  
  mydbconn = dbConnect(RSQLite::SQLite(), my_inputs$db)
  dbWriteTable(mydbconn, "infotable", rvs$annotate_text, overwrite = TRUE)
  dbDisconnect(mydbconn)
}

function(input, output, session) {
  rvs = reactiveValues(selection1 = NA,
                       mytext = c(1:5),
                       annotate_text = data.frame(mydata = character(0),
                                                  Aspects = character(0),
                                                  Sentiment = character(0),
                                                  "Emotional Sentiment" = character(0)))
  
  observeEvent(input$LoadDB, {
    mydbconn = dbConnect(RSQLite::SQLite(), input$db)
    rvs$annotate_text = dbGetQuery(mydbconn, "SELECT * FROM infotable")
    rvs$mytext = sample(which(is.na(rvs$annotate_text$Aspects)),5)
    enable("Update")
    enable("Refresh")
    enable("Review")
    dbDisconnect(mydbconn)
    disable("LoadDB")
    disable("db")
  })
  
  observeEvent(input$Update, {
    updatedb(input, rvs)
    reset("text-panel")
    
    rvs$mytext = sample(which(is.na(rvs$annotate_text$Aspects)),5)
  })
  
  observeEvent(input$Refresh, {
    rvs$mytext = sample(which(is.na(rvs$annotate_text$Aspects)),5)
  })
  
  observeEvent(input$Review, {
    if (length(which(!is.na(rvs$annotate_text$Aspects)))<5) {
      showNotification("Nothing is labelled yet.")
      rvs$mytext = sample(c(1:1000),5)
    } else {
      rvs$mytext = sample(which(!is.na(rvs$annotate_text$Aspects)),5)
    }

    updateSelectizeInput(session, "aspect1", selected = str_split(rvs$annotate_text[rvs$mytext[1],"Aspects"], ",")[[1]])
    updateSelectInput(session, "sentiment1", selected = rvs$annotate_text[rvs$mytext[1],"Sentiment"])
    updateSelectInput(session, "e_sentiment1", selected = rvs$annotate_text[rvs$mytext[1],"Emotional Sentiment"])
    
    updateSelectizeInput(session, "aspect2", selected = str_split(rvs$annotate_text[rvs$mytext[2],"Aspects"], ",")[[1]])
    updateSelectInput(session, "sentiment2", selected = rvs$annotate_text[rvs$mytext[2],"Sentiment"])
    updateSelectInput(session, "e_sentiment2", selected = rvs$annotate_text[rvs$mytext[2],"Emotional Sentiment"])
    
    updateSelectizeInput(session, "aspect3", selected = str_split(rvs$annotate_text[rvs$mytext[3],"Aspects"], ",")[[1]])
    updateSelectInput(session, "sentiment3", selected = rvs$annotate_text[rvs$mytext[3],"Sentiment"])
    updateSelectInput(session, "e_sentiment3", selected = rvs$annotate_text[rvs$mytext[3],"Emotional Sentiment"])
    
    updateSelectizeInput(session, "aspect4", selected = str_split(rvs$annotate_text[rvs$mytext[4],"Aspects"], ",")[[1]])
    updateSelectInput(session, "sentiment4", selected = rvs$annotate_text[rvs$mytext[4],"Sentiment"])
    updateSelectInput(session, "e_sentiment4", selected = rvs$annotate_text[rvs$mytext[4],"Emotional Sentiment"])
    
    updateSelectizeInput(session, "aspect5", selected = str_split(rvs$annotate_text[rvs$mytext[5],"Aspects"], ",")[[1]])
    updateSelectInput(session, "sentiment5", selected = rvs$annotate_text[rvs$mytext[5],"Sentiment"])
    updateSelectInput(session, "e_sentiment5", selected = rvs$annotate_text[rvs$mytext[5],"Emotional Sentiment"])
  })
  
  output$line1 = renderText({rvs$annotate_text$mydata[rvs$mytext[1]]})
  output$line2 = renderText({rvs$annotate_text$mydata[rvs$mytext[2]]})
  output$line3 = renderText({rvs$annotate_text$mydata[rvs$mytext[3]]})
  output$line4 = renderText({rvs$annotate_text$mydata[rvs$mytext[4]]})
  output$line5 = renderText({rvs$annotate_text$mydata[rvs$mytext[5]]})
  
  output$sampletable = DT::renderDataTable(rvs$annotate_text[rvs$mytext,], options = list(dom = 't'))
  
  session$onSessionEnded(function() {
    # dbDisconnect(mydbconn)
    print('Hello, the session has ended')
  })
}