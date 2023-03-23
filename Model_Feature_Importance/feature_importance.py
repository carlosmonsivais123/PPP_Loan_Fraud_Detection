import xgboost as xgb
import pandas as pd
import plotly.express as px

class Model_Feature_Importance:
    def xgboost_feature_importance(self):
        best_xgboost_model=xgb.XGBRegressor()
        best_xgboost_model.load_model("XGBoost_Regression_Model/Saved_Model/xgboost_model1.json")

        data={'Features': best_xgboost_model.feature_names_in_, 'Importance Score': best_xgboost_model.feature_importances_}
        feature_importance=pd.DataFrame(data).sort_values(by='Importance Score', ascending=True).reset_index(drop=True)

        fig = px.bar(feature_importance, 
                     y="Features", 
                     x="Importance Score", 
                     orientation='h',
                     title="Feature Importance",
                     color='Importance Score',
                     color_continuous_scale=px.colors.diverging.RdYlGn)
        fig.update_layout(yaxis=dict(tickfont=dict(size=8)), 
                          title_x=0.5,)

        fig.write_image("Model_Feature_Importance/Feature_Importance_Plot/model_feature_importance.png")

        return None