from django.shortcuts import render, render_to_response
from django import forms
from django.http import HttpResponse
from disk.models import User
import random
# Create your views here.

class UserForm(forms.Form):
    username = forms.CharField()
    headimg = forms.ImageField()

def register(request):
    if request.method == "POST":
        uf = UserForm(request.POST, request.FILES)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            headimg = uf.cleaned_data['headimg']

            user = User()
            user.username = username
            user.headimg = headimg
            user.save()

            return HttpResponse('upload ok!')
    else:
        uf = UserForm()
    return render_to_response('register.html', {'uf': uf})

def result(request):
    lucky_member = random.choice(User.objects.all())
    return HttpResponse(
        "<p>{0.username} {0.headimg}<p>".format(lucky_member)
    )