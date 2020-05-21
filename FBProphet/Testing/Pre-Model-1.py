import pandas as pd
import numpy as np
import holidays
from fbprophet import Prophet
from matplotlib import pyplot as plt
plt.style.use('fivethirtyeight')
import seaborn as sns
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from scipy.stats import skew

import warnings
warnings.simplefilter('ignore', DeprecationWarning)
warnings.simplefilter('ignore', FutureWarning)


# Model 1 using  x.test as measure with extra graphs

train= pd.read_csv('2018-2020j_prophet.csv')
train.info()
train['Date'] = pd.to_datetime(train['Date'])
train.drop(columns=['Unnamed: 0'], inplace=True)
train.rename(columns={'Date': 'ds', 'Total': 'y'}, inplace=True)
df = train
fig, ax = plt.subplots(figsize=(15, 5))
ax.plot(df['ds'], df['y'], linestyle='-', label='All data')
ax.set_xlabel('Date')
ax.set_ylabel('Sales');

n_test = 26
df_train = df[:-n_test]
df_test = df[-n_test:]
fig, ax = plt.subplots(figsize=(15,5))
ax.plot(df_train['ds'], df_train['y'], linestyle='-', color='blue', label='Train')
ax.plot(df_test['ds'],df_test['y'],linestyle='-', color='red', label='Test')
ax.legend()
ax.set_xlabel('Date')
ax.set_ylabel('Sales');

events = pd.DataFrame({
    'holiday': 'event',
    'ds': pd.to_datetime(['2018-04-28', '2018-04-29', '2018-04-30',
                          '2018-05-03', '2018-05-04', '2018-05-05',
                          '2018-05-20', '2018-05-26', '2018-05-27',
                          '2018-06-23', '2018-06-24', '2018-07-29',
                          '2018-08-04', '2018-08-11', '2018-08-12',
                          '2018-08-14', '2018-08-16', '2018-08-19',
                          '2018-09-02', '2018-09-23', '2018-09-24',
                          '2018-10-08', '2018-11-03',
                          '2019-01-02', '2019-01-03', '2019-01-04',
                          '2019-01-05', '2019-01-06', '2019-01-12',
                          '2019-01-13', '2019-04-13', '2019-04-14',
                          '2019-04-20', '2019-04-21', '2019-04-28',
                          '2019-04-29', '2019-04-30', '2019-05-01',
                          '2019-05-02', '2019-05-03', '2019-05-04',
                          '2019-05-25', '2019-05-26', '2019-06-22',
                          '2019-06-23', '2019-07-14', '2019-08-11',
                          '2019-08-12', '2019-08-15', '2019-09-29',
                          '2019-11-03',
                          '2020-01-02', '2020-01-03', '2020-01-04',
                          '2020-01-05', '2020-01-11', '2020-01-12',
                          '2020-01-13', '2020-02-02', '2020-02-14',
                          '2020-02-23']),
    'lower_window':0,
    'upper_window':1,
})
superholidays = pd.DataFrame({
    'holiday': 'superholiday',
    'ds': pd.to_datetime(['2018-04-29', '2018-05-03', '2018-05-04',
                          '2018-05-05', '2018-05-27', '2018-06-23',
                          '2018-06-24', '2018-08-04',
                          '2019-01-02', '2019-01-03', '2019-01-13',
                          '2019-04-29', '2019-04-30', '2019-05-01',
                          '2019-05-03', '2019-05-04', '2019-06-22',
                          '2020-01-02', '2020-01-03', '2020-01-04',
                          '2020-01-11']),
    'lower_window':0,
   'upper_window':1,
})
holidays = pd.concat((events, superholidays))

#Hyperparameters
model = Prophet(holidays=holidays,

            yearly_seasonality=True,
            weekly_seasonality=True,
            daily_seasonality=False,

            seasonality_prior_scale=0.1,
            interval_width=0.95,
            holidays_prior_scale=10,
            changepoint_prior_scale=0.15)

model.add_country_holidays(country_name='JP')
model.fit(df_train)

forecast = model.predict(df)
forecast[['ds','yhat']].head()

model.plot_components(forecast)

fig, ax = plt.subplots(figsize=(15,5))
ax.plot(df_train['ds'], df_train['y'], c='grey', marker='o', ms=3, linestyle='-', label='Train')
ax.plot(df_test['ds'], df_test['y'], c='red', marker='o',ms=3, linestyle='-', label='Test')
ax.plot(forecast['ds'], forecast['yhat'], c='blue', marker='o', ms=3, linestyle='-', label='Forecast', alpha=0.5)
ax.legend()
ax.set_xlabel('Date')
ax.set_ylabel('Sales');

forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()
metric_df = forecast.set_index('ds')[['yhat']].join(df.set_index('ds').y).reset_index()

metric_df.tail(5)
metric_df.dropna(inplace=True)
metric_df.tail()
print('The R2 score is:', r2_score(metric_df.y, metric_df.yhat))
