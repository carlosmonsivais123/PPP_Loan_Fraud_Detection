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