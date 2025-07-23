
## 50_Startups Profit Prediction Using Linear Regression.

## Project Overview
This project analyzes the impact of R&D Spend, Administration, and Marketing Spend on company profit across different U.S. states using linear regression. The goal is to build an interpretable model to understand which features most influence profitability and create a predictive tool for future estimates.
## Dataset Description
Records: 50 rows & Features:4

R&D Spend: Investment in research and development

Administration: Operational spending

Marketing Spend: Advertising and promotional costs

State: Company’s registered location (California, Florida, New York)

Profit: Net profit (target variable)

## 🎯 Problem Statement
To predict company Profit based on investment features, and understand the relative importance of R&D, administration, and marketing expenses.

## Exploratory Data Analysis
Check for missing values, outliers, and distribution of features.

Use visualizations like histograms,scatterplot pair plots, and box plots.

Correlation analysis to understand feature-target relationships.

## Data Preprocessing:

#### Handling missing values :
  no explicit nulls, but rows with zero values in R&D Spend and Marketing Spend replace its with mean.

#### Feature Scaling :
 Applied StandardScaler to normalize numerical features for better model performance:

## Model building :
 split data into 75% for training and 25% testing. use linear regression model for prediction.

## Evaluation Metrics:

Metric	        Value
R² Score     :	0.94
Adj R² Score :  0.91
MAE         :	0.028	
RMSE	    :    0.16

#### Model gives 94% accurasy thats means model is best fit.

## 🔍 Key Insights
R&D Spend likely has the strongest positive correlation with Profit.

State may have minor impact; explore via dummy coefficients.

Marketing Spend may show diminishing returns—important for budget allocation.
## 🛠️ Tools & Libraries
Python 3.x

pandas, numpy, matplotlib, seaborn

scikit-learn for regression and metrics

## 🧠 Author
   **Rohini**  
Data science enthusiast focused on real-world modeling. 

📂 GitHub: [RohiniBawake31](https://github.com/RohiniBawake31)
