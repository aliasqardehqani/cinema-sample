from django.shortcuts import render, redirect, get_object_or_404
from .models import Foods, Comment
from .forms import CommentForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.http import HttpResponse
# Create your views here.

#  ---------------------------------------------------



def food_list(request):

    food_list = Foods.objects.all()
    context = {
        'foods': food_list
    }
    return render(request, 'index.html', context)

#  ---------------------------------------------------



def food_detail(request, id):
    food = Foods.objects.get(id=id)

    context = {
        'food': food
    }
    return render(request, 'detail.html', context)

#  ---------------------------------------------------



def add_comment(request, pk):
    food = get_object_or_404(Foods, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=True)
            comment.food = food
            comment.save()
            return redirect('foods:detail', pk=food.pk)
    else:

        form = CommentForm()
        return render(request, 'comment.html', {'form': form})

#  ---------------------------------------------------



def discount(request):
    food = Foods.objects.all()
    context = {
        'food': food
    }
    return render(request, 'discount.html', context)

#  ---------------------------------------------------



def contact(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/foods/')

    form = AuthenticationForm()
    return render(request, 'contact.html', {'form': form})

#  ---------------------------------------------------


