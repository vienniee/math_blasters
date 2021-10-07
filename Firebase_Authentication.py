import pyrebase

firebaseConfig = {
  'apiKey': "AIzaSyBEOlShI29lUu4NhonKtqFH-NSt85ZvGVI",
  'authDomain': "math-blasters.firebaseapp.com",
  'projectId': "math-blasters",
  'storageBucket': "math-blasters.appspot.com",
  'messagingSenderId': "1022427765658",
  'appId': "1:1022427765658:web:f5319e28731afca5783823",
  'measurementId': "G-L2L2H64FDN",
  "databaseURL": ""
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

def signup():
    email = input("Enter email: ")
    password = input("Enter password: ")
    try:
      user = auth.create_user_with_email_and_password(email, password)
      print("Successfully created")
    except:
      print("Email already exist")

signup()
