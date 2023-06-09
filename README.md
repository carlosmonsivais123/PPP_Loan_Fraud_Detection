# Small Business Paycheck Protection Program Fraud Detection
## By: Carlos Monsivais

### Goal
The goal is to look for instances of loan fraud for the Small Business PPP  program. Since there are no labels indicating
whether each loan is fraudulent, I will use a XGBoost Regression modeling technique to analyze the model standardized 
residuals and look for outliers, which I will consider fraudulent.

### How to Execute
1. Download the dataset from the following link:
    * PPP Dataset: https://www.kaggle.com/datasets/nflovejoy/paycheck-protection-program-loan-data?select=public_150k_plus_230101.csv

2. After downloading the dataset, place it in the following project folder: data/Input_Data/

3. Run the following bash script to create the virtual environment for the project: ./create_env.sh

4. Activate the virtual environment called small_biz by using the command: source small_biz/bin/activate

5. Now there are two options to run this process:
    * Option 1 --> Run the main.ipynb notebook cell by cell.
    * Option 2 --> Run the main.py file with the following command: python3 main.py
      
        * Either option will work. Running this process will do the following jobs:
            - Read in the datasets with a predefined schema ensuring proper data types.
            - Clean data by removing rows with important loan information and null value filling.
            - Feature engineering by creating new features such as: 
                - Industry Type (mapping)
                - Loan Count (function) 
                - Loan Amount Owed (function)
                - Revised Loan Amount (function) 
                - Days With Loans (function)
                - Borrower ZIP5 (function)
                - Service Lender ZIP5 (function)
            - Create 15 EDA Plots using Plotly and are then stored as static images here: Plots_Storage/EDA_Plots
                - These plots include a correlation matrix, and compare industry, gender and loan types.
            - Feature selection to ensure the features that will be used make sense within the model.
            - Data pipeline where one-hot encoding and standard scaling is applied to the categorical and numerical variables.
            - Split data into X and y variables.
            - Create 20 XGBoost Regression models and choose the best model based on cross validation.
                - The best model of the 20 is saved in the following location where it can be recalled at anytime to not have to re-run this step: XGBoost_Regression_Model/Saved_Model/xgboost_model1.json
            - Model feature importance is calculated and plotted to show the effect of each feature in our model to help give explainability to our results. The values are plot and saved here: Model_Feature_Importance/Feature_Importance_Plot/model_feature_importance.png
            - Standardized residuals are calculated through a custom function in order for them to be in a state where we can use them for outlier detection.
            - Fraud labels are applied to each loan using the bottom 1% and upper 99% loans that are considered to be outliers.
            - Final dataframe is produced and stored in the following location so the Dash application is able to use this output file in the following location: Dash_App/data/final_analysis_df.csv

6. Now that all the output files are in the correct place, we can run the Dash web application by changing directories into the Dash_App environment by running the following:
    * cd Dash_App/
    * python3 index.py

7. Now this will create the web application on the following port where you need to open a browser and type in the following link to access the Dash application:
    * http://127.0.0.1:8050/

8. This is the process end to end from reading in data, data cleaning, transformations, modeling, fraud detection, output files and starting up the web application.

### Project Diagram
![Project Flow Diagram](Project_Diagram_Flow/PPP_Fraud_Detection.drawio.png)

### Readings
* Standardized Residuals
    * http://www.stat.ucla.edu/~nchristo/introeconometrics/introecon_compute_sres_hat.pdf
    * https://online.stat.psu.edu/stat462/node/172/

### Dash Images
![alt](Dash_Images/dash_1.png)
![alt](Dash_Images/dash_2.png)
![alt](Dash_Images/dash_3.png)
![alt](Dash_Images/dash_4.png)
![alt](Dash_Images/dash_5.png)
![alt](Dash_Images/dash_6.png)
![alt](Dash_Images/dash_7.png)
![alt](Dash_Images/dash_8.png)
![alt](Dash_Images/dash_9.png)