import pandas as pd

class Final_DF:
    def create_final_dataframe(self, clean_data_df, fraud_df):
        clean_data_df_subset=clean_data_df[['LoanNumber', 'DateApproved', 
                                            'BorrowerName', 'BorrowerCity', 'BorrowerState',
                                            'Term', 'InitialApprovalAmount', 'CurrentApprovalAmount', 
                                            'ServicingLenderName', 'ServicingLenderCity', 'ServicingLenderState', 'ServicingLenderZip', 
                                            'RuralUrbanIndicator', 'HubzoneIndicator', 'LMIIndicator', 'JobsReported', 
                                            'UTILITIES_PROCEED', 'PAYROLL_PROCEED', 'MORTGAGE_INTEREST_PROCEED', 'RENT_PROCEED', 
                                            'REFINANCE_EIDL_PROCEED', 'HEALTH_CARE_PROCEED', 'DEBT_INTEREST_PROCEED', 
                                            'NonProfit', 'ForgivenessAmount', 'ForgivenessDate', 'Industry_Type', 'Loan_Count',
                                            'Revised_Loan_Amount', 'Days_With_Loan','Borrower_ZIP5', 'Servicing_Lender_ZIP5']]
        
        final_df=pd.merge(clean_data_df_subset, 
                          fraud_df, 
                          left_index=True, 
                          right_index=True)
        
        final_df=final_df.rename(columns={'LoanNumber': 'Loan Number',
                                          'DateApproved': 'Date Approved', 
                                          'BorrowerName': 'Borrower Name', 
                                          'BorrowerCity': 'Borrower City',
                                          'BorrowerState': 'Borrower State',
                                          'Term': 'Term', 
                                          'InitialApprovalAmount': 'Initial Approval Amount',
                                          'CurrentApprovalAmount': 'Current Approval Amount', 
                                          'ServicingLenderName': 'Servicing Lender Name', 
                                          'ServicingLenderCity': 'Servicing Lender City',
                                          'ServicingLenderState': 'Servicing Lender State', 
                                          'ServicingLenderZip': 'Servicing Lender Zip', 
                                          'RuralUrbanIndicator': 'Rural Urban Indicator',
                                          'HubzoneIndicator': 'Hubzone Indicator', 
                                          'LMIIndicator': 'LMI Indicator', 
                                          'JobsReported': 'Jobs Reported', 
                                          'UTILITIES_PROCEED': 'Utilities Proceed',
                                          'PAYROLL_PROCEED': 'Payroll Proceed', 
                                          'MORTGAGE_INTEREST_PROCEED': 'Mortgage Interest Proceed', 
                                          'RENT_PROCEED': 'Rent Proceed',
                                          'REFINANCE_EIDL_PROCEED': 'Refinance EIDL Proceed', 
                                          'HEALTH_CARE_PROCEED': 'Health Care Proceed',
                                          'DEBT_INTEREST_PROCEED': 'Debt Interest Proceed', 
                                          'NonProfit': 'Nonprofit', 
                                          'ForgivenessAmount': 'Forgiveness Amount',
                                          'ForgivenessDate': 'Forgiveness Date', 
                                          'Industry_Type': 'Industry Type', 
                                          'Loan_Count': 'Loan Count', 
                                          'Revised_Loan_Amount': 'Revised Loan Amount',
                                          'Days_With_Loan': 'Days With Loan', 
                                          'Borrower_ZIP5': 'Borrower ZIP5', 
                                          'Servicing_Lender_ZIP5': 'Servicing Lender ZIP5',
                                          'Predicted_Loan_Amount_Owed': 'Predicted Loan Amount Owed', 
                                          'Actual_Loan_Amount_Owed': 'Actual Loan Amount Owed', 
                                          'Residuals': 'Residuals',
                                          'standardized_residual': 'Standardized Residuals', 
                                          'percentile': 'Percentile', 
                                          'Fraud_Detection': 'Fraud Detection'})

        final_df.to_csv('Dash_App/data/final_analysis_df.csv', index=False)
        
        return final_df