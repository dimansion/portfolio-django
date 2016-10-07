from django.shortcuts import render
from .models import Picture

def photo_list(request):
    pictures = Picture.objects.all()
    context = {'pictures': pictures}
    return render(request, 'gallery/photo_list.html', context)
