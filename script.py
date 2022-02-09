import requests
from coinbase.wallet.client import Client

import psycopg2
from datetime import date
from config import *


def getInvestments():
    # Indexa
    response = requests.get(
        "https://api.indexacapital.com/accounts/3V6ZEIPQ/portfolio",
        headers={"X-Auth-Token": Auth_indexa},
    )
    json = response.json()
    indexa = json["portfolio"]["total_amount"]
    # Coinbase
    api_key = Coinbase_API_key
    api_secret = Coinbase_API_secret
    client = Client(api_key, api_secret)
    user = client.update_current_user(name=User_name)
    total = 0
    message = []
    accounts = client.get_accounts()
    for wallet in accounts.data:
        message.append(str(wallet["name"]) + " " + str(wallet["native_balance"]))
        value = str(wallet["native_balance"]).replace("EUR", "")
        total += float(value)
    coinbase = round(total, 2)
    total = round(indexa + coinbase, 2)
    return total, coinbase, indexa


def trackInvestmentsSQL():
    conn = psycopg2.connect(
        dbname=PG_dbname, user=PG_user, password=PG_password, host=PG_host, port=PG_port
    )
    cur = conn.cursor()
    total, coinbase, indexa = getInvestments()
    today = date.today()
    cur.execute(
        'INSERT INTO investments ("Date", "Coinbase", "Indexa", "Total") VALUES (%s, %s, %s, %s)',
        (today, coinbase, indexa, total),
    )
    conn.commit()
    conn.close()
