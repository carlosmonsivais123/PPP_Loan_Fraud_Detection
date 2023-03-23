# Libraries and Modules
from Input_Values.input_vars import loan_input_data_location, geojson_input_data_location
from Read_Data.read_data_files import Read_Data
from Data_Cleaning.clean_data import Clean_Data
from Feature_Engineering.create_features import Create_Features
from EDA.eda_outputs import EDA_Outputs
from XGBoost_Regression_Model.model_data_transformation import Model_Data_Transformations
from XGBoost_Regression_Model.data_split import Data_Split
from XGBoost_Regression_Model.create_model import Create_Model
from Residual_Analysis.residual_analysis import Residual_Analysis
from Residual_Analysis.standardized_residuals_fraud import Fraud_Detection
from Create_Final_DF.final_df import Final_DF


# Calling Modules
print('Importing Modules\n')
read_data=Read_Data()
clean_data=Clean_Data()
create_features=Create_Features()
eda_outputs=EDA_Outputs()
model_data_transformations=Model_Data_Transformations()
data_split=Data_Split()
create_model=Create_Model()
residual_analysis=Residual_Analysis()
fraud_detection=Fraud_Detection()
final_df=Final_DF()


# Read in Data
print('Reading In Data\n')
original_data_df=read_data.loan_data_to_pandas_df(loan_input_data_location=loan_input_data_location)
geojson_data=read_data.read_in_geojson_data(geojson_input_data_location=geojson_input_data_location)


# Removing Certain Rows Based on Columns
print('Removing Null Values\n')
print(f'The original dataframe has the following shape: {original_data_df.shape}')
remove_nulls_df=clean_data.remove_nulls_based_on_columns(data=original_data_df)
remove_territories_df=clean_data.remove_usa_territories(data=remove_nulls_df)
print(f'After removing Null values the new dataframe has the following shape: {remove_territories_df.shape}')


# Feature Engineering: Industry Mapping
print('Feature Engineering: Industry Mapping\n')
clean_data_df=create_features.mapping_industries(data=remove_nulls_df) # Industry Mapping
clean_data_df=create_features.number_of_loans(data=clean_data_df) # Number of Loans
clean_data_df=create_features.amount_of_loan_forgiven(data=clean_data_df) # Amount of Loan Forgiven
clean_data_df=create_features.revised_loan_amount(data=clean_data_df) # Revised Loan Approval
clean_data_df=create_features.days_with_loan_approval(data=clean_data_df) # Days With Loan
clean_data_df=create_features.create_borrower_zip5(data=clean_data_df) # ZIP5 Borrower Feature
clean_data_df=create_features.create_lender_zip5(data=clean_data_df) # ZIP5 Lender Feature


# EDA
print('Creating EDA Plots\n')
eda_outputs.eda_plots_missing_values_heatmap(data=clean_data_df)
eda_outputs.eda_correlation_heatmap(data=clean_data_df)
eda_outputs.eda_mapping_industries_and_count(data=clean_data_df)
eda_outputs.eda_spread_by_gender(data=clean_data_df)
eda_outputs.eda_average_loan_amount_by_industry_and_gender(data=clean_data_df)
eda_outputs.eda_average_loan_amount_by_lmi_indicator_by_industry(data=clean_data_df)
eda_outputs.eda_average_loan_amount_by_hubzone_indicator_by_industry(data=clean_data_df)
eda_outputs.eda_state_loan_count(data=clean_data_df)
eda_outputs.eda_state_loan_avg_amount(data=clean_data_df)
eda_outputs.eda_zip_loan_count(data=clean_data_df, counties=geojson_data)
eda_outputs.eda_zip_loan_avg(data=clean_data_df, counties=geojson_data)
eda_outputs.eda_time_series_gender_loan_amount(data=clean_data_df)
eda_outputs.eda_time_series_loan_amount(data=clean_data_df)
eda_outputs.eda_spend_amount_per_category(data=clean_data_df)
eda_outputs.eda_daily_spend_per_indsutry(data=clean_data_df)


# Selecting Modeling Features
print('Selecting and Imputing Features That Will Be Used In The Modeling Process')
ml_dataset_df=model_data_transformations.select_and_impute_features(data=clean_data_df)


# Sklearn Pipeline For Modeling Features --> One-Hot Encoding and StandardScaler()
print('Normalizing And One-Hot Encoding Variables That Will Be Used To Model\n')
ml_sparse_df=model_data_transformations.sklearn_data_pipelines(data=ml_dataset_df)


# Splitting Into X and Y Variables
print('Splitting Into X And y Variables\n')
x_y_variables=data_split.split_data_x_y(data=ml_sparse_df)
X=x_y_variables[0]
y=x_y_variables[1]


# XGBoost Regression Model
print('Creating And Saving XGBoost Model Based On A GridSearchCV\n')
best_xgboost_model=create_model.create_xgboost_model(X=X, y=y)


# Standardized Residuals
print('Standardizing Resdiduals For Fraud Detection\n')
standardized_residuals_df=residual_analysis.analyze_residual_data(X=X, 
                                                                  y=y,
                                                                  clean_data_df=clean_data_df)


# Calculating Fraud Based on Residuals
print('Labeling Fraud And Not Fraud Loans Based On Standardized Residual Percentiles\n')
fraud_df=fraud_detection.standardized_residuals_percentiles(data=standardized_residuals_df)


# Creating Final DataFrame
print('Creating The Final Output DataFrame\n')
final_df_output=final_df.create_final_dataframe(clean_data_df=clean_data_df, fraud_df=fraud_df)