import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.metrics import mean_squared_error

class Residual_Analysis:
    def analyze_residual_data(self, load_model, X, y, actual_model):
        if load_model==True:
            best_xgboost_model=xgb.XGBRegressor()
            best_xgboost_model.load_model("XGBoost_Regression_Model/Saved_Model/xgboost_model1.json")

        elif load_model==False:
            best_xgboost_model=actual_model

        predictions=best_xgboost_model.predict(X)

        data={'Predictions': predictions, 'Actual': y}
        residual_df=pd.DataFrame(data=data)
        residual_df['Residuals']=residual_df['Actual']-residual_df['Predictions']

        divider=1/len(residual_df)
        residual_df['ssd']=(residual_df['Actual']-residual_df['Actual'].mean())**2
        tss=((residual_df['Actual']-residual_df['Actual'].mean())**2).sum()

        residual_df['h_val']=divider+(residual_df['ssd']/tss)

        mse=mean_squared_error(y_true=residual_df['Actual'], y_pred=residual_df['Predictions'])

        residual_df['standardized_residual']=(residual_df['Residuals'])/(mse*np.sqrt(1-residual_df['h_val']))

        return residual_df