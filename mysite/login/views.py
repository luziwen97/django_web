from django.shortcuts import HttpResponse
from django.shortcuts import render
from login import models
# Create your views here.

user_list=[]

def index(request):

    if request.method == 'POST':
        username=request.POST.get("username")
        password = request.POST.get("password")
        p=request.POST.get("img")


        # 数据保存到数据库
        models.UserInfo.objects.create(user=username,pwd=password)


    # 数据库读取数据
    user_list = models.UserInfo.objects.all()

    #return HttpResponse('Hello Word!')
    return render(request,'index.html', {'data': user_list})

def home(request):
    if request.method=='GET':
        index=request.GET.get('index')

    return render(request,"index.html",locals())