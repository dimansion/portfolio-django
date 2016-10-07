from django.shortcuts import render
from .models import Project
from blog.views import post_list

def home_view(request):
	project = Project.objects.all()
	context = {
		'projects': project,
	}
	return render(request, 'portfolio/projects.html', context)
