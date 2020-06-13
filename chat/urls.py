# chat/urls.py
from django.conf.urls import url,re_path

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
   #  url('test', views.test, name='test'),
     re_path('^convCreation/$',views.create_conversation,name='create_conversation'),
  re_path('^convDisplayAll',views.display_all_conversation,name='display_all_conversation'),
  re_path('^convDisplayMessage',views.display_a_conversation,name='display_a_conversation'),
  re_path('^get_messages',views.get_messages,name='get_messages'),
  re_path('^get_conversations',views.get_conversations,name='get_conversations'),
]
