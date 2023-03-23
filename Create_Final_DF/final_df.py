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
        
        final_df.to_csv('data/Output_Data/final_analysis_df.csv', index=False)
        
        return final_df