from django.forms import ModelForm
from django import forms
from .models import Comment, Foods, Sales

class FoodForm(forms.ModelForm):

    class Meta:
        model = Foods
        fields = '__all__'

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('post', 'author', 'text')

class SaleForm(forms.ModelForm):

    class Meta:
        model = Sales
        fields = '__all__'

