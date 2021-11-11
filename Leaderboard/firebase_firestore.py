import pyrebase
import pygame
import pygame.freetype
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("serviceaccountkey.json")
firebase_admin.initialize_app(cred)

#Initialising the database
db=firestore.client()

#Test data insertion, to be deleted later
#For Vivien:
#use this to populate database
#use a loop to add records into the database and partition them by levels and question types
#db.collection('Students').add({'Name':'John', 'Score':100})
#db.collection('Students').add({'Name':'Adam', 'Score':80})
#db.collection('Students').add({'Name':'Kenny', 'Score':70})
#db.collection('Students').add({'Name':'Richard', 'Score':60})
#db.collection('Students').add({'Name':'Damien', 'Score':50})
#db.collection('Students').add({'Name':'Ben', 'Score':20})
#db.collection('Students').add({'Name':'Xavier', 'Score':10})

def getRanking():
    #pull data of the top 5 students
    scoreref = db.collection('Students')
    query = scoreref.order_by('Score',direction=firestore.Query.DESCENDING).limit(5)
    return query.get()