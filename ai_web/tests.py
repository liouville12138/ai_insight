from django.test import TestCase
import os
# Create your tests here.
from python_file.image_recognition import file_parse


current_path = os.path.dirname(os.path.abspath(__file__))

fileIn = current_path + "/cache/file_uploaded/pmi_log.xlsx"
pmi_parse = file_parse.PmiParse(fileIn)
pmi_log = pmi_parse.getdata
pass
