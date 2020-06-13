
from django.shortcuts import render,redirect,HttpResponse
from blog.models import Firebase_module,Pyrebase_module
import re,json 
import datetime
import requests

from django.core import serializers
from django.http.response import JsonResponse




# Create your views here.



fb = Firebase_module()

######### page indexing ############

	
def food_form(request):
	try:
		token = request.session['token']
		info_vendor = fb.verify_session_token(token)
		return render(request,"food_form.html")
	except:
		message ="issue with session, please log in "
		return render(request,"signIn.html",{"data":message})

	
####################################

def display_data(request):
	try:
		token = request.session['token']
		info_vendor = fb.verify_session_token(token)
		return render(request,"Main.html")
	except:
		message ="issue with session, please log in "
		return render(request,"signIn.html",{"data":message})
	
def get_data(request):
	data = fb.get_a_product()
	
	data2 =  json.dumps(data)
	return HttpResponse(data2,content_type='application/json')




def post_food_form(request):
	try:
		token = request.session['token']
		info_vendor = fb.verify_session_token(token)
	except:
		message ="issue with session, please log in "
		return render(request,"signIn.html",{"data":message})


	try:
		foodDescription=request.POST.get('foodDescription')
		foodTitle=request.POST.get('foodTitle')
		foodCategory=request.POST.get('foodCategory')
		vegStatus=request.POST.get('vegStatus')
		vendor=request.POST.get('vendor')
		image=request.FILES['image']
		price=request.POST.get('price')
	except:
		return render(request,"food_form.html")

	

	#### upload data ######

	# upload picture
	fb.upload_image_storage(image,'ProductImages/')

	
	
	# add food's info 
	fb.upload_food(foodCategory,foodDescription,foodTitle,vegStatus,info_vendor['uid'],price)

	return redirect(display_data);



