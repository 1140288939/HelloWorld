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

from HelloWorld import view,test_db,search,search2

urlpatterns = [
     url(r'^$', view.hello),
]
urlpatterns = [
     path('admin/', view.hello),
]
# re_path 兼容url()函数
urlpatterns = [
     re_path(r'^$', view.hello),
]

urlpatterns = [
     path('show/', view.show),
]

urlpatterns = [
     path('show/', view.runlist),
]
urlpatterns = [
     path('show/', view.filter),
     path('testdb_insert/', test_db.testdb_insert),
     path('testdb_query/', test_db.testdb_query),
     path('testdb_update/', test_db.testdb_update),
     path('testdb_delete/', test_db.testdb_delete),
     url(r'^search-form/$', search.search_form),
     url(r'^search/$', search.search),
]
