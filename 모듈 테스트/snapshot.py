#-*- coding:utf-8 -*-

from picamera import PiCamera
import time
import requests
import sys, os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
import uuid
import schedule

PROJECT_ID = trash-d0f5c

cred = credentials.Certificate("../home/pi/Downloads/trash-d0f5c-firebase-adminsdk-vfc9v-59ece9fa8e.json")
default_app = firebase_admin.initialize_app(cred, { 'storageBucket': "gs://trash-d0f5c.appspot.com" })

bucket = storage.bucket()
filename = smr_20200712_144216

def fileUpload(file) :
	blob = bucket.blob('captureImages'+file)
	new_token = uuid4()
	metadata = {"firebaseStorageDownloadTokens": new_token}
	blob.metadata = metadata
	
	blob.upload_from_filename(filename='./captureImages'+file, content_type='image/jpeg')
	print(blob.public_url)


