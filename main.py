# Libraries and Modules
from Input_Values.input_vars import loan_input_data_location, geojson_input_data_location
from Read_Data.read_data_files import Read_Data
from Data_Cleaning.clean_data import Clean_Data
from Feature_Engineering.create_features import Create_Features
from EDA.eda_outputs import EDA_Outputs


# Calling Modules
print('Importing Modules\n')
read_data=Read_Data()
clean_data=Clean_Data()
create_features=Create_Features()
eda_outputs=EDA_Outputs()


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
clean_data_df=create_features.create_zip5(data=clean_data_df) # Zip5 Feature


# EDA (All EDA Images are Output in the folder --> Plots_Storage/EDA_Plots)
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


# Subsetting Features



# Sklearn Pipeline For Modeling Features
print('Normalizing And One-Hot Encoding Variables That Will Be Used To Model\n')