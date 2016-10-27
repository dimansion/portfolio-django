from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('portfolio.urls', namespace='portfolio')),
    url(r'^blog/', include("blog.urls", namespace='blog')),
    url(r'^todo/', include('todo.urls', namespace='todo')),
    url(r'^gallery/', include('gallery.urls', namespace='gallery')),
    url(r'^polls/', include('polls.urls', namespace='polls')),
    url(r'^library/', include('library.urls', namespace='library')),
    url(r'^logout/$', auth_view.logout, name='logout', kwargs={'next_page': '/'}),
    url(r'^s/', include('shortener.urls', namespace='shortener')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)