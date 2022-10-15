from numpy.lib.function_base import append
from myWebApp.ImgUpload.form import ImageUploadForm
from django import forms
from django.shortcuts import render
from .form import ImageUploadForm

from keras.applications.resnet import ResNet50 
from keras.preprocessing import image
from keras.applications.resnet import preprocess_input, decode_predictions
import numpy as np

def home(request):
    return render(request,'home.html')

def imageprocess(request):
    form=ImageUploadForm(request.POST, request.FILES )
    if form.is_valid():
        handle_uploaded_file(request.FILES['image'])
        model= ResNet50(weights='imagenet')
        img_path = 'img.jpg'
        imge=image.load_img(img_path, target_size=(224,224))
        x=image.img_to_array(imge)
        x=np.expand_dims(x,axis=0)
        x=preprocess_input(x)
        preds=model.predict(x)
        print('Pridicted',decode_predictions(preds,top=3)[0])

        html=decode_predictions(preds,top=3,)[0]

        res=[]
        for e in html:
            res.append((e[1],np.round(e[2]*100,2)))
        return render(request,'result.html' , {'res':res})





    

def handle_uploaded_file(f):
    with open('img.jpg','wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

# Create your views here.
