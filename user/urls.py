from django.conf.urls import include, url
from .views import MyView,GetUserView,GetParticularUserView,TView,ContactView,AuthorCreate,AuthorUpdate,AuthorDelete
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import *
from django.conf.urls import (
handler400, handler403, handler404, handler500
)

urlpatterns=[
	url(r'^base/$',MyView.as_view(),name='MyView'),			#overriding class attribute 
	url(r'^all/$',GetUserView.as_view(),name='users'),
	url(r'^(?P<id>[0-9]+)/$',GetParticularUserView.as_view(),name='user'),
	url(r'^t/(?P<id>[0-9]+)/$',TView.as_view(),name='T'),
	url(r'^contact/$',ContactView.as_view(),name='contact'),
	url(r'author/add/$', AuthorCreate.as_view(), name='author-add'),
    url(r'author/(?P<slug>[0-9A-Za-z_\-]+)/$', AuthorUpdate.as_view(), name='author-update'),
    url(r'author/(?P<pk>[0-9]+)/delete/$', AuthorDelete.as_view(), name='author-delete'),
]