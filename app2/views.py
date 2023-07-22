from django.shortcuts import render
# from .models import chat,group
# Create your views here.
def index(request,group_name):
    print("group naem =",group_name)
    return render(request,'index.html',{'groupname':group_name})