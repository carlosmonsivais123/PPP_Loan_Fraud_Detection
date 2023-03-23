class Create_Features:
    def mapping_industries(self, data):
        data['Industry_Type']=data['NAICSCode'].astype(str).str[:2]

        industry_mapping_dictionary={'11': 'Agriculture, Forestry, Fishing and Hunting',
                                     '21': 'Mining, Quarrying, and Oil and Gas Extraction',
                                     '22': 'Utilities',
                                     '23': 'Construction',
                                     '31': 'Manufacturing',
                                     '32': 'Manufacturing',
                                     '33': 'Manufacturing',
                                     '42': 'Wholesale Trade',
                                     '44': 'Retail Trade', 
                                     '45': 'Retail Trade', 
                                     '48': 'Transportation and Warehousing', 
                                     '49': 'Transportation and Warehousing', 
                                     '51': 'Information', 
                                     '52': 'Finance and Insurance', 
                                     '53': 'Real Estate and Rental and Leasing',
                                     '54': 'Professional, Scientific, and Technical Services', 
                                     '55': 'Management of Companies and Enterprises',
                                     '56': 'Administrative and Support and Waste Management and Remediation Services',
                                     '61': 'Educational Services', 
                                     '62': 'Health Care and Social Assistance', 
                                     '71': 'Arts, Entertainment, and Recreation', 
                                     '72': 'Accommodation and Food Services', 
                                     '81': 'Other Services (except Public Administration)', 
                                     '92': 'Public Administration',
                                     '99': 'Nonclassifiable Establishments',
                                     'na': 'No Response'}

        data['Industry_Type']=data['Industry_Type'].map(industry_mapping_dictionary)

        return data
    

    def number_of_loans(self, data):
        loan_count_feature=data.groupby('BorrowerName').count()['LoanNumber'].reset_index().rename(columns={'LoanNumber':'Loan_Count'})
        data=data.merge(loan_count_feature, 
                        left_on='BorrowerName', 
                        right_on='BorrowerName', 
                        how='left')
        
        return data


    def amount_of_loan_forgiven(self, data):
        data['Loan_Amount_Owed']=data['ForgivenessAmount']-data['CurrentApprovalAmount']

        return data
    

    def revised_loan_amount(self, data):
        data['Revised_Loan_Amount']=data['CurrentApprovalAmount']-data['InitialApprovalAmount']

        return data
    

    def days_with_loan_approval(self, data):
        data['Days_With_Loan']=(data['ForgivenessDate']-data['DateApproved']).dt.days

        return data
    
    
    def create_borrower_zip5(self, data):
        data['Borrower_ZIP5']=data['BorrowerZip'].str[0:5]

        return data
    

    def create_lender_zip5(self, data):
        data['Servicing_Lender_ZIP5']=data['ServicingLenderZip'].str[0:5]

        return data