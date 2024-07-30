import pyrebase

config = {
  'apiKey': "AIzaSyADCjgV2PeZEpAjPUfWVV60OET-D1zXyQo",
  'authDomain': "newsaggregator-6b964.firebaseapp.com",
  'databaseURL': "https://newsaggregator-6b964-default-rtdb.firebaseio.com/",
  'projectId': "newsaggregator-6b964",
  'storageBucket': "newsaggregator-6b964.appspot.com",
   # 'messagingSenderId': "590901073777",
   # 'appId': "1:590901073777:web:8f2c995011de16ace6c8d0",
   # 'measurementId': "G-FSBZ4ZEJC0",
    "serviceAccount":"D:/News_Aggregator/service_account_key.json"

}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

