from myWebApp.ImgUpload.form import ImageUploadForm
from django import forms
from django.shortcuts import render
from .form import ImageUploadForm

def home(request):
    return render(request,'home.html')

def imageprocess(request):
    form=ImageUploadForm(request.POST, request.FILES )
    if form.is_valid():
        handel_uploaded_file(request.FILES['image'])
        return render(request,'result.html')

def handel_uploaded_file(f):
    with open('img.jpg','wb+')as destination:
        for chunk in f.chunks():
            destination.write(chunk)

# Create your views here.
