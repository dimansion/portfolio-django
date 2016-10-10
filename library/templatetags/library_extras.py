from django import template
from library.models import Category

register = template.Library()

@register.inclusion_tag('library/cats.html')
def get_category_list(cat=None):
    return {'cats': Category.objects.all().order_by('name'), 'act_cat': cat}

