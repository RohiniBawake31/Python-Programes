# Analysis of Advertising Data
    Predict product sales based on advertising spend across TV, Radio, and Newspaper.
# Dataset Overview:
   There are three features and one target variable in dataset,involving 200 row and 5 columns. 
TV: Advertising budget spent on TV (in thousands of dollars)
Radio: Advertising budget spent on Radio
Newspaper: Advertising budget spent on Newspaper
Sales: Units sold (in thousands)

# Exploratory Data Analysis (EDA):
    Firstly we check Null values ,duplicates , outliers in data. For Visualization use Histograms,box plots for each feature. also used Scatter plot for find relation between features and target.
 we see TV and Radio likely have stronger correlations with Sales than Newspaper.
# feature Engineering :
  Drop unnecessary columns like Unnamed: 0 .
# Model Building:
Divide data into training and testing used 80% data for training & 20 % data for testing the model.
# Model Evaluation:
   we have to use linear regression model its give 91% R2 Score. then K neirest neighbour give 93% and In Naive bayes algorithms we used baysian ridge its gives 89% r2 score.
From this we conclude that k neirest neighbour model is give more accurest prediction.

