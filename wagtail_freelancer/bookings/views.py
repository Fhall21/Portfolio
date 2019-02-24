import ast, re, json

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, filters, viewsets

from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404

from bookings.models import Meeting
from bookings.serializer import MeetingSerializer

class MeetingViewSet(viewsets.ModelViewSet):
	queryset = Meeting.objects.all()
	serializer_class = MeetingSerializer

#	def perform_update(self, serializer):
#		print (serializer.context['request'].data)
#		serializer.save()

	# def patch(self, request, pk):
	# 	print ('from pk: '+ str(pk))
	# 	print ('from request: ' + str(request.data.id)) 
	# 	model_object = Meeting.objects.get(id=request.data.id)
	# 	serializer = MeetingSerializer(model_object, data=request.data, partial=True) # set partial=True to update a data partially
	# 	if serializer.is_valid(raise_exception=True):
	# 		serializer.save(id=pk, **serializer.validated_data)
	# 		return JsonReponse(code=201, data=serializer.data)
	# 	return JsonResponse(code=400, data="wrong parameters")
	def partial_update(self, request, *args, **kwargs):
		#print (request.data)
		kwargs['partial'] = True
		QuerySet = list(request.data)[0]
		query_data = ast.literal_eval(QuerySet)
		#json_data = json.loads(request.data)
		#print ('json: ' + type(json_data))
		del query_data["id"]
		del query_data['csrfmiddlewaretoken']

		model_object = Meeting.objects.get(id=kwargs['pk'])
		serializer = MeetingSerializer(model_object, data=query_data, partial=True)
		#print (serializer)
		if serializer.is_valid(raise_exception=True):
			serializer.save(id=kwargs['pk'], **serializer.validated_data)

		return self.update(request, *args, **kwargs)
#https://stackoverflow.com/questions/31880227/django-rest-framework-method-put-not-allowed-in-viewset-with-def-update
'''
as.literal_eval(l)
{
'{"id":["8"],
"name":"Felix Hall",
"email":"felix.p.hall@gmail.com",
"phone_number":"0481322948",
"csrfmiddlewaretoken":"nR2UuR8KCjAtyMGeIOwTI6zQiYy0fjjdYft8v6fdsExik4A5jOB0BlyfTKdzjsKM"}': ['']
}

'''