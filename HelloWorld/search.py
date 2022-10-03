from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.urls import reverse

# 表单
def search_form(request):# ,kw
    return render(request, 'search_form.html',)# 有值reverse的重定向返回kw{"kw":kw}


# 接收请求数据
def search(request):
    request.encoding = 'utf-8'
    print(request.body)
    print(request.path)
    if 'q' in request.GET and request.GET['q']:
        # message = '你搜索的内容为: ' + request.GET['q']
        message = '你搜索的内容为: ' + request.GET.get('q') + "<a href='https://www.runoob.com/'>菜鸟教程</a>"
    else:
        message = '你提交了空表单'
        # 重定向
        # return redirect(reverse('app02:qas',kwargs={"kw":3333}))
    return HttpResponse(message)