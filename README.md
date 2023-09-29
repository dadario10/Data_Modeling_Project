# Selective Stock Market Price Spanning COVID-19 Global Pandemic Predictions vs. Actuality 

## Table of Contents 
* [Overview](#overview)
* [Purpose](#purpose)
* [Technologies](#technologies)
* [Data](#data)
* [Models](#models)
* [Visualization](#visualization) 
* [Challenges](#challenges)
* [Summary](#summary)
* [Resources](#resources)
* [Team Members](#team-members)

## Overview 
In this project we created predictive models to predict the 'bounce-back' for Amazon, Netfix and Nikola stock prices.  We compared the predictive models to the actual data for the same time period.  

## Purpose
The purpose of our study is to:
* Extract, clean and pre-process data for models. 
* Build multiple machine learning models to predict selective stock market stocks spanning COVID-19 global pandemic and predict the 'bounce back' of the stock vs. actual performance of the selective stocks. 
* Compare each of the machine learning predictive models to the actual performance of the selected stocks. 
* Use a Tableau HTML, to visualize models' prediction.

## Technologies 
* Python & Pandas
* Jupyter Notebook 
* Visual Studio
* MySql Database 
* xGBoost 

## Data
### Data Source

Three stocks were chosen; Amazon, Netflix and Nikola.  All three stocks are listed on the NASDAX Stock Exchange.  The data was gathered from Yahoo Finance:

* [Amazon](https://ca.finance.yahoo.com/quote/AMZN?p=AMZN&.tsrc=fin-srch)
* [Netflix](https://ca.finance.yahoo.com/quote/NFLX?p=NFLX&.tsrc=fin-srch)
* [Nikola](https://ca.finance.yahoo.com/quote/NKLA?p=NKLA&.tsrc=fin-srch)

### Data Cleaning 
The data was downloaded from the above links as .csv files.  These .csv files were imported into a MySQL Database. 
![](images/MySQL_ERD.PNG)
</br>
The data for each stock was then extracted and converted into a Panda DataFrame.
</br>
</br>
![](images/Amazon_df.png)
</br>
Fig 1 - Amazon DataFrame
</br>
</br>
![](images/Netflix_df.png)
</br>
Fig 2 - Netflix DataFrame
</br>
</br>
![](images/Nikola_df.png)
</br>
Fig 3 - Nikola DataFrame
</br>
</br>

## Models 
The models that we used were:
* Arima
* XGBoost
* Artificial Neural Network for Regression

## Visualization
To visualize our data and predictions, we used the following:

* [Tableau Stock Visualizations Project 4](https://public.tableau.com/app/profile/dario.micucci/viz/StockVisualizationsProject4/VolumeDashboard?publish=yes)
* Matplot


## Challenges
The challenges that we experienced were:

* Model selections
* Complexity and shape of the data
* Limited experience with level of models
* More advanced engineered features required

## Summary 
The question our team set out to answer was the continued impact of COVID-19 on stock market performance.

**Amazon:** The stocks took a steady rise during and following COVID. After a market correction, Amazon has continued increasing.
- 2018-2020: The stock experienced fluctuations because of its strong performance in e-commerce  and cloud computing. 
- 2020-2023: The company’s stock skyrocketed in 2020 and 2021 as e-comm boomed during the pandemic. However, the company is facing growing pressure to prove that they can sustain the growth they enjoyed during the pandemic, as the economy reopens, and consumers head back to physical stores.
  
**Netflix:** There was a positive linear correlation to the Netflix stocks (increasing), and COVID-19 only enhanced this correlation. Since the pandemic, the stocks have steadily decreased for what we theorize to be bad business decisions. An example of this is Netflix’s decision to crackdown on password sharing. This has caused subscribers to leave the service.
- 2018-2020: Netflix’s stock price was already strong, with share prices climbing steadily.
- 2020-2023: COVID led to a surge in demand for streaming services as more people were forced to stay home. Netflix benefited from this trend, and its stock reached new highs. Analysts expect Netflix's stock to continue increasing in 2023 and 2024.



**Nikola:** From 2018 to 2020, these stocks were not performing well (they were flat lined). During COVID-19 however, there was an unprecedented and sharp increase, especially around September 2020. It’s interesting to note that the stocks took a significant dive again and they haven’t been able to progress from this position. 
- 2018-2020: The company was still in its early stages and its stock was not publicly traded under its formal NKLA ticker until a merger with VectoIQ Corp in 2020.
- 2020-2023: Following the merger and increased investor interest, Nikola’s stock price surged in the first half of 2020 – which was during COVID. The company faced controversy about its technology and business practices, leading to a sharp decline in the stock price. It has since continued to face volatility and skepticism from investors and analysts alike, hence its decline.

## Conclusion
Each Model we used all had their benefits and detractors. In short, the type of data that you use, also dictates the model that you use.

## Resources
The following resources were leveraged in this project:

* Yahoo Finance
* Tutors
* Kaggle
* MySql
* Tableau

## Team Members
* <a href="https://github.com/dadario10"> Dario Micucci</a>
* <a href="https://github.com/bchaudang"> Brett Chau-dang </a>
* <a href="https://github.com/JP-Butler"> Justin Butler </a>
* <a href="https://github.com/RP8844"> Rebeca Perez </a>
* <a href="https://github.com/rbrennan55"> Ron Brennan </a>

-30-
