import plotly.express as px
import plotly.figure_factory as ff
import plotly.express as px

import seaborn as sns
import matplotlib.pyplot as plt

import numpy as np
import pandas as pd


class EDA_Outputs:
    def eda_plots_missing_values_heatmap(self, data):
        fig, ax=plt.subplots(figsize=(15,15)) 
        sns.heatmap(data.isnull(),
                    cbar=False,
                    cmap='viridis').set(title='Missing Values by Column and Row',
                                        xlabel='Column',
                                        ylabel='Row')
        fig.savefig("Plots_Storage/EDA_Plots/missing_values_heatmap.png")
        plt.close()

        return None
    
    def eda_correlation_heatmap(self, data):
        corr=data.corr(method='pearson', numeric_only=True)
        corr=corr.dropna(axis=1, how='all')
        corr=corr.dropna(axis=0, how='all')
       
        mask=np.triu(np.ones(corr.shape, dtype=bool))
        df_mask = corr.mask(mask)

        fig=ff.create_annotated_heatmap(z=df_mask.to_numpy(), 
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

        fig.write_image("Plots_Storage/EDA_Plots/correlation_heatmap.png")

        return None
    
    def eda_mapping_industries_and_count(self, data):
        loan_counts_by_indsutry=data.groupby(['Industry_Type']).size().reset_index().rename(columns={0:'Count'}).sort_values(by='Count', ascending=True)

        fig=px.bar(loan_counts_by_indsutry, 
                   x='Count', 
                   y='Industry_Type', 
                   text_auto='.2s', 
                   title="Amount of Loans Given Out Per Industry Type", 
                   color='Count', 
                   orientation='h')
        fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
        fig.update_layout(yaxis=dict(tickfont=dict(size=8)), 
                          title_x=0.5,
                          yaxis_title="Industry Type")

        fig.write_image("Plots_Storage/EDA_Plots/loan_count_barchart.png")
        
        return None
    
    def eda_spread_by_gender(self, data):
        fig=px.strip(data, 
                     x='Gender', 
                     y='CurrentApprovalAmount',
                     title="Loan Current Approval Amount by Gender",
                     color='Gender')
        fig.update_layout(title_x=0.5)
        fig.write_image("Plots_Storage/EDA_Plots/approval_amount_spread_by_gender.png")

        return None
    
    def eda_average_loan_amount_by_industry_and_gender(self, data):
        approval_amount_industry_gender=data.groupby(['Industry_Type', 'Gender'])['CurrentApprovalAmount'].mean().reset_index()
        fig=px.histogram(approval_amount_industry_gender, 
                         y="Industry_Type", 
                         x="CurrentApprovalAmount",
                         color='Gender', 
                         barmode='group',
                         title="Average Loan Amount by Industry Per Gender",
                         orientation='h',
                         height=800,
                         width=1200)

        fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
        fig.update_layout(yaxis=dict(tickfont=dict(size=10)), 
                          title_x=0.5,
                          xaxis_title="Average Loan Amount",
                          yaxis_title="Industry Type")
        
        fig.write_image("Plots_Storage/EDA_Plots/average_loan_amount_by_industry_and_gender.png")

        return None
    
    def eda_average_loan_amount_by_lmi_indicator_by_industry(self, data):
        lmi_indicator_by_industry_type=data.groupby(['Industry_Type', 'LMIIndicator'])['CurrentApprovalAmount'].mean().reset_index()
        fig=px.bar(lmi_indicator_by_industry_type, 
                   x="Industry_Type", 
                   y="CurrentApprovalAmount",
                   title="Average Current Approval Amount by Lower Middle Income Indicator", 
                   color="LMIIndicator",
                   barmode='group',)
        fig.update_layout(xaxis=dict(tickfont=dict(size=8)), 
                          title_x=0.5,
                          xaxis_title="Industry Type",
                          yaxis_title="Average Current Approval Amount",
                          legend_title="Lower Middle Income Indicator",
                          legend=dict(font=dict(size=9), 
                                      orientation="h",
                                      entrywidth=70,
                                      yanchor="bottom",
                                      y=1.02,
                                      xanchor="right",
                                      x=0.90))
        
        fig.write_image("Plots_Storage/EDA_Plots/average_loan_amount_by_lmi_indicator_by_industry.png")

        return None
        

    def eda_average_loan_amount_by_hubzone_indicator_by_industry(self, data):
        hbzi_indicator_by_industry_type=data.groupby(['Industry_Type', 'HubzoneIndicator'])['CurrentApprovalAmount'].mean().reset_index()
        fig=px.bar(hbzi_indicator_by_industry_type, 
                   x="Industry_Type", 
                   y="CurrentApprovalAmount",
                   title="Average Current Approval Amount by Historically Under-utilized Business Zones", 
                   color="HubzoneIndicator",
                   barmode='group',)
        fig.update_layout(xaxis=dict(tickfont=dict(size=8)), 
                          title_x=0.5,
                          title=dict(font=dict(size=12)),
                          xaxis_title="Industry Type",
                          yaxis_title="Average Current Approval Amount",
                          legend_title="Historically Under-utilized Business Zones Indicator",
                          legend=dict(font=dict(size=7), 
                                      orientation="h",
                                      entrywidth=70,
                                      yanchor="bottom",
                                      y=1.02,
                                      xanchor="right",
                                      x=0.90))
        
        fig.write_image("Plots_Storage/EDA_Plots/average_loan_amount_by_hubzone_indicator_by_industry.png")

        return None
    

    def eda_state_loan_count(self, data):
        state_loan_count=data.groupby(['BorrowerState'])['CurrentApprovalAmount'].\
            count().reset_index().rename(columns={'CurrentApprovalAmount': 'Number of Loans'})

        fig=px.choropleth(locations=state_loan_count['BorrowerState'], 
                          locationmode="USA-states", 
                          color=state_loan_count['Number of Loans'],
                          color_continuous_scale=px.colors.sequential.Blues, 
                          title='Number of Loans Approved per State',
                          scope="usa")
        
        fig.update_layout(title_x=0.5,
                          title=dict(font=dict(size=15)),
                          coloraxis_colorbar=dict(title="Number of Loans"))
        fig.update_coloraxes(colorbar_title_font_size=10)
        
        fig.write_image("Plots_Storage/EDA_Plots/state_loan_count.png")

        return None


    def eda_state_loan_avg_amount(self, data):
        state_loan_avg_amount=data.groupby(['BorrowerState'])['CurrentApprovalAmount'].\
            mean().reset_index().rename(columns={'CurrentApprovalAmount': 'Average Loan Amount'})

        fig=px.choropleth(locations=state_loan_avg_amount['BorrowerState'], 
                          locationmode="USA-states", 
                          color=state_loan_avg_amount['Average Loan Amount'],
                          color_continuous_scale=px.colors.sequential.Blues, 
                          title='Average Loan Amount Approved per State',
                          scope="usa")
        
        fig.update_layout(title_x=0.5,
                          title=dict(font=dict(size=15)),
                          coloraxis_colorbar=dict(title="Average Loan Amount"))
        fig.update_coloraxes(colorbar_title_font_size=10)
        
        fig.write_image("Plots_Storage/EDA_Plots/state_loan_avg_amount.png")

        return None

    
    def eda_zip_loan_count(self, data, counties):
        zip5_loan_count=data.groupby(['zip5'])['CurrentApprovalAmount'].\
            count().reset_index().rename(columns={'CurrentApprovalAmount': 'loan_amount_count'})

        fig=px.choropleth(zip5_loan_count, 
                          geojson=counties, 
                          locations='zip5', 
                          color='loan_amount_count',
                          color_continuous_scale="Viridis",
                          title='Number of Loans Approved per FIPS Code',
                          scope="usa")
        
        fig.update_layout(title_x=0.5,
                          title=dict(font=dict(size=15)),
                          coloraxis_colorbar=dict(title="Number of Loans"))
        fig.update_coloraxes(colorbar_title_font_size=10)

        fig.write_image("Plots_Storage/EDA_Plots/fips_code_loan_count.png")

        return None


    def eda_zip_loan_avg(self, data, counties):
        zip5_loan_mean=data.groupby(['zip5'])['CurrentApprovalAmount'].\
            mean().reset_index().rename(columns={'CurrentApprovalAmount': 'loan_amount_mean'})

        fig=px.choropleth(zip5_loan_mean, 
                          geojson=counties, 
                          locations='zip5', 
                          color='loan_amount_mean',
                          color_continuous_scale="Viridis",
                          title='Average Loan Amount Approved per FIPS Code',
                          scope="usa")
        
        fig.update_layout(title_x=0.5,
                          title=dict(font=dict(size=15)),
                          coloraxis_colorbar=dict(title="Average Loan Amount"))
        fig.update_coloraxes(colorbar_title_font_size=10)

        fig.write_image("Plots_Storage/EDA_Plots/fips_code_loan_avg_amount.png")
        
        return None
    

    def eda_time_series_gender_loan_amount(self, data):
        fig=px.scatter(data, 
                       x="DateApproved", 
                       y="CurrentApprovalAmount", 
                       title='Loan Amount Approval By Gender Over Time',
                       color='Gender')

        fig.update_layout(title_x=0.5)

        fig.write_image("Plots_Storage/EDA_Plots/loan_amount_gender_over_time.png")

        return None
    

    def eda_time_series_loan_amount(self, data):
        fig=px.scatter(data, 
                       x="DateApproved", 
                       y="CurrentApprovalAmount", 
                       title='Loan Amount Approval Over Time',
                       color='CurrentApprovalAmount',
                       color_continuous_scale="RdBu",)

        fig.update_layout(title_x=0.5,
                          coloraxis_colorbar=dict(title="Loan Amount"))

        fig.write_image("Plots_Storage/EDA_Plots/loan_amount_over_time.png")

        return None