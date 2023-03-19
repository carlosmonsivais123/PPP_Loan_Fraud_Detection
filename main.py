# Libraries and Modules
from Input_Values.input_vars import input_data_location
from Read_Data.read_data_df import Read_Data_DF
from EDA.eda_outputs import EDA_Outputs

import pandas as pd


# Calling Modules
read_data_df=Read_Data_DF()
eda_outputs=EDA_Outputs()


# Reading in Data
original_data_df=read_data_df.data_to_pandas_df(input_data_location=input_data_location)


# EDA
eda_outputs.eda_plots_missing_values_heatmap(data=original_data_df)
eda_outputs.eda_correlation_heatmap(data=original_data_df)