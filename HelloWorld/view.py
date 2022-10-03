from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hello world ! ")


def runoob(request,unknow,unknow2):
    print(request,unknow,unknow2)
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, '1.html', context)


def show(request):
    return render(request, '1.html', {"show":"good", "hello":"hello world!","src":"scene1380.jpg"})

def runlist(request):
    list1 = ['1',"2"]
    return render(request, '1.html', {"list":list1})

def filter(request):
    import datetime
    now = datetime.datetime.now()
    views_str = "<a href='https://www.runoob.com/' style='text-decoration:none' target='_blank'>点击跳转</a>"
    list1 = ['1', "2","3","4","5"]
    dict1 = {"one":1,"two":2}
    athlete = [{"name":"zhangsan","hobby":[1,2,3]},{"name":"lisi","hobby":[12,22,32]}]
    return render(request,'1.html',{"hello":"abcdevdasffdsfab","num":89,"datetime":now, "views_str":views_str,
                                    "list":list1,"dict":dict1, "athlete_list":athlete,"user":"1"})
def index(request):
    return render(request,"index.html")