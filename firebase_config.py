import pyrebase

config = {
  'apiKey': "",
  'authDomain': "",
  'databaseURL': "",
  'projectId': "",
  'storageBucket': "",
   # 'messagingSenderId': "590901073777",
   # 'appId': "1:590901073777:web:8f2c995011de16ace6c8d0",
   # 'measurementId': "G-FSBZ4ZEJC0",
    "serviceAccount":""

}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

