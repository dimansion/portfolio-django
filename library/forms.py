from django import forms
from .models import Book
from pagedown.widgets import PagedownWidget

class BookForm(forms.ModelForm):
    
    published_date = forms.DateField(widget=forms.SelectDateWidget)
    class Meta:
        model = Book
        fields = [
            'image',
            'author',
            'title',
            'synopsis',
            'published_date',
            'category',
            
        ]