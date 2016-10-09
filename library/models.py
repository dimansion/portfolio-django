from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.conf import settings
from django.core.urlresolvers import reverse

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Book(models.Model):
    image = models.ImageField(null=True, blank=True)
    author = models.CharField(max_length=128, unique=True)
    title = models.CharField(max_length=200)
    synopsis = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    category = models.ForeignKey(Category,blank=True,null=True)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
                # Uncomment if you don't want the slug to change every time the name changes
                #if self.id is None:
                        #self.slug = slugify(self.name)
            self.slug = slugify(self.title)
            super(Book, self).save(*args, **kwargs)    
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug})        

    def __str__(self):
        return self.title
