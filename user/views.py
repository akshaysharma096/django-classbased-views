from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotAllowed,JsonResponse
from django.views.generic import View
from django.conf import settings
import uuid
from django.utils.cache import patch_cache_control,get_max_age,patch_response_headers
# Create your views here.

class MyView(View):
	#each class must be a subclass of View class

	#specifies the http methods allowed in this view
	http_method_names=['post','get']
	message='Hello niggaz'

	def get(self,request,*args,**kwargs):

		# response=HttpResponse('<div id="myview">This is a class based view response.</div>',content_type='text/html',charset='utf-8')
		response=HttpResponse(self.message)
		response.__setitem__('x-uid',uuid.uuid4().hex)		#set header explicitly
		response.__setitem__('status',200)
		# response.set_signed_cookie('__ga_id__','112(8*(89&!891292',salt=settings.COOKIE_SALT,httponly=True)
		patch_response_headers(response)
		return response

	#Override this method to tell what to do when one of the methods in http_method_names is called
	def http_method_not_allowed(request, *args, **kwargs):
		return HttpResponse("Method not allowed",status=405)
		#return any type of response here
		# return JsonResponse(status=405,data={'not_allowed':True})
