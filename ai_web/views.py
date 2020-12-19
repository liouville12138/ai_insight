from django.shortcuts import render
import os

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from .forms import UploadFileForm
from .upload_file import handle_uploaded_file


def index(request):
    return render(request, 'ai_web/ai_web.html')

def image_recognition(request):
    return render(request, 'image_recognition/index.html')

def upload_file(request):
    print(request.method)
    if request.method == 'POST':
        obj = request.FILES.get('upload')
        baseDir = os.path.dirname(os.path.abspath(__file__))
        orderDir = os.path.join(baseDir, 'cache/file_uploaded/')
        filename = os.path.join(orderDir, obj.name)
        fobj = open(filename, 'wb')
        for chrunk in obj.chunks():
            fobj.write(chrunk)
        fobj.close()
    return render(request, 'image_recognition/index.html')