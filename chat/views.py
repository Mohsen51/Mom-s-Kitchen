# chat/views.py
from django.shortcuts import render,HttpResponse
from django.utils.safestring import mark_safe
import json

from blog.models import Firebase_module,Pyrebase_module

def index(request):
    return render(request, 'chat/index.html', {})


fb = Firebase_module()



def create_conversation(request):
	# verify cookie session 
	try:
		token = request.session['token']
		uid = fb.verify_session_token(token)['uid']
	except:
		message ="issue with session, please log in "
		return render(request,"signIn.html",{"data":message})

	
	uuid_products = request.GET['uuid']
	
	#get 
	uid_vendor = fb.get_uid_vendor(uuid_products)

	check_conv = fb.verify_if_conversation_exist(uid,uid_vendor)

	if(check_conv == "0"):
		print("gell")
		uuid_conv= Firebase_module.generate_random_uuid()
		fb.create_channel_conversation_for_user(uid,uid_vendor,uuid_conv);
		fb.create_channel_conversation_for_user(uid_vendor,uid,uuid_conv);
		fb.init_conversation("subject",uuid_conv)
	else:
		print("pas ")
		uuid_conv = check_conv

	content = {
		'uuid_conv':uuid_conv,
		'from': uid,
		'user_name': fb.get_name_from_uid(uid),
	}

	#redirect
	
	return render(request,"chat/room.html",{"content":mark_safe(json.dumps(content))})




def display_all_conversation(request):
	# verify cookie session 
	try:
		token = request.session['token']
		uid = fb.verify_session_token(token)['uid']
	except:
		message ="issue with session, please log in "
		return render(request,"signIn.html",{"data":message})

	return render(request,"chat/contact.html")


def get_conversations(request):
	# verify cookie session 
	try:
		token = request.session['token']
		uid = fb.verify_session_token(token)['uid']
	except:
		message ="issue with session, please log in "
		return render(request,"signIn.html",{"data":message})

	
	data = fb.get_all_conversation(uid)

	data2 =  json.dumps(data)	
	
	return HttpResponse(data2,content_type='application/json')



def display_a_conversation(request):
	# verify cookie session 
	try:
		token = request.session['token']
		uid = fb.verify_session_token(token)['uid']
	except:
		message ="issue with session, please log in "
		return render(request,"signIn.html",{"data":message})

	uuid_conv = request.GET.get('uuid')

	content = {
		'uuid_conv':uuid_conv,
		'from': uid,
		'user_name': fb.get_name_from_uid(uid),
	}

	return render(request,"chat/room.html",{"content":mark_safe(json.dumps(content))})

def get_messages(request,uuid_conv):
	# verify cookie session 

	#uuid_conv="f11afdea-67f8-4c2c-a998-d08c74639f20"

	data = fb.get_a_conversation(uuid_conv)
	#to_test
	data2 =  json.dumps(data)	
	
	return data2


def delete_a_conversation(request):
	# verify cookie session 
	try:
		token = request.session['token']
		uid = fb.verify_session_token(token)['uid']
	except:
		message ="issue with session, please log in "
		return render(request,"signIn.html",{"data":message})

	#uuid_conv=request.POST.get('uuid_conv')
	uuid_conv="f11afdea-67f8-4c2c-a998-d08c74639f20"

	fb.delete_a_conversation(uuid_conv)

	#to_test
	return render(request,"chat/list_conversation_display.html")






	