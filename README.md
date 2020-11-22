# Stock-Price-Forecasting-Using-Optimized-Technical-Indicators-With-Three-Stage-Feature-Selection
This project has focused on predicting the closing prices of stock.Prediction of stock price movement has been made by calculating and selecting effective technical indicators and then applied machine learning models on optimized technical indicator for forecasting the closing price.
## Technologies Used
- Python
- Machine Learning
## Description
Project has been made to predict the closing price of stock, So that a person will know whether to invest or not in that stock.
### About Dataset
Data is collected from a stock marketing site that is YahooFinance . We have focused on Maruti and TCS data of last 12years.In
prepossessing technical indicators are calculated by formulas based on the prices. We have used 41 technical indicators i.e. Accumulation/Distribution Line, Aroon Up, Aroon Down, Average Directional Index (ADX), Average True Range (ATR), Bollinger Band %B, Upper Bollinger Band, Lower Bollinger Band, Chaikin Money Flow (CMF), Commodity Channel Index (CCI), MACD (Moving Average Convergence/Divergence Oscillator), MACD Histogram, Money Flow Index (MFI), On Balance Volume (OBV), Percentage Price Oscillator (PPO), Rate of Change (ROC), Rate of change Percentage, Rate of change Ratio, Relative Strength Index (RSI), Standard Deviation, Williams %R, Awesome Oscillator(AO), Exponential Moving Average(EMA), stochastic K%, stochastic d%,open momentum, close momentum, high momentum, low momentum, Simple Moving Average(SMA), Weighted Moving Average(WMA), Upper price channel, Lower price channel, Triangular Moving Average( TMA), Median price, Previous closing price, Previous high price, Previous low price, Plus
Directional Indicator(+DI), Minus Directional Indicator(-DI). We have taken these indicators by analyzing its importance in literature.
### Methodology
In this we have two stages before forecasting prices. In stage 1, technical indicator are optimized. We used technical indicator which have parameter N. In stage 2, three stage feature selection algorithm is used It not only reduce the training time but also reduces evaluation time.
- Stage 1: In this, we propose optimized technical indicator by finding the most related value of N. In this we will vary the value of N from 2 to 20. The value of N which is more related to class is decided by the algorithm called FAST correlation feature selection.In this way, we will get the
value of N for different technical indicators like RSI, SMA, WMA , STCK, EMA, WMA, TMA .
- Stage2: In this, input from the stage 1 is combined with technical indicators which are not using N. Three independent feature selection methods are used on the combined data for dimension reduction. These three feature selection methods are implemented sequentially; this is called as multilevel feature selection.Three different feature selection methods which are to be applied on data are:
  - Principal Component Analysis (PCA)
  - Granger Causality Test (GCT)-It identifies that the feature is able to forecast or not, But before going for this test it is very important that data should be stationary. For checking the stationarity of data, Dickey fuller test is applied. In dickey fuller test, if p-value is more than 0.05 then data is not stationary. If data is not stationary, it is required to make data stationary by using difference function and if data is stationary, it is passed for granger causality test in which the correlation between the feature and class is explored.
  - Recursive Feature Elimination (RFE).
- After feature selection methods, the modified data is used, as input to the machine learning models. Models are:
  - Random forest.
  - Multiple Linear Regression.
  - Artifical neural network.
  - Gradient Boosting.
- The evaluation measures are Mean Absolute Percentage Error (MAPE), Mean Square Error (MSE), Mean absolutem error(MAE) are used to evaluate the performance of models which are used for forecasting.

## Data and code flow
- Maruti_raw.xlsx and TCS_raw.xlsx are the base 12 years of dataset.Dataset has been created using formulas of technical indicator i.e. Maruti.xlsx and TCS.xlsx. 
- Before sending data to stage 1. Data has been created for technical indicators for which N can vary. In this there are 7 techincal indicators (ema,tma,rsi,stochastic K%, stochastic d%,sma,wma) like that. ema,tma has been calculated in Excel only and for rest rsi.py,sma.py,stckstc.py,wma.py for creating rest data for passing input to stage1. 7 Dataset has been created and one by one passed to stage 1.
- fcbc.py for appling FAST correlation feature selection algorithm (stage1). for each dataset in data folder this .py file will give an efficient N value.
- Used jupyter notebook for stage 2 and stage 3. Maruti.ipynb and TCS.ipynb are the main code. In this PCA output created and stored in PCA.csv. then dickeyfuller test applied on it. then granger_ip.csv is send to test.R and output of that has been stored in granger_op.csv. this is send to RFE and result of that stored in rfe.csv. This is the input for all the prediction models
- Used Rstudio for granger casuality test which is in test.R.
