#################### Libraries ####################
import dash_core_components as dcc
import dash_html_components as html

#################### Application Server File ####################
from app import app
from app import server

#################### Python Layouts ####################
from apps import project_overview, data_exploration, fraud_detection


#################### Layout ####################
app.layout = html.Div(children=[
    html.Div(id="banner",
             className="banner",
             children=[html.Div(id="banner-text",
                                children=[html.H5("SBA Paycheck Protection Program"),
                                          html.H6("Fraud Detection Using XGBoost Regression")]),
                        html.Div(id="banner-logo",
                                 children=[html.A(html.Button(children="Github Repo"),
                                                  href="https://github.com/carlosmonsivais123/PPP_Loan_Fraud_Detection")])]),

    html.Div(id="tabs",
             className="tabs",
             children=[dcc.Tabs(id="app-tabs",
                                value="tab1",
                                className="custom-tabs",
                                children=[dcc.Tab(id="Specs-tab",
                                                  label="Project Overview",
                                                  value="tab1",
                                                  children=[project_overview.layout],
                                                  className="custom-tab",
                                                  selected_className="custom-tab--selected"),
                                          dcc.Tab(id="Control-chart-tab",
                                                  label="Data Exploration",
                                                  value="tab2",
                                                  children=[data_exploration.layout],
                                                  className="custom-tab",
                                                  selected_className="custom-tab--selected"),
                                          dcc.Tab(id="Control-chart-tab",
                                                  label="Fraud Detection",
                                                  children=[fraud_detection.layout],
                                                  value="tab3",
                                                  className="custom-tab",
                                                  selected_className="custom-tab--selected")
                                                  ])])])

# Running the server
if __name__ == '__main__':
    app.run_server(debug=True, port=8050)
