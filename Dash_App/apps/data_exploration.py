#################### Libraries ####################
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.figure_factory as ff
import pandas as pd
import warnings
warnings.filterwarnings("ignore")
from app import app
from dash import dash_table
import numpy as np

from read_in_data.read_in_datasets import Read_Data


#################### Datasets ####################
read_data=Read_Data()
df=read_data.loan_data_to_pandas_df()
counties=read_data.read_in_geojson_data()

industry_types=df['Industry Type'].unique().tolist()

################### Static Figures ################
approval_amount_industry=df.groupby(['Industry Type'])['Current Approval Amount'].mean().reset_index().\
    sort_values(by='Current Approval Amount', ascending=True)
ind_avg_fig=px.bar(approval_amount_industry, 
            y="Industry Type", 
            x="Current Approval Amount",
            text_auto='.2s', 
            title="Average Loan Amount by Industry", 
            color='Current Approval Amount', 
            orientation='h')
ind_avg_fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
ind_avg_fig.update_layout(yaxis=dict(tickfont=dict(size=8)), 
                    title_x=0.5,
                    yaxis_title="Industry Type")
ind_avg_fig.update_layout({'title_x':0.5,
                    'font_color': 'white',
                    'plot_bgcolor': 'rgba(0, 0, 0, 0)',
                    'paper_bgcolor': 'rgba(0, 0, 0, 0)'})
ind_avg_fig.for_each_xaxis(lambda x: x.update(showgrid=False))
ind_avg_fig.for_each_yaxis(lambda x: x.update(showgrid=False))


approval_count_industry=df.groupby(['Industry Type'])['Current Approval Amount'].count().reset_index().\
    sort_values(by='Current Approval Amount', ascending=True).rename(columns={'Current Approval Amount': 'Number of Loans Approved'})
ind_num_fig=px.bar(approval_count_industry, 
            y="Industry Type", 
            x='Number of Loans Approved',
            text_auto='.2s', 
            title="Number of Loans Approved by Industry", 
            color='Number of Loans Approved', 
            orientation='h')
ind_num_fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
ind_num_fig.update_layout(yaxis=dict(tickfont=dict(size=8)), 
                    title_x=0.5,
                    yaxis_title="Industry Type")
ind_num_fig.update_layout({'title_x':0.5,
                    'font_color': 'white',
                    'plot_bgcolor': 'rgba(0, 0, 0, 0)',
                    'paper_bgcolor': 'rgba(0, 0, 0, 0)'})
ind_num_fig.for_each_xaxis(lambda x: x.update(showgrid=False))
ind_num_fig.for_each_yaxis(lambda x: x.update(showgrid=False))



count_df=df.groupby([df['Date Approved'].dt.strftime('%Y-%m-%d')])['Current Approval Amount'].count().\
    reset_index().rename(columns={'Current Approval Amount': 'Current Approval Amount Count'}).sort_values(by='Date Approved', ascending=True)

count_df['Date Approved']=pd.to_datetime(count_df['Date Approved'], format='%Y-%m-%d')

fig1=px.bar(count_df, 
            x='Date Approved', 
            y='Current Approval Amount Count',
            title='Number of Loans Approved Daily',
            color='Current Approval Amount Count')

fig1.update_layout({'title_x':0.5,
                    'font_color': 'white',
                    'plot_bgcolor': 'rgba(0, 0, 0, 0)',
                    'paper_bgcolor': 'rgba(0, 0, 0, 0)'})
fig1.for_each_xaxis(lambda x: x.update(showgrid=False))
fig1.for_each_yaxis(lambda x: x.update(showgrid=False))



amount_df=df.groupby([df['Date Approved'].dt.strftime('%Y-%m-%d')])['Current Approval Amount'].sum().\
    reset_index().rename(columns={'Current Approval Amount': 'Current Approval Amount Sum'}).sort_values(by='Date Approved', ascending=True)

count_df['Date Approved']=pd.to_datetime(count_df['Date Approved'], format='%Y-%m-%d')

fig2=px.bar(amount_df, 
            x='Date Approved', 
            y='Current Approval Amount Sum',
            title='Number of Loans Approved Daily',
            color='Current Approval Amount Sum')

fig2.update_layout({'title_x':0.5,
                    'font_color': 'white',
                    'plot_bgcolor': 'rgba(0, 0, 0, 0)',
                    'paper_bgcolor': 'rgba(0, 0, 0, 0)'})
fig2.for_each_xaxis(lambda x: x.update(showgrid=False))
fig2.for_each_yaxis(lambda x: x.update(showgrid=False))






category_spend=pd.DataFrame(df[['Utilities Proceed',
       'Payroll Proceed', 'Mortgage Interest Proceed', 'Rent Proceed',
       'Refinance EIDL Proceed', 'Health Care Proceed',
       'Debt Interest Proceed']].\
                                    sum(axis=0)).\
                                        reset_index(drop=False).\
                                            rename(columns={'index':'Spend Categories', 0:'Amount Spent'}).\
                                                sort_values(by='Amount Spent', ascending=False)

fig3=px.bar(category_spend, 
            x="Spend Categories", 
            y="Amount Spent", 
            color="Spend Categories", 
            title="Spending by Categories",
            text_auto=True)
fig3.update_layout({'title_x':0.5,
                    'showlegend': False, 
                    'font_color': 'white',
                    'plot_bgcolor': 'rgba(0, 0, 0, 0)',
                    'paper_bgcolor': 'rgba(0, 0, 0, 0)'})
fig3.for_each_xaxis(lambda x: x.update(showgrid=False))
fig3.for_each_yaxis(lambda x: x.update(showgrid=False))




#################### Layout ####################
layout=html.Div([html.Div(children=[html.H5("Data Exploration"),
                                    html.P('''Here we can see some initial data exploration''')],
                          style = {'padding' : '10px',
                                   'text-align': 'center', 'whiteSpace': 'pre-wrap'}),

                 html.Div(className="section-banner", 
                          children='Loan Counts and Amounts Given'),


                 html.Div(children=[dcc.Graph(figure=fig1)],
                          style = {'display': 'inline-block', 'verticalAlign': 'top',  'padding':'0px', "width": "100%"}),

                 html.Div(children=[dcc.Graph(figure=fig2)],
                          style = {'display': 'inline-block', 'verticalAlign': 'top',  'padding':'0px', "width": "100%"}),


                 html.Div(className="section-banner", 
                          children='Where Loan Disbursements Went'),

                 html.Div(children=[dcc.Graph(figure=fig3)],
                          style = {'display': 'inline-block', 'text-align': 'center', 
                                   'verticalAlign': 'top',  'padding':'0px', "width": "100%"}),

                 html.Div(className="section-banner", 
                          children='Loans By Industry'),

                 html.Div(children=[dcc.Graph(figure=ind_avg_fig)],
                          style = {'display': 'inline-block', 'verticalAlign': 'top',  'padding':'0px', "width": "50%"}),

                 html.Div(children=[dcc.Graph(figure=ind_num_fig)],
                          style = {'display': 'inline-block', 'verticalAlign': 'top',  'padding':'0px', "width": "50%"}),

                          ])
