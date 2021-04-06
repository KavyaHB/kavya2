from django.http import HttpResponse
import os
file_path=os.path.abspath(__file__)
dir_path=os.path.dirname(file_path)

def home(request):
    file_addr=os.path.join(dir_path,"sample.html")
    fp=open(file_addr,"r")
   # fp=open(r'C:\Users\DELL\Desktop\kavya1_django\project1\pro3\sample.html',"r")
    data=fp.read()
    return HttpResponse(data)
