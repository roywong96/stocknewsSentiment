# Stock News Sentiment
This project aims to predict if the stock price of a company will increase or decrease based on top news headlines

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
- Combined and cleaned all texts from all 24 columns of the top news headlines. 
- Two functions were created to obtain the Subjectivity and Polarity of the text sentiment 


# Exploratory Data Analysis

I looked at the overall Closing Price for the Dow Jones Industrial Average Stock Price from 2008-2016. The reason is because the Closing Price is the considered to be more signficant. Usually, investors, traders, financial institutions, regulators and other stakeholders use it as a reference point for determining performance over a specific time






# Feature Engineering

- As mentioned above, new feature is created "Combined_News" where texts from all the top news headlines were cleaned and combined.
- 


# Model Building


# Model Performance


