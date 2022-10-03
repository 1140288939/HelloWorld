from django.shortcuts import render
from django.views.decorators import csrf


# 接收POST请求数据
def search_post(request):
    ctx = {}
    print(request.body)
    print(request.path)
    print(request.method)
    if request.POST:
        print(1)
        # ctx['rlt'] = request.POST['q']
        ctx['rlt'] = request.POST.get('q')
    return render(request, "post.html", ctx)