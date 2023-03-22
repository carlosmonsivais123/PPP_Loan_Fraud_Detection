class Clean_Data:
    def remove_nulls_based_on_columns(self, data):
        data=data.dropna(subset=['BorrowerAddress', 
                                 'BorrowerCity', 
                                 'BorrowerState', 
                                 'BorrowerZip', 
                                 'ForgivenessAmount', 
                                 'BusinessAgeDescription',
                                 'JobsReported'], 
                         how='any')
        
        data=data.reset_index(drop=True)
        
        return data
    
    def remove_usa_territories(self, data):
        us_territories=['AS', 'GU', 'MP', 'PR', 'VI']
        data=data[~data['BorrowerState'].isin(us_territories)]

        return data