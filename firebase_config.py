import firebase_admin
from firebase_admin import credentials, auth

cred = credentials.Certificate("D:/News_Aggregator/service_account_key.json")
firebase_admin.initialize_app(cred)
