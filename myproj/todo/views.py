from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from django import forms

class LoginForm(forms.Form):
    task=forms.CharField(max_length=100, label="New Task")

# Create your views here.
def view(request):
    if "todo" not in request.session:
        request.session["todo"]=[]
    return render(request, 'todo/index.html', {'todo':request.session["todo"]})

def add(request):
    if request.method=="POST":
        myLoginForm=LoginForm(request.POST)
        if myLoginForm.is_valid():
            task=myLoginForm.cleaned_data['task']
            request.session["todo"]+=[task]
            # return HttpResponseRedirect(reverse("todo:view"))
            return HttpResponseRedirect(reverse("todo:add"))
        else:
            return render(request, "todo/add.html", {"form": myLoginForm})
    else:
        return render(request, 'todo/add.html', {"form":LoginForm()})

def dlt(request, pk):
    task=request.session["todo"].object.get(id=pk)
    task.delete()
    return redirect("index")