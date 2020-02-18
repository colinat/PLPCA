##### Load the db you want to work with.
mydbs = list.files(pattern = "\\.db$")

aspects = readLines("Aspects.txt")
emotions = readLines("Sentiments.txt")

fluidPage(theme = "bootstrap.css",
  
  titlePanel("Annotation helper"),
  br(),
  br(),

  fluidRow(
    useShinyjs(),
    id = "text-panel",
    column(9,
           h3(print("Please update your annotations here.")),
           wellPanel(
             fluidRow(
               column(6,
                      wellPanel(span(textOutput("line1"), style="color:red; font-size: 12px;"))),
               column(2,
                      selectizeInput("aspect1","Aspect", aspects, multiple = TRUE)),
               column(2,
                      selectInput("sentiment1","Sentiment", c("Neutral","Positive","Negative"))),
               column(2,
                      selectInput("e_sentiment1","Emotional Sentiment", emotions))
               ),
             fluidRow(
               column(6,
                      wellPanel(span(textOutput("line2"), style="color:red; font-size: 12px;"))),
               column(2,
                      selectizeInput("aspect2","Aspect", aspects, multiple = TRUE)),
               column(2,
                      selectInput("sentiment2","Sentiment", c("Neutral","Positive","Negative"))),
               column(2,
                      selectInput("e_sentiment2","Emotional Sentiment", emotions))
             ),
             fluidRow(
               column(6,
                      wellPanel(span(textOutput("line3"), style="color:red; font-size: 12px;"))),
               column(2,
                      selectizeInput("aspect3","Aspect", aspects, multiple = TRUE)),
               column(2,
                      selectInput("sentiment3","Sentiment", c("Neutral","Positive","Negative"))),
               column(2,
                      selectInput("e_sentiment3","Emotional Sentiment", emotions))
             ),
             fluidRow(
               column(6,
                      wellPanel(span(textOutput("line4"), style="color:red; font-size: 12px;"))),
               column(2,
                      selectizeInput("aspect4","Aspect", aspects, multiple = TRUE)),
               column(2,
                      selectInput("sentiment4","Sentiment", c("Neutral","Positive","Negative"))),
               column(2,
                      selectInput("e_sentiment4","Emotional Sentiment", emotions))
             ),
             fluidRow(
               column(6,
                      wellPanel(span(textOutput("line5"), style="color:red; font-size: 12px;"))),
               column(2,
                      selectizeInput("aspect5","Aspect", aspects, multiple = TRUE)),
               column(2,
                      selectInput("sentiment5","Sentiment", c("Neutral","Positive","Negative"))),
               column(2,
                      selectInput("e_sentiment5","Emotional Sentiment", emotions))
             )
           )),
    column(3,
           h3(print("Control Panel")),
           wellPanel(
             selectInput("db","Select db to work with", mydbs),
             actionButton("LoadDB", "Load selected database", 
                          style="color:#000000; width:100%; white-space:normal; font-size:14px; ",
                          class = "btn btn-warning")
           ),
           wellPanel(
             disabled(actionButton("Update", "Update Annotations", 
                          style="color:#000000; width:100%; white-space:normal; font-size:14px; ",
                          class = "btn btn-success")),
             br(),
             br(),
             
             disabled(actionButton("Refresh", "Refresh Lines (Without Update)", 
                          style="color:#000000; width:100%; white-space:normal; font-size:14px; ")),
             br(),
             br(),
             
             disabled(actionButton("Review", "Review Previous Annotations", 
                                   style="color:#000000; width:100%; white-space:normal; font-size:14px; ",
                                   class = "btn btn-info"))
           ))
  ),
  fluidRow(
    column(4,
           plotOutput("completion", width = "100%", height = "400px")),
    column(4,
           plotOutput("sentiment_count", width = "100%", height = "400px")),
    column(4,
           plotOutput("e_sentiment_count", width = "100%", height = "400px"))
           
  )
)
