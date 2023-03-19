import pandas as pd
df=pd.read_csv('data/public_150k_plus_230101.csv')

print(df)

print(df.columns)

print(df['CurrentApprovalAmount'].min())
print(df['CurrentApprovalAmount'].max())


print(df[['UTILITIES_PROCEED',
       'PAYROLL_PROCEED', 'MORTGAGE_INTEREST_PROCEED', 'RENT_PROCEED',
       'REFINANCE_EIDL_PROCEED', 'HEALTH_CARE_PROCEED',
       'DEBT_INTEREST_PROCEED']])