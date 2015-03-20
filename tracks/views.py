from django.shortcuts import render
from .models import Track

def home(request):
	tracks = Track.objects.order_by('name')

	return render(request, 'indexfinal.html', locals())
