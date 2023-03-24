#################### Libraries ####################
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import warnings
warnings.filterwarnings("ignore")
from app import app
import dash_daq as daq

from read_in_data.read_in_datasets import Read_Data


#################### Datasets ####################
read_data=Read_Data()
df=read_data.loan_data_to_pandas_df()
counties=read_data.read_in_geojson_data()

average_loan_amount=round(df['Current Approval Amount'].mean(), 0)
num_loans_given=len(df['Current Approval Amount'])
average_forgiveness=round(df['Forgiveness Amount'].mean(), 0)


#################### Layout ####################
layout=html.Div([html.Div(children=[html.H5("Project Overview"),
                                    html.P('''The Small Business Administration created the Paycheck Protection Program referred to 
                                    as the PPP, intended to give business owners that qualified for these loans the chance to keep 
                                    the workforce employed during the COVID-19 pandemic. With this in mind, it has come to 
                                    light recently that there was a lot of fraud committed to attain these loans and fraud 
                                    committed during the money disbursement of the loans. As a result I will use data science 
                                    and machine learning to create a fraud detection system using unlabeled data and basing the 
                                    analysis in identifying fraud on an XGBoost Regression model where the residuals that are 
                                    standardized will be used to identify fraudulent loans.''')],
                          style = {'padding' : '10px',
                                   'text-align': 'center'}),



            html.Div(dcc.Graph(id = "market gauge",
                              figure = {"data": [go.Indicator(
                                                                title = {"text": "Average Loan Amount", "font": {"color": 'white'}},
                                                                mode = "number",
                                                                number = {"font": {"color": 'green'}, 'valueformat':'f', 'prefix': "$"},
                                                                value =average_loan_amount,
                                                                domain = {'x': [0, 1], 'y': [0, 1]})],
                                        "layout": go.Layout(height = 150,
                                                            paper_bgcolor='rgba(0, 0, 0, 0)')
                                                                        }),
                      style = {'display': 'inline-block', 'verticalAlign': 'top', 'width': '33.33%', 'padding':'0px'}),



            html.Div(dcc.Graph(id = "market gauge",
                              figure = {"data": [go.Indicator(
                                                                title = {"text": "Average Forgiveness Amount", "font": {"color": 'white'}},
                                                                mode = "number",
                                                                number = {"font": {"color": 'red'}, 'valueformat':'f', 'prefix': "$"},
                                                                value = average_forgiveness,
                                                                domain = {'x': [0, 1], 'y': [0, 1]})],
                                        "layout": go.Layout(height = 150,
                                                            paper_bgcolor='rgba(0, 0, 0, 0)')
                                                                        }),
                      style = {'display': 'inline-block', 'verticalAlign': 'top', 'width': '33.33%', 'padding':'0px'}),


            html.Div(dcc.Graph(id = "market gauge",
                              figure = {"data": [go.Indicator(
                                                                title = {"text": "Number of Loans Given", "font": {"color": 'white'}},
                                                                mode = "number",
                                                                number = {"font": {"color": 'white'}, 'valueformat':'f'},
                                                                value = num_loans_given,
                                                                domain = {'x': [0, 1], 'y': [0, 1]})],
                                        "layout": go.Layout(height = 150,
                                                            paper_bgcolor='rgba(0, 0, 0, 0)')
                                                                        }),
                      style = {'display': 'inline-block', 'verticalAlign': 'top', 'width': '33.33%', 'padding':'0px'}),







                          ])