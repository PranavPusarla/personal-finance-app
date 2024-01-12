import plaid
from plaid.api import plaid_api
from plaid.model.transactions_get_request import TransactionsGetRequest
from datetime import datetime

from src.models.Transaction import Transaction

client_id = ""
client_secret = ""
access_token = ""

def create_client(client_id, client_secret):
    configuration = plaid.Configuration(
        host=plaid.Environment.Production,
        api_key={
            'clientId': client_id,
            'secret': client_secret,
        }
    )

    api_client = plaid.ApiClient(configuration)
    client = plaid_api.PlaidApi(api_client)
    return client

def get_transactions(client, access_token):
    request = TransactionsGetRequest(
        access_token=access_token,
        start_date=datetime.strptime('2023-12-01', '%Y-%m-%d').date(),
        end_date=datetime.strptime('2024-01-01', '%Y-%m-%d').date(),
    )
    response = client.transactions_get(request)
    return response

if __name__ == "__main__":

    client = create_client(client_id, client_secret)

    transactions_response = get_transactions(client, access_token)
    transactions_data = transactions_response['transactions']
    
    print(len(transactions_data))
    print(transactions_data[0])