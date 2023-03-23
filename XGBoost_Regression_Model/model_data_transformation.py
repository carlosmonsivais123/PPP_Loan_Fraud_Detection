import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

class Model_Data_Transformations:
    def select_and_impute_features(self, data):
        model_vars=data[['LoanNumber', 
                         'ProcessingMethod',
                         'Term',
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
        categorical_features=['ProcessingMethod', 
                              'RuralUrbanIndicator', 
                              'HubzoneIndicator', 
                              'LMIIndicator']
        categorical_transformer=Pipeline([('onehot', OneHotEncoder(sparse_output=False, handle_unknown='ignore'))])

        numeric_features=['Term', 
                          'JobsReported',
                          'CurrentApprovalAmount',
                          'UTILITIES_PROCEED', 
                          'PAYROLL_PROCEED', 
                          'MORTGAGE_INTEREST_PROCEED', 
                          'RENT_PROCEED',
                          'REFINANCE_EIDL_PROCEED',
                          'HEALTH_CARE_PROCEED',
                          'DEBT_INTEREST_PROCEED',
                          'Loan_Count',
                          'Loan_Amount_Owed',
                          'Revised_Loan_Amount',
                          'Days_With_Loan']
        numeric_transformer=Pipeline([('scaler', StandardScaler())])

        preprocessing_step=ColumnTransformer([('categorical', categorical_transformer, categorical_features),
                                              ('numerical', numeric_transformer, numeric_features)],
                                              remainder = 'passthrough')


        preprocessing_step.set_output(transform='pandas')
        preprocessing_pipeline=Pipeline([('preprocessing_step', preprocessing_step)])
        ml_sparse_df=preprocessing_pipeline.fit_transform(data)

        return ml_sparse_df