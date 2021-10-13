import pyrebase

firebaseConfig = {
    'apiKey': "AIzaSyBEOlShI29lUu4NhonKtqFH-NSt85ZvGVI",
    'authDomain': "math-blasters.firebaseapp.com",
    'projectId': "math-blasters",
    'storageBucket': "math-blasters.appspot.com",
    'messagingSenderId': "1022427765658",
    'appId': "1:1022427765658:web:f5319e28731afca5783823",
    'measurementId': "G-L2L2H64FDN",
    "databaseURL": "https://math-blasters-default-rtdb.asia-southeast1.firebasedatabase.app/"
}

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()
auth = firebase.auth()
