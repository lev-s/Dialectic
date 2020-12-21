from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import dialecticapp
from .forms import DialecticAppForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from django.views import generic
from rest_framework import viewsets
from .serializers import dialecticappSerializer


class dialecticappViewSets(viewsets.ModelViewSet):
    queryset = dialecticapp.objects.all();
    serializer_class = dialecticappSerializer


def dialectic_home(request):

    
    context={
        "title": "Dialectic - Homepage",
    }


    return render(request, "index.html", context)


def dialectic_signIn(request):
    context={
        "title": "Dialectic - Sign in page"
    }
    return render(request, "login.html", context)

def dialectic_signUp(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect('login')
            else:
                return redirect('join')
            
    context={
        "form": form,
    }
    return render(request, "registration/join.html", context)

def dialectic_schedule(request):
    table = dialecticapp.objects.all()

    form = DialecticAppForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('/table')


    context={
        "objectList": table,
        "form": form,
    }
    return render(request, "table.html", context)

def dialectic_update(request, pk):
    table = dialecticapp.objects.get(id=pk)

    form = DialecticAppForm(instance=table)
    context = {
        'form': form,
        'title': "Dialectic - Update Page"
    }

    if request.method == "POST":
        form = DialecticAppForm(request.POST, instance=table)
        if form.is_valid():
            form.save()
            return redirect('/table')


    return render(request, "update.html", context)



