import pandas as pd
import json

class Read_Data:
    def loan_data_to_pandas_df(self, loan_input_data_location):
        data_schema={'LoanNumber': str, 
                     'DateApproved': str, 
                     'SBAOfficeCode': str, 
                     'ProcessingMethod': str,
                     'BorrowerName': str, 
                     'BorrowerAddress': str, 
                     'BorrowerCity': str, 
                     'BorrowerState': str,
                     'BorrowerZip': str, 
                     'LoanStatusDate': str, 
                     'LoanStatus': str, 
                     'Term': int,
                     'SBAGuarantyPercentage': float, 
                     'InitialApprovalAmount': float,
                     'CurrentApprovalAmount': float, 
                     'UndisbursedAmount': float, 
                     'FranchiseName': str,
                     'ServicingLenderLocationID': str, 
                     'ServicingLenderName': str,
                     'ServicingLenderAddress': str, 
                     'ServicingLenderCity': str, 
                     'ServicingLenderState': str,
                     'ServicingLenderZip': str, 
                     'RuralUrbanIndicator': str, 
                     'HubzoneIndicator': str,
                     'LMIIndicator': str, 
                     'BusinessAgeDescription': str, 
                     'ProjectCity': str,
                     'ProjectCountyName': str, 
                     'ProjectState': str, 
                     'ProjectZip': str, 
                     'CD': str, 
                     'JobsReported': float,
                     'NAICSCode': str, 
                     'Race': str, 
                     'Ethnicity': str, 
                     'UTILITIES_PROCEED': float,
                     'PAYROLL_PROCEED': float, 
                     'MORTGAGE_INTEREST_PROCEED': float, 
                     'RENT_PROCEED': float,
                     'REFINANCE_EIDL_PROCEED': float, 
                     'HEALTH_CARE_PROCEED': float,
                     'DEBT_INTEREST_PROCEED': float, 
                     'BusinessType': str, 
                     'OriginatingLenderLocationID': str,
                     'OriginatingLender': str, 
                     'OriginatingLenderCity': str, 
                     'OriginatingLenderState': str,
                     'Gender': str, 
                     'Veteran': str, 
                     'NonProfit': str, 
                     'ForgivenessAmount': float,
                     'ForgivenessDate': str}
        
        parse_dates = ['DateApproved', 'LoanStatusDate', 'ForgivenessDate']
        original_data_df=pd.read_csv(loan_input_data_location, dtype=data_schema, parse_dates=parse_dates)

        return original_data_df
    


    def read_in_geojson_data(self, geojson_input_data_location):
        with open(f'{geojson_input_data_location}') as f:
            counties=json.load(f)

        return counties