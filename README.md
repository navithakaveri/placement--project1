# placement--CRIME ANALYSIS

**DATA COLLECTION**
Gathered data such as crime type,date,location,location description..etc

**DATA PREPROCESSING**
Data Preprocessing: The project begins with a data preprocessing step, which involves handling missing values, removing duplicate values, and converting data types to prepare the dataset for analysis and modeling.

*missing value filled with constant for community area and location description

*missing value filled with median for  district,ward etc

*Date data type convered from object to datetime,for extracting day,month,year,hour etc..

**EDA PROCESS**
*Manual EDA involves visualizing key features such as PRIMARY TYPE, , LOCATION DESCRIPTION, TIME SERIES ANALYSIS ON YEAR ,MONTH,DAY ,ARREST RATE ETC..

**MODEL SELECTION**
* model selected and fitted data and transform data nto the algorithm.


**Train-Test Split:**
Split the data into training (80%) and test (20%) sets using train_test_split from scikit-learn.


**Model Initialization and Training**
Create a logistic regression and decision tree classifier model and train it on the training data using model.fit(X_train, y_train).


**Prediction and Evaluation**
Make predictions on the test data with model.predict(X_test)  using mean_squared_error(y_test, y_pred) to evaluate model performance.


**Results Visualization:**
Plot the predicted vs actual values to visually inspect how well the model predictions align with the true values


  

 Predictive Analysis: Develop models to predict future crime incidents based on historical data, time, location, and other relevant factors.
   - Risk Assessment: Assess the risk of different areas and times for specific types of crimes to help in resource allocation for law enforcement.

