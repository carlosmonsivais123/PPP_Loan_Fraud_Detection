import pandas as pd
import json
import pathlib

class Read_Data:
    def __init__(self):
        self.PATH=pathlib.Path(__file__).parent
        self.DATA_PATH=self.PATH.joinpath("../data").resolve()

    def loan_data_to_pandas_df(self):
        data_schema={'Loan Number': str, 
                     'Date Approved': str, 
                     'Borrower Name': str, 
                     'Borrower City': str,
                     'Borrower State': str,
                     'Term': int, 
                     'Initial Approval Amount': float,
                     'Current Approval Amount': float, 
                     'Servicing Lender Name': str, 
                     'Servicing Lender City': str,
                     'Servicing Lender State': str, 
                     'Servicing Lender Zip': str, 
                     'Rural Urban Indicator': str,
                     'Hubzone Indicator': str, 
                     'LMI Indicator': str, 
                     'Jobs Reported': int, 
                     'Utilities Proceed': float,
                     'Payroll Proceed': float, 
                     'Mortgage Interest Proceed': float, 
                     'Rent Proceed': float,
                     'Refinance EIDL Proceed': float, 
                     'Health Care Proceed': float,
                     'Debt Interest Proceed': float, 
                     'Nonprofit': str, 
                     'Forgiveness Amount': float,
                     'Forgiveness Date': str, 
                     'Industry Type': str, 
                     'Loan Count': int, 
                     'Revised Loan Amount': float,
                     'Days With Loan': int, 
                     'Borrower ZIP5': str, 
                     'Servicing Lender ZIP5': str,
                     'Predicted Loan Amount Owed': float, 
                     'Actual Loan Amount Owed': float, 
                     'Residuals': float,
                     'Standardized Residuals': float, 
                     'Percentile': float, 
                     'Fraud Detection': str}
    
        parse_dates = ['Date Approved', 'Forgiveness Date']
        df=pd.read_csv(self.DATA_PATH.joinpath("./final_analysis_df.csv"), 
                       dtype=data_schema, 
                       parse_dates=parse_dates)

        return df
    

    def read_in_geojson_data(self):
        with open(self.DATA_PATH.joinpath("./geojson-counties-fips.json")) as f:
            counties=json.load(f)

        return counties