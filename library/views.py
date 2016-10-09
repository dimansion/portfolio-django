from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from library.models import Category, Book
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.template import RequestContext
from django.utils import timezone
from django.views.generic import TemplateView
from .forms import BookForm

def index(request):
    category_list = Category.objects.order_by('name')
    posts_lists = Book.objects.order_by('-published_date')
    query = request.GET.get("q")
    if query:
        posts_lists = posts_lists.filter(Q(title__icontains=query)|Q(synopsis__icontains=query)).distinct()
    
    paginator = Paginator(posts_lists, 10) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)
    context_dict = {'categories': category_list, 'posts': posts }
    return render(request, 'library/post_list.html', context_dict)


def category(request, category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category_name'] = category.name
        posts = Book.objects.filter(category=category)
        context_dict['posts'] = posts
        context_dict['category'] = category
    except Category.DoesNotExist:
        pass
    return render(request, 'library/category.html', context_dict)

def post_detail(request, slug=None):
    post = Book.objects.get(slug=slug)
    return render(request, 'library/post_detail.html', {'post': post})


def post_create(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.save()
            return redirect('index')
    else:
        form = BookForm()

    context_dict = {
        'form': form
    }
    return render(request, 'library/post_create.html', context_dict)

def post_update(request, slug=None):
    #if not request.user.is_staff or not request.user.is_superuser:
    #    raise Http404
    instance = get_object_or_404(Post, slug=slug)
    form = BookForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect('library:post_detail', slug=slug)

    context_dict = {
        "title": instance.title,
        "instance": instance,
        "form":form,
    }
    return render(request, 'library/post_create.html', context_dict)

def post_delete(request, slug=None):
    instance = get_object_or_404(Post, slug=slug)
    instance.delete()
    return redirect("index")
