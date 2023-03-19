import yaml
import numpy as np

with open('Input_Values/inputs.yaml', 'r') as file:
    input_vars=yaml.safe_load(file)

input_data_location=input_vars['Data_Location']