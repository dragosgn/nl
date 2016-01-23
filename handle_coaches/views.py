from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Coach

from contact_app.forms import ContactForm

#import contact form here!!!!!

#Api imports
from .serializers import CoachSerializer
from rest_framework import generics
from rest_framework import permissions
from rest_framework.decorators import api_view
from .permissions import IsOwnerOrReadOnly
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework.decorators import detail_route




def index(request):
    latest_coaches_list = Coach.objects.order_by('-date_joined')[:4]
    context = {'latest_coaches_list': latest_coaches_list}
    return render(request, 'index.html', context)

def coachesList(request):
	return render(request, 'coaches_list_page.html', [])

def coachProfile(request, coach_id):
	#return HttpResponse("You are looking at Coach: %s." % coach_id)
	coach = get_object_or_404(Coach, pk=coach_id)
	return render(request, 'coach_profile.html', {'coach': coach})
# Api Views

class CoachViewSet(viewsets.ModelViewSet):
	queryset = Coach.objects.all()
	serializer_class = CoachSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

