from django.http import HttpResponse
import os

def handle_uploaded_file(file_name):
    current_path = os.path.abspath(__file__)
    with open(current_path + 'cache/file_uploaded/'+ file_name, 'wb+') as destination:
        destination.write(chrunk)
    destination.close()