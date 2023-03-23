class Data_Split:
    def split_data_x_y(self, data):
        X=data.drop(['remainder__LoanNumber', 'numerical__Loan_Amount_Owed'], axis=1)
        y=data['numerical__Loan_Amount_Owed']

        return X, y