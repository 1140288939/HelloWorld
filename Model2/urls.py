"""HelloWorld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]
from django.conf.urls import url
from django.urls import path,re_path,include

from HelloWorld import view,search,search2


urlpatterns = [
     url(r'^search-form/$', search.search_form, name="search_form"),
     url(r'^search/$', search.search,name="search"),
     url(r'^search-post/$', search2.search_post, name="search_post"),
     re_path(r'^articles/([0-9]{4})/([0-9]{4})/$', view.runoob), # 正则路径
     re_path(r"^search1/(?P<kw>[0-9]{4})/$", search.search_form, name="qas"),
]