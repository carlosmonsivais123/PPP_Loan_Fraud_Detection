import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler

class Residual_Analysis:
    def analyze_residual_data(self, X, y, clean_data_df):
        best_xgboost_model=xgb.XGBRegressor()
        best_xgboost_model.load_model("XGBoost_Regression_Model/Saved_Model/xgboost_model1.json")

        predictions=best_xgboost_model.predict(X)
        data={'Predictions': predictions, 'Actual': y}
        residual_df=pd.DataFrame(data=data)

        standard_scaler=StandardScaler().fit(clean_data_df['Loan_Amount_Owed'].values.reshape(-1, 1))
        y_inverse_actual=standard_scaler.inverse_transform(residual_df['Actual'].values.reshape(-1, 1))
        y_inverse_pred=standard_scaler.inverse_transform(residual_df['Predictions'].values.reshape(-1, 1))

        data={'Predictions': y_inverse_pred.reshape(-1), 'Actual': y_inverse_actual.reshape(-1)}
        residual_df_inversed=pd.DataFrame(data=data)
        residual_df_inversed['Residuals']=residual_df_inversed['Actual']-residual_df_inversed['Predictions']

        divider=1/len(residual_df_inversed)
        residual_df_inversed['ssd']=(residual_df_inversed['Actual']-residual_df_inversed['Actual'].mean())**2
        tss=((residual_df_inversed['Actual']-residual_df_inversed['Actual'].mean())**2).sum()

        residual_df_inversed['h_val']=divider+(residual_df_inversed['ssd']/tss)

        mse=mean_squared_error(y_true=residual_df_inversed['Actual'], y_pred=residual_df_inversed['Predictions'])

        residual_df_inversed['standardized_residual']=(residual_df_inversed['Residuals'])/(mse*np.sqrt(1-residual_df_inversed['h_val']))

        return residual_df_inversed