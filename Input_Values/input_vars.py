import yaml
import numpy as np

with open('Input_Values/inputs.yaml', 'r') as file:
    input_vars=yaml.safe_load(file)

loan_input_data_location=input_vars['Loan_Data_Location']
geojson_input_data_location=input_vars['GeoJSON_Data_Location']