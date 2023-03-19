import plotly.graph_objects as go
import plotly.express as px
import plotly.figure_factory as ff

import seaborn as sns
import matplotlib.pyplot as plt

import numpy as np
import pandas as pd


class EDA_Outputs:
    def eda_plots_missing_values_heatmap(self, data):
        fig, ax = plt.subplots(figsize=(15,15)) 
        sns.heatmap(data.isnull(),
                    cbar=False,
                    cmap='viridis').set(title='Missing Values by Column and Row',
                                        xlabel='Column',
                                        ylabel='Row')
        fig.savefig("Plots_Storage/EDA_Plots/missing_values_heatmap.png")

        return None
    
    def eda_correlation_heatmap(self, data):
        corr=data.corr(method='pearson', numeric_only=True)
        corr=corr.dropna(axis=1, how='all')
        corr=corr.dropna(axis=0, how='all')
       
        mask=np.triu(np.ones(corr.shape, dtype=bool))
        df_mask = corr.mask(mask)

        fig = ff.create_annotated_heatmap(z=df_mask.to_numpy(), 
                                          x=df_mask.columns.tolist(),
                                          y=df_mask.columns.tolist(),
                                          annotation_text = np.around(df_mask.to_numpy(), decimals=2),
                                          colorscale=px.colors.diverging.RdBu,
                                          showscale=True, 
                                          ygap=1, 
                                          xgap=1)

        fig.update_xaxes(side="bottom")
        fig.update_layout(title_text='Correlation Heatmap', 
                          title_x=0.5, 
                          width=1000, 
                          height=1000,
                          xaxis_showgrid=False,
                          yaxis_showgrid=False,
                          xaxis_zeroline=False,
                          yaxis_zeroline=False,
                          yaxis_autorange='reversed',
                          template='plotly_white')

        for i in range(len(fig.layout.annotations)):
            if fig.layout.annotations[i].text == 'nan':
                fig.layout.annotations[i].text = ""

        fig.show()
        fig.write_image("Plots_Storage/EDA_Plots/correlation_heatmap.png")

        return None