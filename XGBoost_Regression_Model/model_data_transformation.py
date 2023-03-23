class Model_Data_Transformations:
    def select_and_impute_features(self, data):
        model_vars=data[['LoanNumber', 
                         'ProcessingMethod',
                         'Term',
                         'InitialApprovalAmount',
                         'CurrentApprovalAmount', 
                         'RuralUrbanIndicator', 
                         'HubzoneIndicator',
                         'LMIIndicator', 
                         'JobsReported',
                         'UTILITIES_PROCEED',
                         'PAYROLL_PROCEED', 
                         'MORTGAGE_INTEREST_PROCEED', 
                         'RENT_PROCEED',
                         'REFINANCE_EIDL_PROCEED', 
                         'HEALTH_CARE_PROCEED',
                         'DEBT_INTEREST_PROCEED',
                         'ForgivenessAmount',
                         'Industry_Type', 
                         'Loan_Count', 
                         'Loan_Amount_Owed',
                         'Revised_Loan_Amount', 
                         'Days_With_Loan']]

        model_vars[['UTILITIES_PROCEED',
                    'PAYROLL_PROCEED', 
                    'MORTGAGE_INTEREST_PROCEED', 
                    'RENT_PROCEED',
                    'REFINANCE_EIDL_PROCEED', 
                    'HEALTH_CARE_PROCEED',
                    'DEBT_INTEREST_PROCEED']]=model_vars[['UTILITIES_PROCEED',
                                                          'PAYROLL_PROCEED', 
                                                          'MORTGAGE_INTEREST_PROCEED', 
                                                          'RENT_PROCEED',
                                                          'REFINANCE_EIDL_PROCEED', 
                                                          'HEALTH_CARE_PROCEED',
                                                          'DEBT_INTEREST_PROCEED']].fillna(value=0)
        
        return model_vars
    

    def sklearn_data_pipelines(self, data):
        return None