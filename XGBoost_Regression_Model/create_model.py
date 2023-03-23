from xgboost.sklearn import XGBRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import r2_score, mean_squared_error

class Create_Model:
    def create_xgboost_model(self, X, y):
        xgb=XGBRegressor()
        parameters={'objective':['reg:squarederror'],
                    'learning_rate': [0.1, 0.01],
                    'eval_metric': [r2_score, mean_squared_error],
                    'random_state': [21]}

        xgb_grid=GridSearchCV(xgb,
                              parameters,
                              cv=5,
                              verbose=True,
                              error_score='raise',
                              refit=True)

        xgb_grid.fit(X, y)

        xgb_grid.best_estimator_.save_model('XGBoost_Regression_Model/Saved_Model/xgboost_model1.json')

        return xgb_grid.best_estimator_