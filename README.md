# Used Cars Pricing Machine Learning Model

This repository contains the data pipeline, modeling experiments, and deployment code for a car price prediction application, as outlined in the project presentation Used Car pp.pptx.

## Data Preparation

The machine learning pipeline begins by importing the dataset from a CSV file named `used_cars_data.csv`. To ensure accurate model predictions, the following data cleaning and feature engineering steps are applied:

* Dropping high cardinality columns, specifically `S.No.` and the original `Name` column.


* Dropping the `New_Price` column because it contains a high percentage of null values.


* Dropping duplicate rows and rows where all values are null.


* Filling remaining missing numerical values using the mean of their respective columns.


* Extracting `Car_maker` (brand) and `Car_model` features by splitting the text in the `Name` column.


* Removing text characters (such as 'km/kg', 'kmpl', 'CC', and 'bhp') from the `Mileage`, `Engine`, and `Power` columns to convert them into float/numeric data types.



## Modeling and Experiments

Multiple machine learning models were tested using a scikit-learn `Pipeline` and `ColumnTransformer` (which applied One-Hot Encoding to categorical variables) to find the highest accuracy.

| Model | Validation Method | Validation Accuracy (R-squared) |
| --- | --- | --- |
| **Linear Regression** | Train/Test Split | 68.2%

 |
| **Linear Regression** | 5-Fold Cross Validation | 67.8%

 |
| **Random Forest Regressor** | 5-Fold Cross Validation | 89.7%

 |

According to the experiment results, the Random Forest Regressor with Cross Validation was chosen for the final validation and deployment steps due to its superior accuracy.

## Deployment

The final phase of the project involves deploying the chosen model as an interactive web application:

* The trained Random Forest pipeline is saved as a pickle file named `car_price_predictor.pkl` using the `joblib` library.


* The cleaned dataset is exported as `Used.csv` to be utilized by the frontend application.


* The deployment UI is built using Streamlit via an `app.py` script.


* The application takes user inputs including Year of Manufacture, Kilometers Driven, Mileage (km/l), Engine Capacity (cc), Power (bhp), Seats, Brand, Model, Location, Fuel Type, Transmission, and Owner Type.


* Upon processing the inputs, the application returns the predicted car price formatted in thousands of dollars (e.g., 7.56K $).



## Author & Contact

* **Email:** eng.ahmed.fakhrelden@gmail.com


* **Phone:** +20 155 044 8090


* **Portfolio:** [https://a-fakhrelden.github.io/Ahmedfakhr/](https://www.google.com/search?q=https://a-fakhrelden.github.io/Ahmedfakhr/&utm_source=gemini)
