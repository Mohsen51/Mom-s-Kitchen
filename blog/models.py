from django.db import models

# Create your models here.
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import storage
from firebase_admin import auth
import pyrebase
import datetime
import uuid
import json
import requests
from pprint import pprint
from google.cloud.firestore_v1beta1 import ArrayUnion


class Firebase_module(models.Model):

	# Class Attribute
	cred = credentials.Certificate("homefood-b7713-firebase-adminsdk-u8apq-e2983e57b5.json")

	# Initializer / Instance Attributes
	def __init__(self):
		try:
			self.app = firebase_admin.initialize_app(Firebase_module.cred)
		except:
			pass
		self.db = firestore.client()
		self.bucket = storage.bucket('homefood-b7713.appspot.com')
		
      
	
	# instance method
	def delete_instance(self):
		firebase_admin.delete_app(app)

	def create_user(self,email,password):
		Firebase_module.user = auth.create_user( email=email,password=password)

	

	def generate_random_uuid():
		return str(uuid.uuid4())
		

	####### storage database #######
	def upload_image_storage(self,image,folder):
		if(folder == 'profileImages/'):
			path = Firebase_module.user.uid
		else:
			path = Firebase_module.generate_random_uuid()

		blob = self.bucket.blob(folder+path+'.png')
		blob.upload_from_file(image)
		blob.make_public()
		Firebase_module.path_picture = blob.public_url

	def upload_credentials_db(self,email,name):
		doc_ref = self.db.collection(u'UsersDetails').document(Firebase_module.user.uid)
		doc_ref.set({
   			u'UserEmail': email,
 	   		u'uid': Firebase_module.user.uid,
	   		u'Username': name,
	   		u'VerificationStatus' : 0,
	   		#u'profileImage' : 'https://firebasestorage.googleapis.com/v0'+Firebase_module.path_picture,
		})

	def upload_food(self,category,description,title,vegStatus,vendor,price):
		doc_ref = self.db.collection(u'Listings').document(Firebase_module.generate_random_uuid())
		doc_ref.set({
   			u'FoodCategory': category,
 	   		u'FoodDescription': description,
	   		u'FoodTitle': title,
	   		u'ProductImageUrl' :Firebase_module.path_picture,
	   		u'VegSatus' : vegStatus,
	   		u'Vendor' : vendor ,
	   		u'Price' : price,
	   		u'MessageChannel': [],
		})

	def get_uid_vendor(self,uuid_product):
		data = self.db.collection(u'Listings').document(uuid_product).get()
		return data.to_dict()['Vendor']

	def create_channel_conversation_for_user(self,uid,uid_contact,uuid):
		doc_ref_vendor = self.db.collection(u'UsersDetails').document(uid)
		doc_ref_vendor.update({u'MessageChannel': ArrayUnion([{uid_contact:uuid}])})

		
	def init_conversation(self,subject,uuid):
		#set the conversation field in messages
		doc_ref = self.db.collection(u'Messages').document(uuid)
		doc_ref.set({
			u'subjet': subject,
			u'Messages' : [],
			
		})

	def get_a_product(self):
		doc_ref = self.db.collection(u'Listings')
		data = doc_ref.get()
		array =[]
		for doc in data:
			tmp = {"id": doc.id,"data":doc.to_dict()}
			array.append(tmp)
		return  array

	def get_name_from_uid(self,uid):
		doc_ref = self.db.collection(u'UsersDetails').document(uid)
		data = doc_ref.get()
		return  data.to_dict()['Username']
		
	def get_all_conversation(self,uid):
		doc_ref = self.db.collection(u'UsersDetails').document(uid)
		data = doc_ref.get()
		array = []


		doc_ref_article = self.db.collection(u'Listings').document

		try:
			for  y in data.to_dict()['MessageChannel']:
				index =list(y)
				tmp = {"Username": self.get_name_from_uid(index[0]),"uuid_conv":y[index[0]]}
				array.append(tmp)
		except:
			pass

		return array

	def get_a_conversation(self,uuid):
		doc_ref = self.db.collection(u'Messages').document(uuid)
		data = doc_ref.get()

		array = []
		try:

			for  y in data.to_dict()['Messages']:
				print(y)
				index= list(y)
				tmp = {"Username": self.get_name_from_uid(index[0]),"message":y[index[0]]}
				array.append(tmp)

			print(array)

		except:
			pass
		return array

	def add_message_to_conversation(self,message,uuid_conv,uid):
		doc_ref = self.db.collection(u'Messages').document(uuid_conv)
		doc_ref.update({u'Messages': ArrayUnion([{uid:message}])})

	def delete_a_conversation(self,uuid):
		doc_ref = self.db.collection(u'Messages').document(uuid_conv).delete()


	def verify_session_token(self,id_token):

		 return auth.verify_id_token(id_token)

	def verify_if_conversation_exist(self,uid,uid_vendor):
		doc_ref = self.db.collection(u'UsersDetails').document(uid)
		data = doc_ref.get()

		try:
			for  y in data.to_dict()['MessageChannel']:
				index =list(y)
				if(index[0]==uid_vendor):
					print("match")
					return y[index[0]]
		except:
			pass
			

		return "0"

	







	
	

class Pyrebase_module(models.Model):


	# Class Attribute
	config = {
		'apiKey': "AIzaSyC0TACrDN13PHAGiKz29_7OnjjYvcR9-7Y",
    	'authDomain': "homefood-b7713.firebaseapp.com",
    	'databaseURL': "https://homefood-b7713.firebaseio.com",
    	'projectId': "homefood-b7713",
    	'storageBucket': "homefood-b7713.appspot.com",
    	'messagingSenderId': "1004772233083"

	}

	# Initializer / Instance Attributes
	def __init__(self):
		self.firebase = pyrebase.initialize_app(Pyrebase_module.config)
		self.auth = self.firebase.auth()

	# instance method
	def password_reset(self,email):
		self.auth.send_password_reset_email(email)

	def credentials_verification(self,email,password):
		user =  self.auth.sign_in_with_email_and_password(email,password)

		return user['idToken']

	
      




