from django.shortcuts import render
import os
from .python_file.image_recognition import pmi_database,file_parse
from django.http import JsonResponse

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from .forms import UploadFileForm


def index(request):
    return render(request, 'ai_web/ai_web.html')

def image_recognition(request):
    return render(request, 'image_recognition/index.html')

def upload_file(request):
    if request.method == 'POST':
        print("upload")
        obj = request.FILES.get('upload')
        baseDir = os.path.dirname(os.path.abspath(__file__))
        orderDir = os.path.join(baseDir, 'cache/file_uploaded/')
        filename = os.path.join(orderDir, obj.name)
        fobj = open(filename, 'wb')
        for chrunk in obj.chunks():
            fobj.write(chrunk)
        fobj.close()
        pmi_database.delete()
        pmi_parse = file_parse.PmiParse(filename)
        pmi_log = pmi_parse.getdata
        print(pmi_log)
        pmi_database.insert(pmi_log)
    return render(request, 'image_recognition/index.html')

def display_pmi_log(request):
    data = []
    if request.method == 'GET':
        data = pmi_database.find()
    #return JsonResponse(data,safe=False)
    return HttpResponse(data)