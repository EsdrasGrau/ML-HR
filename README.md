<div style="text-align:center"><img src="https://user-images.githubusercontent.com/23629340/40541063-a07a0a8a-601a-11e8-91b5-2f13e4e6b441.png" /> <img src="https://www.sweet-bakery.co.jp/sites/default/files/logo.png" /></div>



# FB Prophet (Time Series) Forecasting, practical application

## Overview

This project has the purpose to reduce cost and optimize the resources of a Japanse bakery where I collaborate. [SWEET Co. Bakery](https://www.sweet-bakery.co.jp/) was founded in 1913 in Seattle, USA by a Japanese immigrant that after 10 years decided to move back to his hometown in Matsumoto, Japan. Since then the bakery has been open and run by the same family for 4 generations. 



## Project Tools & Steps

Prophet is [open source software](https://code.facebook.com/projects/) released by Facebook’s [Core Data Science team](https://research.fb.com/category/data-science/).  Prophet is a procedure for forecasting time series data based on an additive model where non-linear trends are fit with yearly, weekly, and daily seasonality, plus holiday effects. It works best with time series that have strong seasonal effects and several seasons of historical data. Prophet is robust to missing data and shifts in the trend, and typically handles outliers well.

**Steps (Jupyter Notebooks)**:

1. I defined a testing area where I learned all the basics and material from FB Prophet documentation. 
2. Used data directly from [SquareUp](http://squareup.com/) that is the cash register management that the company use. This data was cleaned and prepared to be able to use in FB Prophet.
3. The training data is from 2018-04-26 until 2019-12-31 as I want to predict January of 2020.  The last one is also included to test the model.
4. The test area helped me to validate and refine the final model.
5. I added historical weather data to figure out the influence on the model. After some analysis, this data was dropped as was intrinct to the data.
6. Once I got satisfactory results I added Data Visualization to understand how the model was adapting and predicting.
7. Metrics are included and the FB Prophet own cross-validation module.



## Conclusions

Using the model predictions I prepared a business analysis about how the company predicts their sales vs FB Prophet forecast and how they allocate the staff according to their calculations. Finding that FB Prophet offers better insights helping to reduce HR cost allocating the staff more efficiently and reducing cost.

FB Prophet is a great tool that small & medium companies can take advantage to optimize their resources and reduce cost. This model can be easily applied to different areas of the bakery like production, supply chain and human resources where the time series is part of the daily operation of the company. 

## Next steps

- Deploy FB Prophet in pythonanyware.com using Flask and be able to make consultations on the established model by the staff with a basic UI.
- Improve the UI and be able to change the hyperparameters according to the necessities of the staff.



## Files 

FB Prophet folder:

1. FB Prophet - Final Vr.ipynb

2. 2018-2019_prophet.csv

3. 2018-2020j_prophet.csv

4. README.md

5. Business Analysis.xlsx

6. Dynamic-plot.html

Other folders:

1. Data: Includes all raw data by transactions and items (2018-2020 February)
2. Tutorials: Basic tutorials from FB Prophet team
3. Web Scrapping: To obtain weather historical data 

## Author

`EsdrasGrau`

```
|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|
| CODING FERRET     |
|___________________|
(\__/) || 
(•ㅅ•) || 
/ 　 づ
I'm a ferret, not a rabbit o(>ω<)o 
```