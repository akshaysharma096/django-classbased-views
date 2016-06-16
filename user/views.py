from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotAllowed,JsonResponse
from django.views.generic import View
from django.conf import settings
from django.views.generic.base import TemplateView
import uuid
from .models import User,Author
from django.utils.cache import patch_cache_control,get_max_age,patch_response_headers,get_cache_key,patch_vary_headers
from django.views.decorators.http import condition,etag,last_modified
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.gzip import gzip_page
from django.views.decorators.vary import vary_on_headers
from django.core.cache import cache
from django.template.response import TemplateResponse
from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from .forms import ContactForm,ContactForm2
from django.views.generic.edit import CreateView, UpdateView, DeleteView,FormView
from django.core.urlresolvers import reverse_lazy
# Create your views here.


class AuthorCreate(CreateView):
    model = Author
    fields = ['name']

class AuthorUpdate(UpdateView):
    model = Author
    fields = ['name']

class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('author-list')


class ContactView(FormView):
	'''
		Inherit this View to create and validate  a form automatically.
	'''
	template_name='form.html'
	form_class=ContactForm
	form_class_2=ContactForm2
	# success_url='/thanks/'

	#function to check the validity of form
	#override the function to add own functionality
	def form_valid(self,form):
		form.send_email()
		#calling a method in the form
		form.save()
		return JsonResponse(status=200,data={'success':True})

	# function that is called when the form is invlaid.
	def form_invalid(self,form):
		return JsonResponse(status=400,data=form.errors)

	def get_context_data(self,**kwargs):
		#set context to pass to html
		context=super(ContactView,self).get_context_data(**kwargs)
		context['form_1']=self.form_class()
		context['form_2']=self.form_class_2()
		return context

class MyView(View):
	#each class must be a subclass of View class

	#specifies the http methods allowed in this view
	http_method_names=['post','get']
	message='<div id="myview">This is a class based view response.</div>'
	content_type='text/html'
	charset='utf-8'
	# template_name='base.html'

	@method_decorator(gzip_page)
	@method_decorator(condition(etag_func=None,last_modified_func=None))
	def get(self,request,*args,**kwargs):
		response=TemplateResponse(request,self.template_name,{'number':1,'number_2':2})
		response.__setitem__('x-uuid',uuid.uuid4().hex)		#set header explicitly
		response.__setitem__('status',200)
		response.__setitem__('page_id',str(uuid.uuid4().hex))
		patch_vary_headers(response,['Etag','Cookie','User-Agent'])
		patch_cache_control(response)
		return response

	#Override this method to tell what to do when one of the methods in http_method_names is called
	def http_method_not_allowed(request, *args, **kwargs):
		response=HttpResponse("Method not allowed",status=405)
		response.__setitem__('x-uid',uuid.uuid4().hex)		#set header explicitly
		response.__setitem__('status',405)
		response.__setitem__({'hello':'word'})
		return response
		#return any type of response here
		# return JsonResponse(status=405,data={'not_allowed':True})

class GetUserView(ListView):
	http_method_names=['get','head']
	queryset=User.objects.all()				#specify which model to populate
	template_name='base.html'	#specify the template
	context_object_name='users'	#context to be passed


	def get_context_data(self,**kwargs):
		context=super(GetUserView,self).get_context_data(**kwargs)
		context['number']=1
		return context

class GetParticularUserView(ListView):
	http_method_names=['get']
	template_name='one_user.html'
	# context_object_name='user'		# set context either by this or by get_context_data
	'''queryset=User.objects.all()'''	# one way to set the data in the context
	
	def get_queryset(self):
		# define the query set to be used here.
		self.user=get_object_or_404(User,id=self.kwargs['id']) 
		return self.user

	def get_context_data(self,**kwargs):
		context=super(GetParticularUserView,self).get_context_data(**kwargs)
		context['user']=self.user
		return context


class TView(TemplateView):
	'''
		Methods, below are not available here.
		Cannot set context using get_queryset or get_context_data
		set context using TemplateResponse()
	'''

	http_method_names=['get']
	template_name='template_view.html'

	def get(self,request,*args,**kwargs):
		return TemplateResponse(request,self.template_name,{'user':User.objects.get(id=1)})

	# def get_queryset(self):
	# 	# define the query set to be used here.
	# 	self.user=get_object_or_404(User,id=self.kwargs['id']) 
	# 	return self.user

	# def get_context_data(self,**kwargs):
	# 	context=super(GetParticularUserView,self).get_context_data(**kwargs)
	# 	context['user']=self.user
	# 	return context