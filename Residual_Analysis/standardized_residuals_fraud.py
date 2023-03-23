import numpy as np

class Fraud_Detection:
    def standardized_residuals_percentiles(self, data):
        data['percentile']=data['standardized_residual'].rank(pct=True)

        data['Fraud_Detection']='Not Fraud'
        data.loc[data['percentile']>0.99, 'Fraud_Detection'] = 'Fraud'
        data.loc[data['percentile']<0.01, 'Fraud_Detection'] = 'Fraud'

        data=data.rename(columns={'Predictions': 'Predicted_Loan_Amount_Owed',
                                 'Actual': 'Actual_Loan_Amount_Owed'})
        
        data=data[['Predicted_Loan_Amount_Owed', 'Actual_Loan_Amount_Owed', 'Residuals',
                   'standardized_residual',	'percentile', 'Fraud_Detection']]


        return data