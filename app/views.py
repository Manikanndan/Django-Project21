from django.http.response import HttpResponse
from app.forms import ImageFile
from django.shortcuts import render
from app.forms import *
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
# Create your views here.

def fun_imageData(request):
    image=ImageFile()
    if request.method=='POST' and request.FILES:
        image_data=ImageFile(request.POST,request.FILES)
        if image_data.is_valid():
            img=image_data.cleaned_data['image']
            fs=FileSystemStorage()
            file=fs.save(img.name,img)
            image_url=fs.url(file)
        return render(request,'imagedisplay.html',context={'image_url':image_url})

    return render(request,'imagefile.html',context={'image':image})