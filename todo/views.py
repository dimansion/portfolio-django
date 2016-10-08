from django.shortcuts import render, get_object_or_404
from .models import Jadwal
from .forms import JadwalForm
from django.shortcuts import redirect
# Create your views here.

def list_jadwal(request):
	posts = Jadwal.objects.all()
	if request.method == "POST":
		form = JadwalForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.waktu.strftime("%d/%m/%y %H:%M") 
			post.save()
		return redirect('todo:list_jadwal')
	else:
		form = JadwalForm()
	context_dict = {
		'jadwal': posts,
		'form': form
	}
	return render(request, 'todo/schedule_list.html', context_dict)

def hapus_jadwal(request, pk):
    post = get_object_or_404(Jadwal, pk=pk)
    post.delete()
    return redirect('todo:list_jadwal')
	