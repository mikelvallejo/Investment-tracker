# InvestmentApp

Simple ETL to track investments. Runs script every day and updates the database. Results are shown in a dashboard made with streamlit frontend.

* Script.py: Contains the 2 main functions. getInvestments() tracks the amount invested in each account. TrackInvestmentsSQL() stores it in a PostgreSQL database (in my case is hosted in Heroku)
* Streamlit.py: Frontend made with the Python framework Streamlit 

# Flow
![Image](https://github.com/mikelvallejo/InvestmentApp/blob/main/flow.png)

# Interface
![Image](https://github.com/mikelvallejo/InvestmentApp/blob/main/image.jpeg)
