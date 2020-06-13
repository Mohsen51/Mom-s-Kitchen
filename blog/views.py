
from django.shortcuts import render,redirect
from blog.models import Firebase_module,Pyrebase_module
import re,json 
import datetime
import requests

from advertisement.views import *


pb = Pyrebase_module();
fb = Firebase_module()

def sign_up(request):
	return render(request,"signUp.html")

def sign_in(request,redirection="welcome"):
	try:
		token = request.session['token']
		fb.verify_session_token(token)
		return render(request,"resultat.html")
	except:
		message=""
		return render(request,"signIn.html")
	
	

def password_reset(request):
	return render(request,"passwordReset.html")
	

def welcome(request):
	#try:
	token = request.session['token']
	fb.verify_session_token(token)
	return render(request,"resultat.html")
	#except:
	message ="issue with sessino, please log in "
	return render(request,"signIn.html",{"data":message})
	

	


def post_sign_up(request):
	try:
		name=request.POST.get('name')
		email=request.POST.get('email')
		password=request.POST.get('pass')
		#image=request.FILES['image']
	except :
		return render(request,"signUp.html",{"data":'image no load '})

	#### input verification ####

	#useless
	#if(len(password)<6 ):
	#	return render(request,"signUp.html",{"data":' Password must be a string at least 6 characters long '})
	#if (len(email)<0):
	#	return render(request,"signUp.html",{"data":'  Email must be a non-empty string '})
	
	
	#### init ####

	
	
	
	#### register #####	
	try:
		fb.create_user(email,password)
	except requests.exceptions.HTTPError as e:
		error_json = e.args[1]
		error = json.loads(error_json)['error']
		message = "Unknown error"
		if(error["errors"][0]["message"] == "EMAIL_EXISTS"):
			message = "Missing email"
		if(error["errors"][0]["message"] == "INVALID_EMAIL"):
			message= "Invalid email"
		return render(request,"signUp.html",{"data":message})
	
	# upload picture
	#path_picture = fb.upload_image_storage(image,'profileImages/')
	# add user's info 
	fb.upload_credentials_db(email,name)
	
	return render(request,"signIn.html")


def post_sign_in(request):
	email=request.POST.get('email')
	password = request.POST.get("pass")
	redirection = request.GET.get("redirection")
	

	#### credentials verification #####	
	try:
		token = pb.credentials_verification(email,password)
		message=""
		print(token)
		creation_cookie_session(request,token)	
	except requests.exceptions.HTTPError as e:
		error_json = e.args[1]
		error = json.loads(error_json)['error']
		message = "Unknown error"
		if(error["errors"][0]["message"] == "MISSING_EMAIL"):
			message = "Missing email"
		if(error["errors"][0]["message"] == "EMAIL_NOT_FOUND" or error["errors"][0]["message"] == "INVALID_PASSWORD" ):
			message = "invalids credentials"
		return render(request,"signIn.html",{"data":message})
		
	return redirect(display_data)

def post_password_reset(request):
	email=request.POST.get('email')
	##### send email ######

	try:
		pb.password_reset(email)
	except:
		pass

	message = "If the user exists, then you will receive an email containing instructions on how to reset the password"
	return render(request,"signIn.html",{"data":message})





def log_out(request):
	try:
		del request.session['token']
	except KeyError:
		return render(request,"signIn.html")

	return render(request,"signIn.html") #redirect to home page



def creation_cookie_session(request,token):
	request.session.set_expiry(1000)
	request.session['token']= str(token)




