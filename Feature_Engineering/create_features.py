
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