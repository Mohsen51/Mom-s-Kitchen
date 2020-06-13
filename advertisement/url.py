from django.urls import path
from django.conf.urls import url,re_path
from . import views


urlpatterns = [
	re_path('^foodForm',views.food_form,name='food_form'),
	re_path('^postFoodForm',views.post_food_form,name='post_food_form'),
   re_path('^get_data',views.get_data,name='get_data'),
   re_path('^display_data',views.display_data,name='display_data'),
   ]

  