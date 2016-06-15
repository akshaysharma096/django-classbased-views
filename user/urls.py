from django.conf.urls import include, url
from .views import MyView,GetUserView,GetParticularUserView
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import *
from django.conf.urls import (
handler400, handler403, handler404, handler500
)

urlpatterns=[
	url(r'^base/$',MyView.as_view(),name='MyView'),			#overriding class attribute 
	url(r'^all/$',GetUserView.as_view(),name='users'),
	url(r'^(?P<id>[0-9]+)/$',GetParticularUserView.as_view(),name='user'),
]