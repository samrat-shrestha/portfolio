from django.shortcuts import render
from .models import Job
# Create your views here.
def home(request):
	jobs = Job.objects # This gets all the database objects
	return render(request, 'jobs/home.html', {'jobs':jobs})
