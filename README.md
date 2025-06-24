# Personality-ml-classifier
## Overview
* Built a machine learning model that classifies individuals as extroverts or introverts based on behavioral data.
* The dataset was downloaded from Kaggle.
* Used a Logistic Regression model for classification.

## Code and Tools
**Pyhton version:** 3.13  
**Environment:** VS Code  
**Packages:** pandas, numpy, matplotlib, seaborn and scikitlearn  

## Dataset Information
**Name:** [Extrovert vs Introvert Behavior Data](https://www.kaggle.com/datasets/rakeshkapilavai/extrovert-vs-introvert-behavior-data?select=personality_dataset.csv)  
**Source:** Kaggle  
**Features:**
1. **Time_spent_Alone**: Hours spent alone daily  
2. **Stage_fear**: Presence of stage fright
3. **Social_event_attendance**: Frequency of social events
4. **Going_outside**: Frequency of going outside
5. **Drained_after_socializing**: Feeling drained after socializing
6. **Friends_circle_size**: Number of close friends
7. **Post_frequency**: Social media post frequency
8. **Personality**: Target variable (Extrovert/Introvert)

## **Process**
1. EDA and data cleaning
2. Preprocessing
3. Data Modeling
4. Evaluation

### 1. EDA and Data Cleaning 
#### Data Cleaning
The dataset had two main issues: missing values and incorrect data types in some features.  

1. **Missing values:** After identifying the missing values, I set a threshold of 5% based on the total length of the DataFrame. Then, I dropped the missing values from all columns that contained 5% or less missing data. No further action was needed, as all missing values were removed.
2. **Data types:** Numeric columns stored as floats were converted to integers. 

#### EDA
For numeric data, I created histograms to visualize distributions and calculated correlations.
For categorical data, I used contingency tables to analyze the relationship with the target variable. I also used boxplots to explore connections between personality type and numerical features.

![Histogram](Visualizations/social_event_attendance_hist.png)    ![Boxplot](Visualizations/circle_size_vs_personality.png)

### 2. Preprocessing
First, I converted categorical variables into binary format (0/1). Then, I split the dataset: 70% for training and 30% for testing. Finally, I scaled the numeric features.

### 3. Model Building 
I used a Logistic Regression model. This choice was based on the small number of features in the dataset, which makes it a good fit for a simple linear model.

### 4. Model Performance
I evaluated the model using a classification report. It showed strong results:

+ **Accuracy:** 0.93
+ **F1-score:** 0.94
