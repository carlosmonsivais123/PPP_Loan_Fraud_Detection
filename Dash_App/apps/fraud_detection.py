#################### Libraries ####################
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import warnings
warnings.filterwarnings("ignore")
from app import app
from dash import dash_table
import dash
import json

from read_in_data.read_in_datasets import Read_Data


#################### Datasets ####################
read_data=Read_Data()
df=read_data.loan_data_to_pandas_df()
counties=read_data.read_in_geojson_data()
fraud_df=df[df['Fraud Detection']=='Fraud'].reset_index(drop=True)
industry_types=fraud_df['Industry Type'].unique().tolist()


fraud_count_industry=fraud_df.groupby(['Industry Type'])['Fraud Detection'].count().\
    reset_index(drop=False).rename(columns={'Fraud Detection': 'Fraud Detection Count'}).\
        sort_values(by=['Fraud Detection Count'], ascending=True)
industry_count=df.groupby(['Industry Type'])['Loan Number'].count().reset_index(drop=False).rename(columns={'Loan Number': 'Loan Number Count'})

fraud_count_industry=pd.merge(fraud_count_industry, industry_count, on='Industry Type')

fraud_count_industry['Fraud Proportion']=fraud_count_industry['Fraud Detection Count']/fraud_count_industry['Loan Number Count']
fraud_count_industry['Fraud Proportion']=round(fraud_count_industry['Fraud Proportion']*100, 2)

################### Static Figures ################
fraud_count_state_code=fraud_df.groupby(['Borrower State'])['Fraud Detection'].count().\
            reset_index().rename(columns={'Fraud Detection': 'Fraud Detection Count'})
geo_state_count_fig=px.choropleth(locations=fraud_count_state_code['Borrower State'].values, 
                                  locationmode="USA-states", 
                                  title='Fraud Cases Per State',
                                  color=fraud_count_state_code['Fraud Detection Count'].values, 
                                  color_continuous_scale=px.colors.diverging.RdYlGn_r,
                                  scope="usa")
geo_state_count_fig.update_layout({'title_x':0.5,
                    'font_color': 'white',
                    'plot_bgcolor': 'rgba(0, 0, 0, 0)',
                    'paper_bgcolor': 'rgba(0, 0, 0, 0)'})



fraud_count_zip_code=fraud_df.groupby(['Borrower ZIP5'])['Fraud Detection'].count().\
    reset_index().rename(columns={'Fraud Detection': 'Fraud Detection Count'})
geo_zip_count_fig=px.choropleth(fraud_count_zip_code, 
                                geojson=counties, 
                                locations='Borrower ZIP5', 
                                color='Fraud Detection Count',
                                color_continuous_scale=px.colors.diverging.RdYlGn_r,
                                title='Fraud Cases Per Zip5',
                                scope="usa")
geo_zip_count_fig.update_layout({'title_x':0.5,
                    'font_color': 'white',
                    'plot_bgcolor': 'rgba(0, 0, 0, 0)',
                    'paper_bgcolor': 'rgba(0, 0, 0, 0)'})


outliers_fig=px.scatter(fraud_df, 
                        x="Date Approved", 
                        y="Current Approval Amount", 
                        title='Fraudulent Loans',
                        color='Current Approval Amount')
outliers_fig.update_layout({'title_x':0.5,
                            'font_color': 'white',
                            'plot_bgcolor': 'rgba(0, 0, 0, 0)',
                            'paper_bgcolor': 'rgba(0, 0, 0, 0)'})



#################### Layout ####################
layout=html.Div([html.Div(children=[html.H5("Fraud Detection Results"),
                                    html.P('''These are the fraudelent cases that were detected, where we can analyze at the individual loan level and aggregated at ZIP 5 and State level.''')],
                          style = {'padding' : '10px',
                                   'text-align': 'center', 'whiteSpace': 'pre-wrap'}),

                 html.Div(className="section-banner", 
                          children='Fraud Case Count'),

                 html.Div([dcc.DatePickerRange(id="date_picker",
                                               start_date=df['Date Approved'].min().date(),
                                               end_date=df['Date Approved'].max().date(),
                                               min_date_allowed=df['Date Approved'].min().date(),
                                               max_date_allowed=df['Date Approved'].max().date(),
                                               display_format='MMMM Y, DD',
                                               clearable=True,
                                               with_portal=False,
                                               start_date_placeholder_text='MMMM Y, DD')], 
                                               style={'text-align':'center', 'display': 'inline-block', 
                                                      'verticalAlign': 'top', 'width': '50%', 'padding':'0px',
                                                      'backgroundColor' : 'rgba(0, 0, 0, 0)'}),


                 html.Div([dcc.RadioItems(id='radio_monthly_daily',
                                          options=[{'label': 'Daily', 'value': 'Daily'},
                                                   {'label': 'Monthly', 'value': 'Monthly'}],
                                          value='Daily',
                                          inline=True)], 
                                          style={'text-align':'center', 'display': 'inline-block', 
                                                 'verticalAlign': 'top', 'width': '50%', 'padding':'0px'}),

                 html.Div(children=[dcc.Graph(id='fraud_count')],
                          style = {'display': 'inline-block', 'verticalAlign': 'top',  'padding':'0px', "width": "100%"}),

                 html.Div(className="section-banner", 
                          children='Fraud Case Count by Geography'),

                 html.Div(children=[dcc.Graph(figure=geo_state_count_fig)],
                          style = {'display': 'inline-block', 'verticalAlign': 'top',  'padding':'0px', "width": "50%"}),

                 html.Div(children=[dcc.Graph(figure=geo_zip_count_fig)],
                          style = {'display': 'inline-block', 'verticalAlign': 'top',  'padding':'0px', "width": "50%"}),
                           
                 html.Div(className="section-banner", 
                          children='Fraud Case by Industry Type'),                          
                          
                 html.Div([dcc.Dropdown(id='industry_type_dropdown',
                                        options=industry_types,
                                        value=industry_types,
                                        multi=True)]),

                 html.Div(children=[dcc.Graph(id='industry_counts')],
                          style = {'display': 'inline-block', 'verticalAlign': 'top',  'padding':'0px', "width": "50%"}),

                 html.Div(children=[dcc.Graph(id='industry_prop')],
                          style = {'display': 'inline-block', 'verticalAlign': 'top',  'padding':'0px', "width": "50%"}),


                 html.Div(className="section-banner", 
                          children='Fraudulent Data Points'), 

                html.Div(children=[html.P('Click on the scatterplot points to produce a data below')],
                                        style = {'padding' : '20px',
                                                'text-align': 'left', 'whiteSpace': 'pre-wrap'}),

                 html.Div(children=[dcc.Graph(id='fraud_scatter', figure=outliers_fig)],
                          style = {'display': 'inline-block', 'verticalAlign': 'top',  'padding':'0px', "width": "100%"}),

                 html.Div(id='table',
                          style = {'display': 'inline-block', 'verticalAlign': 'top',  'padding':'0px', "width": "100%"}),
                          ])

# #################### Callbacks ####################
@app.callback(Output('fraud_count', 'figure'),
              [Input('radio_monthly_daily', 'value'),
               Input('date_picker', 'start_date'),
               Input('date_picker', 'end_date')])
def fraud_count_group(selected_value, start_date, end_date):
    if selected_value=='Daily':
           date_format='''%Y-%m-%d'''
           title='Fraud Cases Per Day'

    elif selected_value=='Monthly':
        date_format='''%Y-%m'''
        title='Fraud Cases Per Month'

    date_df=fraud_df.loc[fraud_df["Date Approved"].between(*pd.to_datetime([start_date, end_date]))]

    fraud_count=date_df.groupby([date_df['Date Approved'].dt.strftime(date_format)])['Fraud Detection'].count().\
        reset_index().rename(columns={'Fraud Detection': 'Fraud Detection Count'}).sort_values(by='Date Approved', ascending=True)

    fraud_count['Date Approved']=pd.to_datetime(fraud_count['Date Approved'], format=date_format)

    fig=px.bar(fraud_count, 
               x='Date Approved', 
               y='Fraud Detection Count',
               title=title,
               color='Fraud Detection Count')

    fig.update_layout({'title_x':0.5,
                       'font_color': 'white',
                      'plot_bgcolor': 'rgba(0, 0, 0, 0)',
                      'paper_bgcolor': 'rgba(0, 0, 0, 0)'})
    fig.for_each_xaxis(lambda x: x.update(showgrid=False))
    fig.for_each_yaxis(lambda x: x.update(showgrid=False))

    return fig

@app.callback(Output('industry_counts', 'figure'),
              [Input('industry_type_dropdown', 'value')])
def fraud_count_group(selected_value):
    fraud_count_industry_dyanmic=fraud_count_industry[fraud_count_industry['Industry Type'].isin(selected_value)]

    fig=px.bar(fraud_count_industry_dyanmic, 
                x='Fraud Detection Count', 
                y='Industry Type', 
                text_auto='.2s', 
                title="Fraudelent Loans Detected Per Industry", 
                color='Fraud Detection Count', 
                orientation='h')
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    fig.update_layout(yaxis=dict(tickfont=dict(size=8)), 
                        title_x=0.5,
                        yaxis_title="Industry Type")

    fig.update_layout({'title_x':0.5,
                       'font_color': 'white',
                      'plot_bgcolor': 'rgba(0, 0, 0, 0)',
                      'paper_bgcolor': 'rgba(0, 0, 0, 0)'})
    fig.for_each_xaxis(lambda x: x.update(showgrid=False))
    fig.for_each_yaxis(lambda x: x.update(showgrid=False))

    return fig

@app.callback(Output('industry_prop', 'figure'),
              [Input('industry_type_dropdown', 'value')])
def fraud_count_group(selected_value):
    fraud_prop_industry_dyanmic=fraud_count_industry[fraud_count_industry['Industry Type'].isin(selected_value)]

    fig=px.bar(fraud_prop_industry_dyanmic, 
                x='Fraud Proportion', 
                y='Industry Type', 
                text_auto='.2s', 
                title="Fraudelent Loans Detected Per Industry by Proportion", 
                color='Fraud Proportion', 
                orientation='h')
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    fig.update_layout(yaxis=dict(tickfont=dict(size=8)), 
                        title_x=0.5,
                        yaxis_title="Industry Type")

    fig.update_layout({'title_x':0.5,
                       'font_color': 'white',
                      'plot_bgcolor': 'rgba(0, 0, 0, 0)',
                      'paper_bgcolor': 'rgba(0, 0, 0, 0)'})
    fig.for_each_xaxis(lambda x: x.update(showgrid=False))
    fig.for_each_yaxis(lambda x: x.update(showgrid=False))

    return fig

@app.callback(Output("table", "children"),
              [Input("fraud_scatter", "clickData")])
def click(clickData):
    if not clickData:
        raise dash.exceptions.PreventUpdate
    
    date_selection=clickData['points'][0]['x']
    value_selection=clickData['points'][0]['y']

    if clickData != 'null':
        filtered_data=fraud_df[(fraud_df['Date Approved']==date_selection) & (fraud_df['Current Approval Amount']==value_selection)]
        filtered_data=filtered_data[['Loan Number', 'Date Approved', 'Borrower Name', 'Borrower City',
                                     'Borrower State', 'Current Approval Amount', 'Servicing Lender Name',
                                     'Industry Type', 'Predicted Loan Amount Owed',
                                     'Actual Loan Amount Owed']]
        
        filtered_data['Date Approved']=pd.to_datetime(filtered_data['Date Approved']).dt.date

        table=dash_table.DataTable(columns=[{"name": i, "id": i} for i in filtered_data.columns],
                                   data=filtered_data.to_dict('records'),
                                   style_cell={'textAlign': 'center',
                                               'font_size': '9px'},
                                   style_data={'color': 'white',
                                               'backgroundColor': 'rgba(0, 0, 0, 0)'},
                                   style_header={'backgroundColor': 'rgba(0, 0, 0, 0)',
                                                 'color': 'white'},
                                   style_table={'overflowY': 'scroll',
                                                'overflowX': 'scroll'})
        
    else:
        filtered_data=fraud_df[['Loan Number', 'Date Approved', 'Borrower Name', 'Borrower City',
                                'Borrower State', 'Current Approval Amount', 'Servicing Lender Name',
                                'Industry Type', 'Predicted Loan Amount Owed',
                                'Actual Loan Amount Owed']]
        filtered_data['Date Approved']=pd.to_datetime(filtered_data['Date Approved']).dt.date
        table=dash_table.DataTable(columns=[{"name": i, "id": i} for i in filtered_data.columns],
                                   data=filtered_data.to_dict('records'),
                                   style_cell={'textAlign': 'center',
                                               'font_size': '9px'},
                                   style_data={'color': 'white',
                                               'backgroundColor': 'rgba(0, 0, 0, 0)'},
                                   style_header={'backgroundColor': 'rgba(0, 0, 0, 0)',
                                                 'color': 'white'},
                                   style_table={'overflowY': 'scroll',
                                                'overflowX': 'scroll'})

    return table