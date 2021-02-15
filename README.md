# Stock News Sentiment
This project aims to predict if the stock price of a company will increase or decrease based on top news headlines

# Overview

- Two datasets: one is the Top News dataset and the other is Dow Jones Industrial Average Stock Prices dataset obtained from Kaggle.
- Combined the datasets and splitting them into training (from 2008-08-08 to 2014-12-31) and the test set (from 2015-01-02 to 2016-07-01) which is approximately 80% to 20% split. 


# References

**Python Version:** 3.8</br>
**Packages:** numpy, pandas, seaborn, matplotlib, VaderSentiment, TextBlob</br>
**Dataset:** [Daily News for Stock Market Predictions](https://www.kaggle.com/aaron7sun/stocknews) obtained from Kaggle </br>
**Dow Jones Stock Market News and Data:** [Dow Jones Industrial Average](https://au.finance.yahoo.com/quote/%5EDJI?p=%5EDJI&.tsrc=fin-srch)</br>
**Stock Prices Article** [What Is the Significance of a Closing Price on a Stock?](https://finance.zacks.com/significance-closing-price-stock-3007.html)</br>
**VaderSentiment Article:** [VaderSentiment Article](https://towardsdatascience.com/sentimental-analysis-using-vader-a3415fef7664)</br>
**Sentiment Analysis Article** [Subjectivity and Polarity](https://www.analyticsvidhya.com/blog/2018/02/natural-language-processing-for-beginners-using-textblob/)</br>
**Linear Discriminant Analysis for Stocks:** [Stock Market Movement Prediction using LDA](https://ieeexplore.ieee.org/document/8441038)</br>
**Text Normalization Article:** [NLP Essentials](https://www.analyticsvidhya.com/blog/2019/08/how-to-remove-stopwords-text-normalization-nltk-spacy-gensim-python/)</br>



# Data Cleaning

- Two of the datasets are mainly used: </br>
  - Top News dataset which consists of 1989 rows and 27 columns;
  - Dow Jones Industrial Average Stock Prices dataset which has 1989 rows and 7 columns.
- Combined and cleaned all texts from all 24 columns of the top news headlines and place it as a new feature. 
- Two functions were created to obtain the Subjectivity (i.e. 0 to 1) and Polarity (i.e. -1 to 1) of the text sentiment.
- These functions are to classify text as positive or negative and determining how subjective it is
- Using SentimentIntensityAnalyzer, created new features of 


# Exploratory Data Analysis

- Looked at the overall **Closing Price** for the Dow Jones Industrial Average Stock Price from 2008-2016.</br>
  - Closing Price is the considered to be more signficant as investors, traders, financial institutions, regulators and other stakeholders use it as a reference point for determining performance over a specific time.
  
![](https://github.com/roywong96/stocknewsSentiment/blob/master/images/DJprices.png)
![](https://github.com/roywong96/stocknewsSentiment/blob/master/images/label.png)


# Model Building


# Model Performance


