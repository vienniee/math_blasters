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
db.collection('Students').add({'name':'John', 'age':'16'})