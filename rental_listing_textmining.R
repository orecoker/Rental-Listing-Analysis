# Text Mining for Rental Listing Data
library(tm)
library(lsa)
library(caret)
library(wordcloud)
library(SentimentAnalysis)

# Read data in from edited data
airbnb<-read.csv("airbnb_cleaned.csv")
corp <- Corpus(VectorSource(airbnb$house_rules))

# Text preprocessing: remove punctuation, white-space, numbers, stopwords
corp <- tm_map(corp, stripWhitespace) 
corp <- tm_map(corp, removePunctuation) 
corp <- tm_map(corp, removeNumbers) 
corp <- tm_map(corp, removeWords, stopwords("english"))
## Stemming
corp <- tm_map(corp, stemDocument) 

# TF-IDF: Identify words of importance
tdm <- TermDocumentMatrix(corp)
inspect(tdm)
tfidf <- weightTfIdf(tdm)

# Term Document Matrix: Count the terms
termcount <-apply(tdm,1,sum)

# Generate a wordcloud
wordcloud(names(termcount),termcount, min.freq = 300, colors=brewer.pal(8, "Dark2"))

# Sentiment Analysis
sentiment <- analyzeSentiment(corp)

## Visualize
hist(sentiment$SentimentQDAP, main='Overall Sentiment',xlab="Sentiment Score")



