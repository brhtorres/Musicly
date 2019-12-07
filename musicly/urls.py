from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^$', views.music_list),
	url(r'^bySinger', views.musics_bySinger),
]