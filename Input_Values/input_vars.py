import yaml
import numpy as np

with open('Input_Values/inputs.yaml', 'r') as file:
    input_vars=yaml.safe_load(file)

# Read Data Location
loan_input_data_location=input_vars['Read_Data_Location']['Loan_Data_Location']
geojson_input_data_location=input_vars['Read_Data_Location']['GeoJSON_Data_Location']

# Plot Location
eda_plot_location=input_vars['Plot_Location']['EDA_Plot_Location']
