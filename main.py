# Libraries and Modules
from Input_Values.input_vars import input_data_location
from Read_Data.read_data_df import Read_Data_DF
from Data_Cleaning.clean_data import Clean_Data
from Feature_Engineering.create_features import Create_Features
from EDA.eda_outputs import EDA_Outputs


# Calling Modules
print('Importing Modules\n')
read_data_df=Read_Data_DF()
clean_data=Clean_Data()
create_features=Create_Features()
eda_outputs=EDA_Outputs()


# Read in Data
print('Reading In Data\n')
original_data_df=read_data_df.data_to_pandas_df(input_data_location=input_data_location)
original_data_df.head()


# Removing Certain Rows Based on Columns
print('Removing Null Values\n')
print(f'The original dataframe has the following shape: {original_data_df.shape}')
remove_nulls_df=clean_data.remove_nulls_based_on_columns(data=original_data_df)
print(f'After removing Null values the new dataframe has the following shape: {remove_nulls_df.shape}')


# Feature Engineering: Industry Mapping
print('Feature Engineering: Industry Mapping\n')
clean_data_df=create_features.mapping_industries(data=remove_nulls_df)


# EDA (All EDA Images are Output in the folder --> Plots_Storage/EDA_Plots)
print('Creating EDA Plots\n')
eda_outputs.eda_plots_missing_values_heatmap(data=clean_data_df)
eda_outputs.eda_correlation_heatmap(data=clean_data_df)
eda_outputs.eda_mapping_industries_and_count(data=clean_data_df)
eda_outputs.eda_spread_by_gender(data=clean_data_df)
eda_outputs.eda_average_loan_amount_by_industry_and_gender(data=clean_data_df)
eda_outputs.eda_average_loan_amount_by_lmi_indicator_by_industry(data=clean_data_df)
eda_outputs.eda_average_loan_amount_by_hubzone_indicator_by_industry(data=clean_data_df)


# Sklearn Pipeline For Modeling Features
print('Normalizing And One-Hot Encoding Variables That Will Be Used To Model\n')